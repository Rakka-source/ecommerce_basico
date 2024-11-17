# Generated by Django 5.1.3 on 2024-11-16 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_cartitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('shipping_address', models.TextField(verbose_name='Dirección de Envío')),
                ('cart_items', models.ManyToManyField(related_name='orders', to='shop.cartitem')),
            ],
        ),
    ]