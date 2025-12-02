from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify 

# Create your models here.
class User(AbstractUser):
    USER_ROLES=[ 
        ('student', 'Student'),
        ('manager', 'Hostel Manager'),
        ('admin', 'Admin'),
    ]
    role=models.CharField(max_length=20, choices=USER_ROLES)
    phone=models.CharField(max_length=15)
    profile_image=models.ImageField(upload_to='profiles/', blank=True, null=True)

    def __str__(self):
        return f'{self.username} ({self.role})'
    
class Manager(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    phone=models.CharField(max_length=15)
    whatsapp=models.CharField(max_length=20, blank=True)
    profile_pic=models.ImageField(upload_to='profiles/', blank=True)