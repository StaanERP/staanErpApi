# Generated by Django 4.2.2 on 2024-02-20 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itemmaster', '0005_remove_itemmasterhistory_columnname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemmasterhistory',
            name='ColumnName',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='itemmasterhistory',
            name='PreviousState',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]