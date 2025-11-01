from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('contact/', views.contact, name='contact'),
    path('add_hostel/', views.add_hostel, name='add_hostel'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('profile/', views.profile, name='profile'),
    path('edit_hostel/', views.edit_hostel, name='edit_hostel'),
    path('hostel_details/', views.hostel_details, name='hostel_details'),
    path('dashboard/', views.dashboard, name='dashboard'),
]