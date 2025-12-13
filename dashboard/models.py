from django.db import models
from accounts.models import User
from hostel.models import Hostel


# Create your models here.
class Report(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, )
    hostel = models.ForeignKey(Hostel, on_delete=models.CASCADE, )
    reason = models.TextField()
    review = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class SystemSetting(models.Model):
    site_name = models.CharField(max_length=100, default='Hostellink')
    support_emal = models.EmailField(default='support@hostellink.com')
    maintenance_mode = models.BooleanField(default=False)
    auto_approve = models.BooleanField(default=True)


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
