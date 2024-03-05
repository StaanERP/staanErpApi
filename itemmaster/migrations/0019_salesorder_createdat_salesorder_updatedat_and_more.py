# Generated by Django 4.2.2 on 2024-02-22 07:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itemmaster', '0018_remove_salesorder_payment_salesorder_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='CreatedAt',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='salesorder',
            name='UpdatedAt',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='createdby',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='createpos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='salesorder',
            name='modified_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='modifiedpos', to=settings.AUTH_USER_MODEL),
        ),
    ]
