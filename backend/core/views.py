from django.contrib.auth import login, authenticate, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db.models import Sum

from .forms import RegisterForm
from .models import FoodDonation

User = get_user_model()


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
        'volunteer': 'dashboard_volunteer',
        'admin': 'dashboard_admin',
    }
    return redirect(role_redirects.get(role, 'dashboard_donor'))


@login_required
def dashboard_router(request):
    return redirect_dashboard(request.user.role)


# ================= DONOR DASHBOARD =================
@login_required
def dashboard_donor(request):
    donations = FoodDonation.objects.filter(donor=request.user).order_by('-created_at')

    total_donations = donations.count()
    total_food = donations.aggregate(Sum('quantity'))['quantity__sum'] or 0
    accepted_count = donations.filter(status='accepted').count()
    delivered_count = donations.filter(status='delivered').count()

    # 🔥 NEW: Expiry logic
    from django.utils import timezone
    from datetime import timedelta

    expiring_soon = 0

    for donation in donations:
        if donation.expiry_time:
            if donation.expiry_time <= timezone.now() + timedelta(hours=24):
                donation.is_expiring = True
                expiring_soon += 1
            else:
                donation.is_expiring = False
        else:
            donation.is_expiring = False

    context = {
        'donations': donations,
        'total_donations': total_donations,
        'total_food': total_food,
        'accepted_count': accepted_count,
        'delivered_count': delivered_count,
        'expiring_soon': expiring_soon,  # 🔥 NEW
    }

    return render(request, 'core/dashboard_donor.html', context)

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


# ================= VOLUNTEER DASHBOARD =================
@login_required
def dashboard_volunteer(request):
    donations = FoodDonation.objects.filter(status='accepted')

    context = {
        'deliveries_count': donations.count(),
        'distance': 120,   # dummy
        'earnings': 1500,  # dummy
        'donations': donations
    }

    return render(request, 'core/dashboard_volunteer.html', context)


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
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .models import FoodDonation
from datetime import datetime

@login_required
def add_food(request):
    if request.method == 'POST':
        try:
            expiry_input = request.POST.get('expiry_date')

            # Convert HTML datetime-local → Python datetime
            expiry_time = datetime.strptime(expiry_input, "%Y-%m-%dT%H:%M")

            FoodDonation.objects.create(
                donor=request.user,
                food_name=request.POST.get('food_name'),
                food_type=request.POST.get('food_type'),
                quantity=float(request.POST.get('quantity')),
                location=request.POST.get('location'),
                expiry_time=expiry_time,  # ✅ FIXED properly
                description=request.POST.get('description'),
                food_image=request.FILES.get('food_image')
            )

        except Exception as e:
            print("ERROR:", e)  # debug

    return redirect('dashboard_donor')
# ================= NGO ACCEPT =================
@login_required
def accept_food(request, id):
    donation = get_object_or_404(FoodDonation, id=id)

    donation.status = 'accepted'
    donation.ngo = request.user
    donation.save()

    return redirect('dashboard_ngo')


# ================= VOLUNTEER DELIVER =================
@login_required
def mark_delivered(request, id):
    if request.user.role != 'volunteer':
        return redirect('dashboard_router')

    food = get_object_or_404(FoodDonation, id=id)

    food.status = 'delivered'
    food.save()

    return redirect('dashboard_volunteer')

@login_required
def admin_portal(request):
    if request.user.role != 'admin':
        return redirect('dashboard_router')

    return render(request, 'core/admin_portal.html')