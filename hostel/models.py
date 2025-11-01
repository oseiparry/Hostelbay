from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    USER_ROLES=[
        ('student', 'Student'),
        ('manager', 'Hostel Manager'),
        ('admin', 'Admin'),
    ]
    role=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    profile_image=models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return f'{self.username} ({self.role})'
    
class Hostel(models.Model):
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('active','Active'),
        ('rejected','Rejected'),
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

    def __str__(self):
        return self.name
    
class HostelImage(models.Model):
    hostel=models.ForeignKey(Hostel, on_delete=models.CASCADE, related_name='images')
    image=models.ImageField(upload_to='hostel_images/')
    uploaded_at=models.DateTimeField(auto_now_add=True)

class Booking(models.Model):
    STATUS_CHOICES=[
        ('pending','Pending'),
        ('approved', 'Approved'),
        ('rejected', 'Rejected'),
        ('cancelled', 'Cancelled'),
      ]
    student=models.ForeignKey(User, on_delete=models.CASCADE , limit_choices_to={'role':'student'})
    hostel=models.ForeignKey(Hostel,  on_delete=models.CASCADE,)
    status=models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    booked_on=models.DateTimeField(auto_now_add=True)
    notes=models.TextField(blank=True)

    def __str__(self):
        return f'{self.student.username} {self.hostel.name}'
    
    
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