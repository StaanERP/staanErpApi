# Generated by Django 4.2.2 on 2024-02-13 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EnquriFromapi', '0001_initial'),
        ('itemmaster', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesorder',
            name='marketingEvent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='EnquriFromapi.conferencedata'),
        ),
    ]
