# Generated by Django 4.2.5 on 2023-09-27 16:59

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=42)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=40)),
                ('date_of_reg', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('date_of_addition', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sum_of_order', models.DecimalField(decimal_places=2, default=0, max_digits=20, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)])),
                ('date_of_order', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homework2_shop_app.client')),
                ('products', models.ManyToManyField(to='homework2_shop_app.product')),
            ],
        ),
    ]