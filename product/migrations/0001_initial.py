# Generated by Django 5.1.3 on 2025-04-14 09:16

import django.db.models.deletion
import multiselectfield.db.fields
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('time', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered_at', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('status', models.CharField(blank=True, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('rejected', 'Rejected')], default='pending', max_length=10, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.URLField(max_length=300)),
                ('name', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('is_available', models.BooleanField(default=True)),
                ('size', multiselectfield.db.fields.MultiSelectField(choices=[('m', 'M'), ('l', 'L'), ('xl', 'XL'), ('lg', 'Lg'), ('xxl', 'XXL')], max_length=100)),
                ('color', multiselectfield.db.fields.MultiSelectField(choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'), ('yellow', 'Yellow'), ('orange', 'Orange'), ('purple', 'Purple'), ('pink', 'Pink'), ('brown', 'Brown'), ('gray', 'Gray'), ('black', 'Black'), ('white', 'White')], max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='product.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('size', models.CharField(blank=True, max_length=100, null=True)),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('status', models.CharField(blank=True, choices=[('pending', 'Pending'), ('approved', 'Approved'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('rejected', 'Rejected')], default='pending', max_length=20, null=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='product.order')),
                ('seller', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to=settings.AUTH_USER_MODEL)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('size', models.CharField(blank=True, choices=[('m', 'M'), ('l', 'L'), ('xl', 'XL'), ('lg', 'Lg'), ('xxl', 'XXL')], max_length=100, null=True)),
                ('color', models.CharField(blank=True, choices=[('red', 'Red'), ('blue', 'Blue'), ('green', 'Green'), ('yellow', 'Yellow'), ('orange', 'Orange'), ('purple', 'Purple'), ('pink', 'Pink'), ('brown', 'Brown'), ('gray', 'Gray'), ('black', 'Black'), ('white', 'White')], max_length=100, null=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='product.cart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='product.product')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.CharField(choices=[('⭐', '⭐'), ('⭐⭐', '⭐⭐'), ('⭐⭐⭐', '⭐⭐⭐'), ('⭐⭐⭐⭐', '⭐⭐⭐⭐'), ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐')], max_length=10)),
                ('review_text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='product.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
