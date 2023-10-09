from django.contrib import admin
from .models import Product,Client,Order

# Register your models here.
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'date_of_order', 'client', 'sum_of_order']
    ordering = ['client', '-date_of_order']
    list_filter = ['date_of_order']
    search_fields = ['client__client_name', 'products__product_name']
    search_help_text = 'Enter client or product name to find orders.'
    fields = ['client', 'products', 'sum_of_order', 'date_of_order']
    readonly_fields = ['client', 'date_of_order']


class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_name']
    ordering = ['client_name']
    search_fields = ['client_name']
    search_help_text = 'Enter client name.'
    fields = ['client_name', 'email', 'phone', 'address', 'date_of_reg']
    readonly_fields = ['client_name', 'email', 'date_of_reg']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name', 'price', 'quantity', 'image']
    ordering = ['product_name']
    search_fields = ['product_name']
    search_help_text = 'Enter product name.'
    readonly_fields = ['date_of_addition', 'quantity']


admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)

