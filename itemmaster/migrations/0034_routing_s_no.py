# Generated by Django 4.2.2 on 2024-02-27 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemmaster', '0033_remove_currencyexchange_savedby_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='routing',
            name='S_No',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
