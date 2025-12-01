from django.shortcuts import render
from .models import User

# Create your views here.
def profile(request):
    context={
        'user':User.objects.all()
    }
    return render(request, 'profile.html')
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')
def contact(request):
    return render(request, 'contact.html')