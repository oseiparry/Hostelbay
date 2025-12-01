from django.contrib import admin
from.models import Hostel,Report,SystemSetting,Notification,HostelImage    
from booking.models import Booking
from accounts.models import User

# Register your models here.
admin.site.register(User)
admin.site.register(Hostel)
admin.site.register(Booking)
admin.site.register(SystemSetting)
admin.site.register(Notification)
admin.site.register(Report)
admin.site.register(HostelImage)