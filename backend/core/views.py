from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum
from django.http import JsonResponse
from django.utils import timezone
from .forms import RegisterForm
from .models import FoodDonation,Notification
from .models import Pickup
from .ai_food_detector import analyze_food_image
User = get_user_model()
from django.db.models.functions import TruncMonth
from django.db.models import Count
from ai.food_ai import analyze_food_image
# ================= REGISTER =================
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect_dashboard(user.role)
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")
    else:
        form = RegisterForm()

    return render(request, 'core/register.html', {'form': form})


# ================= LOGIN =================
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect_dashboard(user.role)
        else:
            messages.error(request, "Invalid username or password")

    return render(request, 'core/login.html')


# ================= REDIRECT =================
def redirect_dashboard(role):
    role_redirects = {
        'donor': 'dashboard_donor',
        'ngo': 'dashboard_ngo',
        'delivery': 'dashboard_delivery',   # ✅ updated
        'admin': 'dashboard_admin',
    }
    return redirect(role_redirects.get(role, 'dashboard_donor'))


@login_required
def dashboard_router(request):
    return redirect_dashboard(request.user.role)


# ================= DONOR DASHBOARD =================
@login_required
def dashboard_donor(request):

    # ALL DONATIONS
    donations = FoodDonation.objects.filter(
        donor=request.user
    ).order_by('-created_at')

    # STATISTICS
    total_donations = donations.count()

    total_food_saved = sum(
        float(d.quantity) for d in donations
    ) if donations else 0

    delivered_count = donations.filter(
        status="delivered"
    ).count()

    pending_count = donations.filter(
        status="pending"
    ).count()

    unique_ngos = donations.exclude(
        ngo=None
    ).values('ngo').distinct().count()

    # AI SCORE AVG
    ai_scores = [
        d.ai_quality_score
        for d in donations
        if d.ai_quality_score
    ]

    avg_ai_score = (
        round(sum(ai_scores) / len(ai_scores), 1)
        if ai_scores else 0
    )

    # CARBON SAVED
    carbon_saved = round(total_food_saved * 2.5, 1)

    # DONOR RATING
    donor_rating = 4.8

    # NOTIFICATIONS
    notifications = Notification.objects.filter(
        user=request.user
    ).order_by('-created_at')[:5]

    context = {
        "donations": donations,
        "notifications": notifications,

        "total_donations": total_donations,
        "total_food_saved": total_food_saved,
        "delivered_count": delivered_count,
        "pending_count": pending_count,
        "unique_ngos": unique_ngos,
        "avg_ai_score": avg_ai_score,
        "carbon_saved": carbon_saved,
        "donor_rating": donor_rating,
    }

    return render(
        request,
        "core/dashboard_donor.html",
        context
    )
# ================= NGO DASHBOARD =================
@login_required
def dashboard_ngo(request):
    donations = FoodDonation.objects.all().order_by('-id')

    accepted_count = donations.filter(status='accepted').count()

    context = {
        'donations': donations,
        'total_donations': donations.count(),
        'accepted_count': accepted_count,
    }

    return render(request, 'core/dashboard_ngo.html', context)


# ================= DELIVERY DASHBOARD =================
@login_required
def dashboard_delivery(request):
    donations = FoodDonation.objects.filter(status='accepted')

    context = {
        'deliveries_count': donations.count(),
        'distance': 120,   # dummy for now
        'earnings': 1500,  # dummy for now
        'donations': donations
    }

    return render(request, 'core/dashboard_delivery.html', context)


# ================= ADMIN DASHBOARD =================
@login_required
def dashboard_admin(request):
    if request.user.role != 'admin':
        return redirect('dashboard_router')

    context = {
        'total_users': User.objects.count(),
        'total_donations': FoodDonation.objects.count(),
    }

    return render(request, 'core/dashboard_admin.html', context)


# ================= HOME =================
def home(request):
    return render(request, 'core/home.html')


# ================= ADD FOOD =================
from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import FoodDonation
import hashlib
import random
from django.utils.dateparse import parse_datetime

