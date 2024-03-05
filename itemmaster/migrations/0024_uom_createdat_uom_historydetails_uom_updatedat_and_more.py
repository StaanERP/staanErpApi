# Generated by Django 4.2.2 on 2024-02-23 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itemmaster', '0023_routing_bom'),
    ]

    operations = [
        migrations.AddField(
            model_name='uom',
            name='CreatedAt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uom',
            name='HistoryDetails',
            field=models.ManyToManyField(blank=True, to='itemmaster.itemmasterhistory'),
        ),
        migrations.AddField(
            model_name='uom',
            name='UpdatedAt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='uom',
            name='createdby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='createUOM', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='uom',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='uom',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ModifiedUOM', to=settings.AUTH_USER_MODEL),
        ),
    ]