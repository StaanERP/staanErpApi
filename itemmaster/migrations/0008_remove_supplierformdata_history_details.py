# Generated by Django 4.2.2 on 2024-03-12 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itemmaster', '0007_alternate_unit_created_at_alternate_unit_created_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supplierformdata',
            name='history_details',
        ),
    ]