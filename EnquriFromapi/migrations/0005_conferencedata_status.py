# Generated by Django 4.2.2 on 2023-11-14 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EnquriFromapi', '0004_product_enquirydatas'),
    ]

    operations = [
        migrations.AddField(
            model_name='conferencedata',
            name='Status',
            field=models.BooleanField(default=False),
        ),
    ]
