from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from accounts.models import User,Manager


# Create your models here.
class Hostel(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('active', 'Active'),
        ('rejected', 'Rejected'),
    ]
    LOCATIONS = [
        ('Abeka', 'Abeka'),
        ('Tesano', 'Tesano'),
        ('Tapaz', 'Lapaz'),
        ('Aladjo', 'Aladjo'),
    ]
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=50, choices=LOCATIONS, default='none')
    manager = models.ForeignKey(User, on_delete=models.CASCADE, )


    # prices
    price_for_one_in_a_room = models.DecimalField(max_digits=8, decimal_places=2, default='0.00')
    price_for_two_in_a_room = models.DecimalField(max_digits=8, decimal_places=2, default='0.00')
    price_for_three_in_a_room = models.DecimalField(max_digits=8, decimal_places=2, default='0.00')
    price_for_four_in_a_room = models.DecimalField(max_digits=8, decimal_places=2, default='0.00')
    contact = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateField(auto_now_add=True)
    priceFilter = models.CharField(max_length=10, default='0.00')
    slug = models.SlugField(unique=True, blank=True, null=True)

    # amenities
    wifi = models.BooleanField(default=False)
    ac = models.BooleanField(default=False)
    security = models.BooleanField(default=False)
    kitchen = models.BooleanField(default=False)
    laundry = models.BooleanField(default=False)
    parking = models.BooleanField(default=False)
    gym = models.BooleanField(default=False)
    study_room = models.BooleanField(default=False)
    common_lounge = models.BooleanField(default=False)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    manager=models.ForeignKey(Manager, 
                              on_delete=models.CASCADE, 
                                related_name='hostels')
    

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    


class HostelImage(models.Model):
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='hostel_images/', blank=True, null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f'Image for {self.hostel.name}'
