from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'index.html')
def login(request):
    return render(request, 'login.html')
def signup(request):
    return render(request, 'signup.html')
def contact(request):
    return render(request, 'contact.html')
def add_hostel(request):
    return render(request, 'add_hostel.html')
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')
def profile(request):
    return render(request, 'profile.html')
def edit_hostel(request):
    return render(request, 'edit_hostel.html')
def hostel_details(request):
    return render(request, 'hostel_detail.html')
def dashboard(request):
    return render(request, 'dashboard.html')
