# Generated by Django 4.2.2 on 2024-03-12 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemmaster', '0008_remove_supplierformdata_history_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplierformdata',
            name='history_details',
            field=models.ManyToManyField(blank=True, to='itemmaster.itemmasterhistory'),
        ),
    ]
