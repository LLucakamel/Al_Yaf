# Generated by Django 5.0.7 on 2024-08-19 11:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_alter_order_requester'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Product',
        ),
    ]
