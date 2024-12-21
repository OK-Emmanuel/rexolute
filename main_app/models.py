from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

# Setting up auth for the user
class user(AbstractUser):
    is_therrapist = models.BooleanField(default=False)

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

# Connetcting a therapist profile to a user
@receiver(post_save, sender=User)
def create_therapist_profile(sender, instance, created, **kwargs):
    if created and instance.is_therapist:
        TherapistProfile.objects.create(user=instance)