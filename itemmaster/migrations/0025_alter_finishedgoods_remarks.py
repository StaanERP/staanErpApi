# Generated by Django 4.2.2 on 2024-02-24 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemmaster', '0024_uom_createdat_uom_historydetails_uom_updatedat_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finishedgoods',
            name='Remarks',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
