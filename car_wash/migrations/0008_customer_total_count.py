# Generated by Django 3.0.3 on 2020-04-26 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_wash', '0007_delete_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='total_count',
            field=models.IntegerField(blank=True, default='1'),
        ),
    ]
