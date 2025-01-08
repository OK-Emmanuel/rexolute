from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Setting up auth for the user
class User(AbstractUser):
    ROLE_CHOICES = [
        ('client', 'Client'),
        ('therapist', 'Therapist'),

    ]
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default="client")
    is_therapist = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

# Therpaist Specific Profile
class TherapistProfile(models.Model):
    user = models.OneToOneField('main_app.user', on_delete=models.CASCADE, related_name='therapist_profile')
    specialization = models.CharField(max_length=100, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    experience_years = models.PositiveIntegerField(blank=True, null=True)
    education = models.CharField(max_length=200, blank=True, null=True)
    certifications = models.CharField(max_length=200, blank=True, null=True)
    availability = models.TextField(blank=True, null=True)
    consultation_fee = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='therapist_profile_pictures/', blank=True, null=True)
    rating = models.FloatField(default=0.0)

# Automatically create Therapist Profile when a therapist user is created
@receiver(post_save, sender=User)
def create_therapist_profile(sender, instance, created, **kwargs):
    if created and instance.is_therapist:
        TherapistProfile.objects.create(user=instance)


# Session Model
class Session(models.Model):
    SESSION_STATUS = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    therapist = models.ForeignKey(TherapistProfile, on_delete=models.CASCADE, related_name='sessions')
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_sessions')
    session_date = models.DateTimeField()
    duration_minutes = models.PositiveIntegerField()
    status = models.CharField(max_length=10, choices=SESSION_STATUS, default='pending')
    notes = models.TextField(blank=True, null=True)

# Payment Model
class Payment(models.Model):
    PAYMENT_STATUS = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.OneToOneField(Session, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=10, choices=PAYMENT_STATUS, default='pending')
    payment_date = models.DateTimeField(auto_now_add=True)
    reference_id = models.CharField(max_length=100, unique=True)