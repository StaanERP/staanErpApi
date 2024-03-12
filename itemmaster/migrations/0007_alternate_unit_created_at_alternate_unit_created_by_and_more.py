# Generated by Django 4.2.2 on 2024-03-12 07:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itemmaster', '0006_remove_alternate_unit_created_at_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alternate_unit',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alternate_unit',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='Aucreate', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='alternate_unit',
            name='is_delete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='alternate_unit',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]