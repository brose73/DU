"""
Author: Brandon Rose
Date: 03-09-18
Class: ICT 4370
Assignment#: 9
Description: Django URL patterns for login, logout and user registration. 
"""

from django.urls import path
from django.contrib.auth.views import login 

from . import views

app_name='users'

urlpatterns = [
    # Login Page
    path(r'login/', login, {'template_name': 'users/login.html'}, name='login'),
    # Registration Page
    path(r'register/', views.register, name='register'),
    # Logout Page
    path(r'logout/', views.logout_view, name='logout'),
]
