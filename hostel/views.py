from django.shortcuts import render
from django.shortcuts import get_object_or_404
from.models import Hostel,HostelImage
from accounts.models import User

# Create your views here.
def home(request):
    context={
        'hostels':Hostel.objects.all(),
        'hostel_image':HostelImage.objects.all()
    }
    return render(request, 'index.html',context)

def add_hostel(request):
    return render(request, 'add_hostel.html')

def edit_hostel(request):
    return render(request, 'edit_hostel.html')

def hostel_details(request, slug):
    context={
        'user':User.objects.all()
    }
    hostel=get_object_or_404(Hostel, slug=slug)
    return render(request, 'hostel_detail.html', {'hostel':hostel})

