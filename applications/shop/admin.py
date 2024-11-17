from django.contrib import admin
from .models import Product,CartItem,Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image')  # Campos que se mostrarán en la lista del administrador
    search_fields = ('name',)  # Permitir búsqueda por nombre
    list_filter = ('price',)  # Agregar filtro por precio


@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'total_cost')
    search_fields = ('product__name',)
    list_filter = ('product',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_at', 'calculate_total', 'shipping_address')
    search_fields = ('shipping_address',)
    list_filter = ('created_at',)