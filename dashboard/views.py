from django.shortcuts import render
from accounts.models import User
from.models import Hostel,Report
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def dashboard(request):
    return render(request, 'dashboard.html')

def is_admin(user):
    return user.is_authenticated and (user.role == 'admin' or user.is_superuser)

@user_passes_test(is_admin)
def admin_dashboard(request):
    total_users=User.objects.count()
    total_hostels=Hostel.objects.count()
    pending_hostels=Hostel.objects.filter(status='pending').count()
    total_reports=Report.objects.count()

    users=User.objects.all().order_by('date_joined')[:10]
    hostels=Hostel.objects.all().order_by('created_at')[:10]

    context={
        'total_users':total_users,
        'total_hostels':total_hostels,
        'pending_hostels':pending_hostels,
        'total_reports':total_reports,
        'users':users,
        'hostels':hostels,
    }
    return render(request, 'admin_dashboard.html', context)
