# Generated by Django 4.2.2 on 2024-02-28 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemmaster', '0035_alter_batchnumber_batchnumbername'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='State',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]