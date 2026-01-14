from django.shortcuts import render
from django.shortcuts import get_object_or_404
from hostel.models import Hostel
from accounts.models import User
from django.db.models import F


# Create your views here.
def home(request):
    if request.user.is_authenticated:
        hostels=Hostel.objects.filter(school=request.user.school, status='active')
    else:
        hostels = Hostel.objects.filter( status='active')
    context = {
        'hostels': hostels,
        'manager': User.objects.filter(role='manager')
    }
    return render(request, 'index.html', context)


def add_hostel(request):
    return render(request, 'add_hostel.html')


def edit_hostel(request):
    return render(request, 'edit_hostel.html')


def hostel_details(request, slug):
    hostel = get_object_or_404(Hostel, slug=slug)
    hostel_manager = User.objects.filter(role='manager')
    hostel_image = hostel.image
    Hostel.objects.filter(id=hostel.id).update(view_count=F('view_count') + 1)
    request.session[f'viewed_{hostel.id}'] = True
    hostel.refresh_from_db()

    context = {
        'hostel': hostel,
        'hostel_image': hostel_image,
        'hostel_manager': hostel_manager,
        'manager': hostel.manager,
    }
    return render(request, 'hostel_detail.html', context)
