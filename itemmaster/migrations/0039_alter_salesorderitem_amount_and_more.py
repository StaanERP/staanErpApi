# Generated by Django 4.2.2 on 2024-02-29 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemmaster', '0038_alter_salesorder_payment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorderitem',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='salesorderitem',
            name='rate',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
