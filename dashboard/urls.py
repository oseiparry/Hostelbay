from django.urls import path
from . import views
urlpatterns = [
        path('dashboard/', views.dashboard, name='dashboard'),
        path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),

]
