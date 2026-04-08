# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
# from django.utils import timezone


class CustomUser(AbstractUser):
    """Extended User model with roles for PG owners and seekers."""
    
    ROLE_CHOICES = [
        ('manager', 'PG Manager'),
        ('seeker', 'Seeker'),
    ]
    
    user_role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='seeker'
    )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    
    def is_manager(self):
        return self.user_role == 'manager'
    
    def is_seeker(self):
        return self.user_role == 'seeker'
    
    def __str__(self):
        return f"{self.username} ({self.get_user_role_display()})"


class PGListing(models.Model):
    """Model for PG accommodations listed by managers."""
    
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='pg_listings',
        limit_choices_to={'user_role': 'manager'}
    )
    pg_name = models.CharField(max_length=200)
    description = models.TextField()
    city = models.CharField(max_length=100)
    address = models.TextField()
    price_per_month = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    rooms_available = models.IntegerField(validators=[MinValueValidator(1)])
    
    # Amenities as boolean fields
    has_wifi = models.BooleanField(default=False)
    has_ac = models.BooleanField(default=False)
    has_food = models.BooleanField(default=False)
    has_laundry = models.BooleanField(default=False)
    
    image = models.ImageField(upload_to='pg_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.pg_name} - {self.city}"
    
    def get_amenities(self):
        """Return list of available amenities."""
        amenities = []
        if self.has_wifi:
            amenities.append('WiFi')
        if self.has_ac:
            amenities.append('AC')
        if self.has_food:
            amenities.append('Food')
        if self.has_laundry:
            amenities.append('Laundry')
        return amenities


class Application(models.Model):
    """Model for applications submitted by seekers to PG listings."""
    
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
    ]
    
    pg = models.ForeignKey(
        PGListing,
        on_delete=models.CASCADE,
        related_name='applications'
    )
    applicant = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name='applications',
        limit_choices_to={'user_role': 'seeker'}
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    applied_on = models.DateTimeField(auto_now_add=True)
    message = models.TextField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ['pg', 'applicant']
        ordering = ['-applied_on']
    
    def __str__(self):
        return f"{self.applicant.username} applied to {self.pg.pg_name}"
