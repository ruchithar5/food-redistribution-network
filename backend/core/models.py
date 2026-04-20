from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from datetime import timedelta


# ================= USER MODEL =================
class User(AbstractUser):
    ROLE_CHOICES = (
        ('donor', 'Donor'),
        ('ngo', 'NGO'),
        ('volunteer', 'Volunteer'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='donor')

    def __str__(self):
        return self.username


# ================= FOOD DONATION =================
class FoodDonation(models.Model):

    FOOD_TYPES = [
        ('fresh', 'Fresh Produce'),
        ('cooked', 'Cooked Food'),
        ('packaged', 'Packaged Food'),
        ('dairy', 'Dairy Products'),
        ('bakery', 'Bakery Items'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('picked', 'Picked Up'),
        ('delivered', 'Delivered'),
    ]

    donor = models.ForeignKey(User, on_delete=models.CASCADE)

    ngo = models.ForeignKey(
        User,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='ngo_donations'
    )

    food_name = models.CharField(max_length=100)
    food_type = models.CharField(max_length=50, default='fresh')

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
    expiry_prediction = models.CharField(max_length=100, blank=True, null=True)
    blockchain_tx_hash = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

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
        ('volunteer', 'Volunteer'),
        ('admin', 'Admin'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    # 🔥 extra useful fields (future features)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    def __str__(self):
        return self.user.username