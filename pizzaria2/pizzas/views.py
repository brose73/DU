"""
Author: Brandon Rosed
Date: 03-09-18
Class: ICT 4370
Assignment#: 9
Description: Django web page views and html docs
"""

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate

from .models import Pizza, Post, Topping, CrustType, PizzaSize
from django.contrib.auth.decorators import login_required
from pizzas.forms import OrderForm

# Create your views here.

def index(request):
    return render(request, 'pizzas/index.html')

def pizzas(request):
    """Show available pizzas"""
    pizzas = Pizza.objects.order_by('name')
    context = {'pizzas':pizzas}
    return render(request, 'pizzas/pizzas.html', context)

def pizza(request, pizza_id):
    """Show toppings associated with a pizza"""
    pizza = Pizza.objects.get(id=pizza_id)
    toppings = pizza.topping_set.all()
    context = { 'pizza':pizza, 'toppings':toppings }
    return render(request, 'pizzas/toppings.html', context) 

@login_required
def orders(request):
    "Allow user to order if they are logged in"
    selections = Post.objects.all()
    crusts = CrustType.objects.all()
    sizes = PizzaSize.objects.get(id=1)
    if request.method != 'POST':
        # Display blank registration form
        form = OrderForm()
    else:
        # Process completed form
        form = OrderForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()


            return redirect('pizzas:orders')
    context = { 'form': form, 'selections': selections, 'crusts': crusts, 'sizes': sizes }
    return render(request, 'pizzas/orders.html', context)


def order_summary(request):
    selected_items = Post.objects.all()
    form = OrderForm()
    context = {'form': form, 'selected_items': selected_items }
    return render(request, 'pizzas/orders.html', context)
