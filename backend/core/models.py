from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import timedelta


# ================= USER MODEL =================
class User(AbstractUser):
    ROLE_CHOICES = (
        ('donor', 'Donor'),
        ('ngo', 'NGO'),
        ('delivery', 'Delivery Person'),  
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='donor')
    phone = models.CharField(max_length=15, blank=True)
    organization_name = models.CharField(max_length=200, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return f"{self.email} ({self.role})"


# ================= FOOD DONATION =================
class FoodDonation(models.Model):

    FOOD_TYPES = [
        ('fresh', 'Fresh Produce'),
        ('cooked', 'Cooked Food'),
        ('packaged', 'Packaged Food'),
        ('dairy', 'Dairy Products'),
        ('bakery', 'Bakery Items'),
    ]

    URGENCY_CHOICES = [
    ('normal', 'Normal'),
    ('high', 'High'),
    ('emergency', 'Emergency'),
    ]  

    urgency_level = models.CharField(
        max_length=20,
        choices=URGENCY_CHOICES,
        default='normal'
    )

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('picked', 'Picked Up'),
        ('delivered', 'Delivered'),
    ]

    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    ngo = models.ForeignKey(
    'NGOProfile',
    on_delete=models.SET_NULL,
    null=True,
    blank=True
)
    ngo = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='ngo_donations'
    )

    food_name = models.CharField(max_length=100)
    food_type = models.CharField(max_length=50, default='fresh')
    ai_quality_score = models.IntegerField(default=0)

    food_condition = models.CharField(
        max_length=50,
        default="Fresh"
    )
    quantity = models.FloatField()  # 🔥 better than Integer

    location = models.CharField(max_length=200)

    expiry_time = models.DateTimeField()

    description = models.TextField(blank=True)
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    image = models.ImageField(upload_to='food_images/', null=True, blank=True)

    # 🔥 AI + Blockchain placeholders
    ai_match_score = models.IntegerField(null=True, blank=True)
    ai_quality_score = models.IntegerField(null=True, blank=True)
    expiry_prediction = models.CharField(max_length=100, blank=True, null=True)
    blockchain_tx_hash = models.CharField(max_length=255, blank=True, null=True)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    pickup_start_time = models.TimeField(null=True, blank=True)
    pickup_end_time = models.TimeField(null=True, blank=True)
    accepted_at = models.DateTimeField(
    null=True,
    blank=True
)

    picked_at = models.DateTimeField(
    null=True,
    blank=True
)

    delivered_at = models.DateTimeField(
    null=True,
    blank=True
)
    # ================= SMART PROPERTIES =================

    def is_expiring_soon(self):
        return self.expiry_time <= timezone.now() + timedelta(hours=2)

    def is_expired(self):
        return self.expiry_time < timezone.now()

    def __str__(self):
        return f"{self.food_name} ({self.quantity} kg)"


# ================= PROFILE =================
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    ROLE_CHOICES = [
        ('donor', 'Donor'),
        ('ngo', 'NGO'),
        ('delivery', 'Delivery Person'),
        ('admin', 'Admin'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    # 🔥 extra useful fields (future features)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Pickup(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('in-progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    donation = models.ForeignKey(FoodDonation, on_delete=models.CASCADE)
    volunteer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pickups')

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')

    distance = models.FloatField(default=0)
    pickup_time = models.DateTimeField(null=True, blank=True)
    completed_at = models.DateTimeField(null=True, blank=True)

    rating = models.IntegerField(null=True, blank=True)
    earnings = models.FloatField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Pickup #{self.id} - {self.donation.food_name}"

    def complete(self, rating=None):
        self.status = 'completed'
        self.completed_at = timezone.now()
        if rating:
            self.rating = rating
            self.earnings = 50 + (rating * 10)
        self.save()