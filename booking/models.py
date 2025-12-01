from django.db import models
from accounts.models import User
from hostel.models import Hostel

# Create your models here.
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
    