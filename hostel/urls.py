from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('contact/', views.contact, name='contact'),
    path('add_hostel/', views.add_hostel, name='add_hostel'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('profile/', views.profile, name='profile'),
    path('edit_hostel/', views.edit_hostel, name='edit_hostel'),
    path('hostel_details/<slug:slug>/', views.hostel_details, name='hostel_detail'),
    path('hostel_details/', views.hostel_details, name='hostel_details'),
    path('dashboard/', views.dashboard, name='dashboard'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)