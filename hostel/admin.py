from django.contrib import admin
from.models import User,Hostel,Booking,Report,SystemSetting,Notification    

# Register your models here.
admin.site.register(User)
admin.site.register(Hostel)
admin.site.register(Booking)
admin.site.register(SystemSetting)
admin.site.register(Notification)
admin.site.register(Report)