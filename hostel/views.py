from django.shortcuts import render
from django.shortcuts import get_object_or_404
from hostel.models import Hostel, HostelImage
from accounts.models import User, Manager


# Create your views here.
def home(request):
    context = {
        'hostels': Hostel.objects.all(),
        'hostel_image': HostelImage.objects.all(),
        'manager': User.objects.filter(role='manager')
    }
    return render(request, 'index.html', context)


def add_hostel(request):
    return render(request, 'add_hostel.html')


def edit_hostel(request):
    return render(request, 'edit_hostel.html')


def hostel_details(request, slug):
    hostel = get_object_or_404(Hostel, slug=slug)
    hostel_image = hostel.images.first()
    hostel_manager = User.objects.filter(role='manager')
    managers = Manager.objects.all()

    context = {
        'hostel': hostel,
        'hostel_image': hostel_image,
        'hostel_manager': hostel_manager,
        'managers': managers
    }
    return render(request, 'hostel_detail.html', context)
