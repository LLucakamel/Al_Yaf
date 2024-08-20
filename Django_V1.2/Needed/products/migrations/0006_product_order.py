# Generated by Django 5.0.7 on 2024-08-19 11:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_delete_product'),
        ('products', '0005_remove_product_supplier'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='order',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='ordered_products', to='orders.order'),
            preserve_default=False,
        ),
    ]