@login_required
def add_food(request):

    if request.method == "POST":

        # =========================
        # DATETIME CONVERSION
        # =========================
        expiry_str = request.POST.get("expiry_time")
        expiry_time = parse_datetime(expiry_str)

        if expiry_time and timezone.is_naive(expiry_time):
            expiry_time = timezone.make_aware(expiry_time)

        # =========================
        # CREATE DONATION
        # =========================
        food = FoodDonation.objects.create(
            donor=request.user,
            food_name=request.POST.get("food_name"),
            food_type=request.POST.get("food_type"),
            quantity=request.POST.get("quantity"),
            location=request.POST.get("location"),
            expiry_time=expiry_time,
            description=request.POST.get("description"),
            status="pending",

            # MAP LOCATION
            latitude=request.POST.get("latitude") or None,
            longitude=request.POST.get("longitude") or None,

            # PICKUP TIME
            pickup_start_time=request.POST.get("pickup_start_time") or None,
            pickup_end_time=request.POST.get("pickup_end_time") or None,

            # URGENCY
            urgency_level=request.POST.get("urgency_level") or "normal",
        )

        # =========================
        # IMAGE UPLOAD + AI ANALYSIS
        # =========================
        if request.FILES.get("image"):

            food.image = request.FILES.get("image")
            food.save()

            # CREATE NOTIFICATION
            Notification.objects.create(
                user=request.user,
                message=f"Your donation '{food.food_name}' was posted successfully."
)

            # AI ANALYSIS
            result = analyze_food_image(food.image.path)

            food.ai_quality_score = result["score"]
            food.food_condition = result["condition"]

        else:

            # DEFAULT VALUES
            food.ai_quality_score = 50
            food.food_condition = "No Image"

        # =========================
        # AI NGO MATCH SCORE
        # =========================
        food.ai_match_score = random.randint(80, 100)

        # =========================
        # EXPIRY PREDICTION
        # =========================
        if food.is_expiring_soon():
            food.expiry_prediction = "Expiring Soon"
        else:
            food.expiry_prediction = "Fresh Food"

        # =========================
        # BLOCKCHAIN HASH
        # =========================
        hash_data = (
            f"{food.food_name}"
            f"{food.quantity}"
            f"{food.created_at}"
        )

        food.blockchain_tx_hash = hashlib.sha256(
            hash_data.encode()
        ).hexdigest()

        # =========================
        # FINAL SAVE
        # =========================
        food.save()

        return redirect("dashboard_donor")

    return redirect("dashboard_donor")

# ================= NGO ACCEPT =================
@login_required
def accept_food(request, id):
    donation = get_object_or_404(FoodDonation, id=id)

    donation.status = 'accepted'
    donation.ngo = request.user
    donation.save()

    return redirect('dashboard_ngo')


# ================= DELIVERY COMPLETE =================
@login_required
def mark_delivered(request, id):
    if request.user.role != 'delivery':
        return redirect('dashboard_router')

    food = get_object_or_404(FoodDonation, id=id)

    food.status = 'delivered'
    food.save()

    return redirect('dashboard_delivery')


# ================= ADMIN PORTAL =================
@login_required
def admin_portal(request):
    if request.user.role != 'admin':
        return redirect('dashboard_router')

    return render(request, 'core/admin_portal.html')


# ================= REQUEST FOOD =================
def request_food(request):
    if request.method == "POST":
        food_item = request.POST.get("food_item")
        quantity = request.POST.get("quantity")
        urgency = request.POST.get("urgency")
        notes = request.POST.get("notes")

        print(food_item, quantity, urgency, notes)

        return redirect('dashboard_ngo')

    return redirect('dashboard_ngo')


# ================= API: START PICKUP =================
@login_required
def start_pickup(request, id):
    from .models import Pickup
    pickup = get_object_or_404(Pickup, id=id)
    pickup.status = 'in-progress'
    pickup.save()
    return JsonResponse({'status': 'success'})


# ================= API: COMPLETE PICKUP =================
@login_required
def complete_pickup(request, id):
    from .models import Pickup
    pickup = get_object_or_404(Pickup, id=id)
    pickup.status = 'completed'
    pickup.save()
    return JsonResponse({'status': 'done'})

@login_required
def get_assigned_pickups(request):
    pickups = Pickup.objects.filter(
        volunteer=request.user
    ).exclude(status='completed').select_related('donation', 'donation__donor')

    data = []

    for p in pickups:
        data.append({
            "id": p.id,
            "status": p.status,
            "distance": p.distance,
            "food_name": p.donation.food_name,
            "location": p.donation.location,
            "donor": p.donation.donor.username,
            "earnings": p.earnings,
        })

    return JsonResponse({"pickups": data})

@login_required
def edit_donation(request, donation_id):

    donation = FoodDonation.objects.get(id=donation_id)

    if request.method == 'POST':

        donation.food_name = request.POST.get('food_name')
        donation.food_type = request.POST.get('food_type')
        donation.quantity = request.POST.get('quantity')
        donation.location = request.POST.get('location')
        donation.description = request.POST.get('description')

        expiry_str = request.POST.get('expiry_time')

        from django.utils.dateparse import parse_datetime
        donation.expiry_time = parse_datetime(expiry_str)

        if request.FILES.get('image'):
            donation.image = request.FILES.get('image')

        donation.save()

        return redirect('dashboard_donor')

    return render(request, 'core/edit_donation.html', {
        'donation': donation
    })

@login_required
def delete_donation(request, donation_id):

    if request.method == 'POST':

        try:

            donation = FoodDonation.objects.get(
                id=donation_id,
                donor=request.user
            )

            # prevent deleting accepted donations
            if donation.status != 'pending':

                return JsonResponse({
                    'success': False,
                    'error': 'Cannot delete accepted donation'
                })

            donation.delete()

            return JsonResponse({
                'success': True
            })

        except FoodDonation.DoesNotExist:

            return JsonResponse({
                'success': False,
                'error': 'Donation not found'
            })

    return JsonResponse({
        'success': False,
        'error': 'Invalid request'
    })