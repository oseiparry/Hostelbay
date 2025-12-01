from django.contrib import admin
from .models import SystemSetting,Notification,Report

# Register your models here.
admin.site.register(SystemSetting)
admin.site.register(Notification)
admin.site.register(Report)