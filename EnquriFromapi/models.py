from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser
from importlib import import_module

from itemmaster.models import Store, CurrencyMaster

status_ = (
    ("Not Contacted", "Not Contacted"),
    ("Converted", "Converted"),
    ('Junk', "Junk"),
    ('Inprogress', "Inprogress"),
)


# Create your models here.
class Conferencedata(models.Model):
    Name = models.CharField(max_length=50)
    incharge = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="incharge")
    startDate = models.DateField(null=True, blank=True)
    endDate = models.DateField(null=True, blank=True)
    Status = models.BooleanField(default=True)
    createdBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="created")
    # itemmaster.Store CurrencyMaster
    """due to circular dependency issue we using itemmaster.Store itemmaster.CurrencyMaster as IntegerField  """
    DefaultStore = models.IntegerField(null=True, blank=True)
    Currency = models.IntegerField(null=True, blank=True)
    # DefaultStore = models.ForeignKey("itemmaster.Store", on_delete=models.SET_NULL, null=True, blank=True, swappable=True)
    # Currency = models.ForeignKey("itemmaster.CurrencyMaster" , on_delete=models.SET_NULL, null=True, blank=True, swappable=True)

    def save(self, *args, **kwargs):
        self.Name = self.Name.title()
        super(Conferencedata, self).save(*args, **kwargs)


class product(models.Model):
    Name = models.CharField(max_length=50)

    def __str__(self):
        return self.Name


class enquiryDatas(models.Model):
    Name = models.CharField(max_length=50)
    OrganizationName = models.CharField(max_length=200)
    Email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^\+?9?1?\s?-?\d{1,}-?\s?\d{1,}',
        message="Phone number must be entered in the format: '+91-1234567890' or '091 1234 567890'. Up to 15 digits "
                "allowed."
    )
    profile_image = models.ImageField(upload_to='customer_profiles/', null=True, blank=True)
    alternateMobileNumber = models.CharField(
        max_length=15,
        validators=[
            RegexValidator(
                regex=r'^\+?9?1?\s?-?\d{1,}-?\s?\d{1,}',
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
            )
        ],
        null=True,
        blank=True
    )
    status = models.CharField(max_length=50, choices=status_)
    MobileNumber = models.CharField(validators=[phone_regex], max_length=17)
    Location = models.CharField(max_length=200)
    message = models.CharField(max_length=500, blank=True)
    Interesteds = models.ManyToManyField(product, blank=True)
    conferencedata = models.ForeignKey(Conferencedata, on_delete=models.SET_NULL, null=True, blank=True)
    salesPerson = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    Remarks = models.TextField(null=True, blank=True)
    followup = models.DateField(null=True, blank=True)

    def __str__(self):
        return "Name: """ + self.Name + " , " + "Organization :" + self.OrganizationName
