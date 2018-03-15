"""
Author: Brandon Rose
Date: 03-09-18
Class: ICT 4370
Assignment#: 9
Description: Django URL pattern matching 
"""

from django.urls import path

from . import views

app_name = 'pizzas'

urlpatterns = [
    #homepage
    path('', views.index, name='index'),
    #pizza types
    path(r'pizzas/', views.pizzas, name='pizzas'),
    #topppings per pizza
    path(r'pizza/<int:pizza_id>/', views.pizza, name='pizza'),
    #order page
    path(r'orders/', views.orders, name='orders'),
    #order summary
    path(r'order_summary/', views.order_summary, name='order_summary')
]
