from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify 
from accounts.models import User

# Create your models here.
    
class Hostel(models.Model):
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('active','Active'),
        ('rejected','Rejected'),
    ]
    LOCATIONS=[
        ('abeka','Abeka'),
        ('tesano', 'Tesano'),
        ('lapaz','Lapaz'),
        ('aladjo','Aladjo'),
    ]
    name=models.CharField(max_length=100)
    location=models.TextField()
    manager=models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'manager'})
    capacity=models.IntegerField()
    available_rooms=models.IntegerField()
    price=models.DecimalField(max_digits=8, decimal_places=2)
    contact=models.TextField()
    status=models.CharField(max_length=50, choices=STATUS_CHOICES, default='pending')
    created_at=models.DateField(auto_now_add=True)
    locationFilter=models.CharField(max_length=50, choices=LOCATIONS, default='none')
    priceFilter=models.CharField(max_length=10, default='0.00')
    slug=models.SlugField(unique=True, blank=True, null=True)

    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug=slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class HostelImage(models.Model):
    hostel=models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='images')
    image=models.ImageField(upload_to='hostel_images/')
    uploaded_at=models.DateTimeField(auto_now_add=True)

    
class Report(models.Model):
    name=models.ForeignKey(User, on_delete=models.CASCADE, )
    hostel=models.ForeignKey(Hostel, on_delete=models.CASCADE,)
    reason=models.TextField()
    review=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)

class SystemSetting(models.Model):
    site_name=models.CharField(max_length=100, default='Hostellink')
    support_emal=models.EmailField(default='support@hostellink.com')
    maintenance_mode=models.BooleanField(default=False)
    auto_approve=models.BooleanField(default=True)

class Notification(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    message=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    is_read=models.BooleanField(default=False)