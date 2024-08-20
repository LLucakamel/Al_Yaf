# Generated by Django 5.0.7 on 2024-08-09 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('code', models.CharField(max_length=100, unique=True)),
                ('quantity', models.IntegerField()),
                ('supplier', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='product_images/')),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
    ]
