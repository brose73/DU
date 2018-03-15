"""
Author: Brandon Rose
Date: 03-09-18
Class: ICT 4370
Assignment#: 9
Description: Django web page view configuration.
"""

from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from users.forms import SignUpForm


def logout_view(request):
    """Log the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('pizzas:index'))

def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Display blank registration form
        form = SignUpForm()
    else:
        # Process completed form
        form = SignUpForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #form.save()
            # Log the user in and redirect to home page
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('pizzas:index'))
    context = { 'form': form }
    return render(request, 'pizzas/register.html', context)
