"""
Author: Brandon Rose
Date: 03-09-18
Class: ICT 4370
Assignment#: 10
Description: Django form for user pizza order
"""

from django import forms
from pizzas.models import Topping, Post, PizzaSize, CrustType
#from pizzas.models import Post


class OrderForm(forms.ModelForm):
    #toppings = []
    toppings = [(topping.id, str(topping)) for topping in Topping.objects.all()]
    sizes = [(size.id, str(size)) for size in PizzaSize.objects.all()]
    crusts = [(crust.id, str(crust)) for crust in CrustType.objects.all()]
    #toppings = (('Pepperoni', 'Blah'), ('Olives', 'Olives'),)
    selection = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices = toppings)
    size = forms.MultipleChoiceField(widget=forms.RadioSelect, choices = sizes)
    crust = forms.MultipleChoiceField(widget=forms.RadioSelect, choices = crusts)

    class Meta:
        model = Post
        exclude = ('', )     
