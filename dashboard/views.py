from django.shortcuts import render
from accounts.models import User
from .models import Hostel, Report
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Sum


# Create your views here.
def is_manager(user):
    return user.is_authenticated and (user.role == 'admin' or user.is_superuser)


@user_passes_test(is_manager or is_admin)
def dashboard(request):
    manager = request.user

    hostels = Hostel.objects.all()
    context = {
        'my_hostels': hostels,
    }
    return render(request, 'dashboard.html', context)


def is_admin(user):
    return user.is_authenticated and (user.role == 'admin' or user.is_superuser)


@user_passes_test(is_admin)
def admin_dashboard(request):
    total_users = User.objects.count()
    total_hostels = Hostel.objects.count()
    pending_hostels = Hostel.objects.filter(status='pending').count()
    total_reports = Report.objects.count()
    total_views = Hostel.objects.aggregate(total_views=Sum('view_count'))['total_views'] or 0

    users = User.objects.all().order_by('date_joined')[:10]
    hostels = Hostel.objects.all().order_by('created_at')[:10]

    context = {
        'total_users': total_users,
        'total_hostels': total_hostels,
        'pending_hostels': pending_hostels,
        'total_reports': total_reports,
        'users': users,
        'hostels': hostels,
        'total_views': total_views,
    }
    return render(request, 'admin_dashboard.html', context)
