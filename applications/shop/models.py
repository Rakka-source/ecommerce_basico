from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre del Producto")
    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    price = models.IntegerField(verbose_name="Precio")
    image = models.ImageField(upload_to='product_images/', blank=True, null=True, verbose_name="Imagen del Producto")

    def __str__(self):
        return self.name

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
    quantity = models.PositiveIntegerField(default=1)

    def total_cost(self):
        return self.quantity * self.product.price

class Order(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    shipping_address = models.TextField(verbose_name="Dirección de Envío")
    cart_items = models.ManyToManyField(CartItem, related_name='orders')
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Costo Total", default=0.0)

    def calculate_total(self):
        return sum(item.total_cost() for item in self.cart_items.all())

    def __str__(self):
        return f"Pedido #{self.id} - {self.created_at.strftime('%Y-%m-%d')}"