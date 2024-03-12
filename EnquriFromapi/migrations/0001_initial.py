# Generated by Django 4.2.2 on 2024-03-07 04:55

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Conferencedata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('startDate', models.DateField(blank=True, null=True)),
                ('endDate', models.DateField(blank=True, null=True)),
                ('Status', models.BooleanField(default=True)),
                ('DefaultStore', models.IntegerField(blank=True, null=True)),
                ('Currency', models.IntegerField(blank=True, null=True)),
                ('createdBy', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='created', to=settings.AUTH_USER_MODEL)),
                ('incharge', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='incharge', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='enquiryDatas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('OrganizationName', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=254)),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='customer_profiles/')),
                ('alternateMobileNumber', models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?9?1?\\s?-?\\d{1,}-?\\s?\\d{1,}')])),
                ('status', models.CharField(choices=[('Not Contacted', 'Not Contacted'), ('Converted', 'Converted'), ('Junk', 'Junk'), ('Inprogress', 'Inprogress')], max_length=50)),
                ('MobileNumber', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+91-1234567890' or '091 1234 567890'. Up to 15 digits allowed.", regex='^\\+?9?1?\\s?-?\\d{1,}-?\\s?\\d{1,}')])),
                ('Location', models.CharField(max_length=200)),
                ('message', models.CharField(blank=True, max_length=500)),
                ('Remarks', models.TextField(blank=True, null=True)),
                ('followup', models.DateField(blank=True, null=True)),
                ('Interesteds', models.ManyToManyField(blank=True, to='EnquriFromapi.product')),
                ('conferencedata', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='EnquriFromapi.conferencedata')),
                ('salesPerson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
