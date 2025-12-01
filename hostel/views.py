from django.shortcuts import render
from django.shortcuts import get_object_or_404
from accounts.models import User
from booking.models import Booking
from.models import Hostel,Report,SystemSetting,Notification,HostelImage
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def home(request):
    context={
        'hostels':Hostel.objects.all(),
        'hostel_image':HostelImage.objects.all()
    }
    return render(request, 'index.html',context)
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')
def contact(request):
    return render(request, 'contact.html')
def add_hostel(request):
    return render(request, 'add_hostel.html')


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
def profile(request):
    return render(request, 'profile.html')
def edit_hostel(request):
    return render(request, 'edit_hostel.html')

def hostel_details(request, slug):
    hostel=get_object_or_404(Hostel, slug=slug)
    return render(request, 'hostel_detail.html', {'hostel':hostel})
def dashboard(request):
    return render(request, 'dashboard.html')
