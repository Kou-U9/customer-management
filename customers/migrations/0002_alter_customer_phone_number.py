# Generated by Django 5.1.6 on 2025-03-16 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=255, verbose_name='電話番号'),
        ),
    ]
