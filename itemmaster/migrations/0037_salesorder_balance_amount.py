# Generated by Django 4.2.2 on 2024-02-29 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemmaster', '0036_salesorder_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='balance_Amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
