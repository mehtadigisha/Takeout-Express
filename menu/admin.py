from django.contrib import admin
from .models import Menu , CartItem

# Register your models here.

admin.site.register(Menu)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'product')

admin.site.register(CartItem,CartItemAdmin)