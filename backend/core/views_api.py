from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
import json

from .models import Pickup


@login_required
@require_POST
def start_pickup(request, id):
    pickup = get_object_or_404(Pickup, id=id, volunteer=request.user)

    if pickup.status != 'accepted':
        return JsonResponse({'error': 'Invalid state'}, status=400)

    pickup.status = 'in-progress'
    pickup.pickup_time = timezone.now()
    pickup.save()

    return JsonResponse({'success': True})


@login_required
@require_POST
def complete_pickup(request, id):
    pickup = get_object_or_404(Pickup, id=id, volunteer=request.user)

    if pickup.status != 'in-progress':
        return JsonResponse({'error': 'Invalid state'}, status=400)

    data = json.loads(request.body or '{}')
    rating = int(data.get('rating', 5))

    pickup.complete(rating)

    return JsonResponse({'success': True})


@login_required
@require_POST
def update_availability(request, status):
    request.user.is_available = (status == 'online')
    request.user.save()

    return JsonResponse({'success': True})