# Generated by Django 5.0.7 on 2024-08-09 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('product_code', models.CharField(max_length=100)),
                ('quantity', models.IntegerField()),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('due_date', models.DateField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('approved', 'Approved'), ('disapproved', 'Disapproved')], default='pending', max_length=20)),
                ('project_name', models.CharField(max_length=255)),
                ('project_code', models.CharField(max_length=100)),
                ('order_name', models.CharField(max_length=255)),
                ('project_phase', models.CharField(max_length=100)),
                ('project_consultant', models.CharField(max_length=255)),
                ('project_location', models.CharField(max_length=255)),
            ],
        ),
    ]
