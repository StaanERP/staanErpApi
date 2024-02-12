# Generated by Django 4.2.2 on 2024-02-10 06:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('itemmaster', '0003_teststaantable_salary_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesorder',
            name='POS_ID',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.CreateModel(
            name='ItemMasterHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Action', models.CharField(choices=[('Add', 'Add'), ('Delete', 'Delete'), ('Update', 'Update')], max_length=10)),
                ('ModelName', models.CharField(max_length=50)),
                ('ModelId', models.IntegerField()),
                ('ColumnName', models.CharField(max_length=250)),
                ('PreviousState', models.CharField(max_length=250)),
                ('UpdatedState', models.CharField(max_length=250)),
                ('modifiedDate', models.DateTimeField(auto_now_add=True)),
                ('SavedBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
