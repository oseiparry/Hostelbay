from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.loginView, name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),
    path('forgot_password/', views.forgot_password, name='forgot_password'),
    path('reset_password/<str:reset_id>/', views.reset_password, name='reset_password'),
    path('logout/', views.logoutView, name='logout'),
    path('reset_password_sent/<str:reset_id>/', views.reset_password_sent, name='password_reset_sent'),
    path("change-password/", views.change_password, name="change_password"),

]
  