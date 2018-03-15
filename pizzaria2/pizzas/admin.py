from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Pizza, Topping, PizzaSize, CrustType
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(PizzaSize)
admin.site.register(CrustType)
