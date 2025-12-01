from django.urls import path
from . import views
urlpatterns = [
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('contact/', views.contact, name='contact'),

]
