# Generated by Django 4.2.2 on 2024-02-22 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itemmaster', '0016_alter_salesorder_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorder',
            name='customerName',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='itemmaster.supplier_form_data'),
        ),
    ]
