from django.contrib import admin
from .models import Produto, Client
# Register your models here.
# import ours models(created in models.py) and add to panel Admin.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')

class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email')

admin.site.register(Produto, ProductAdmin)
# admin.site.register(Client, ClientAdmin)
admin.site.register(Client)