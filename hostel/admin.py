from django.contrib import admin
from.models import Hostel,HostelImage  

# Register your models here.
admin.site.register(Hostel)
admin.site.register(HostelImage)
admin.site.site_header = "HostelLink Admin"
admin.site.site_title = "HostelLink Admin Portal"
admin.site.index_title = "Welcome to HostelLink Admin Portal"

