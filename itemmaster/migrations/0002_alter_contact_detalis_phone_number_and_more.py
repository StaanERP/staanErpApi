# Generated by Django 4.2.2 on 2024-02-05 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemmaster', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_detalis',
            name='Phone_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='contact_detalis',
            name='WhatsappNo',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
