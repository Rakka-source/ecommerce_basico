from django.shortcuts import render, redirect, get_object_or_404
from applications.shop.models import Product, CartItem


# Create your views here.
def product_list(request):
    products = Product.objects.all()  # Obtener todos los productos
    return render(request, 'home.html', {'products': products})

# Ver producto
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_detail.html', {'product': product})

# Agregar al carrito
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('view_cart')

# Ver carrito
def view_cart(request):
    cart_items = CartItem.objects.all()
    total = sum(item.total_cost() for item in cart_items)
    return render(request, 'view_cart.html', {'cart_items': cart_items, 'total': total})

# Formulario de compra
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import CartItem, Order

def checkout(request):
    # Obtener todos los elementos del carrito
    cart_items = CartItem.objects.all()
    total_cost = sum(item.total_cost() for item in cart_items)

    if request.method == "POST":
        shipping_address = request.POST.get('shipping_address')

        # Guardar la orden
        order = Order.objects.create(
            shipping_address=shipping_address,
            total_cost=total_cost
        )
        order.cart_items.set(cart_items)  # Asociar los elementos del carrito con la orden

        # Limpiar el carrito
        cart_items.delete()

        return render(request, 'checkout_complete.html', {'order': order})

    return render(request, 'checkout.html', {'cart_items': cart_items, 'total_cost': total_cost})
