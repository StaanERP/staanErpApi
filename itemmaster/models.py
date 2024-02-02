from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.exceptions import ValidationError
from EnquriFromapi.models import *
from django.db import transaction

item_types = (("Product", "Product"),
              ("Service", "Service"))
Item_Indicators = (("Buyer", "Buyer"),
                   ("seller", "seller"),
                   ('both', 'both'))
hsn_types = (("HSN", "HSN"),
             ("SAC", "SAC"))
e_way_bill = (("BAGS", "BAGS"),
              ("BALE", "BALE"),
              ("BUNDLES", "BUNDLES"),
              ("BUCKLES", "BUCKLES "),
              ("BILLION OF UNITS", "BILLION OF UNITS"),
              ("BOX", "BOX"),
              ("BOTTLES", "BOTTLES"),
              ("BUNCHES", "BUNCHES"),
              ("CANS", "CANS"),
              ("CUBIC METERS", "CUBIC METERS"),
              ("CUBIC CENTIMETERS", "CUBIC CENTIMETERS"),
              ("CENTIMETERS", "CENTIMETERS"),
              ("CARTONS", "CARTONS"),
              ("DOZENS", "DOZENS"),
              ("DRUMS", "DRUMS"),
              ("GREAT GROSS", "GREAT GROSS"),
              ("GRAMMES", "GRAMMES"),
              ("GROSS", "GROSS"),
              ("GROSS YARDS", "GROSS YARDS"),
              ("KILOGRAMS", "KILOGRAMS"),
              ("KILOLITRE", "KILOLITRE"),
              ("KILOMETRE", "KILOMETRE"),
              ("LITRES", "LITRES"),
              ("MILILITRE", "MILILITRE"),
              ("METERS", "METERS"),
              ("METRIC TON", "METRIC TON"),
              ("NUMBERS", "NUMBERS"),
              ("OTHERS", "OTHERS"),
              ("PACKS", "PACKS"),
              ("PIECES", "PIECES"),
              ("PAIRS", "PAIRS"),
              ("QUINTAL", "QUINTAL"),
              ("ROLLS", "ROLLS"),
              ("SETS", "SETS"),
              ("SQUARE FEET", "SQUARE FEET"),
              ("SQUARE METERS", "SQUARE METERS"),
              ("SQUARE YARDS", "SQUARE YARDS"),
              ("TABLETS", "TABLETS"),
              ("TEN GROSS", "TEN GROSS"),
              ("THOUSANDS", "THOUSANDS"),
              ("TONNES", "TONNES"),
              ("TUBES", "TUBES"),
              ("US GALLONS", "US GALLONS"),
              ("UNITS", "UNITS"),
              ("YARDS", "YARDS"))
gst_rate = ((5, 5),
            (12, 12),
            (18, 18),
            (28, 28),)

Action = (("Add", 'Add'),
          ("Delete", 'Delete'),
          ("Update", 'Update'))

Accountsgroup_Type = (("Asset", "Asset"),
                      ("Income", "Income"),
                      ("Liabilities", "Liabilities"),
                      ("Expenses", "Expenses"))

Accounts_Type = (("Bank", "Bank"),
                 ("Tax", "Tax"),
                 ("Cash", "Cash"))

address_types = (('Billing Address', "Billing Address"),
                 ('Shiping Address', 'Shiping Address'),
                 ('Others', 'Others'))
Item_Warranty_base_on = (("Invoice date", "Invoice date"),
                         ('Installation date', 'installation date'))
visibleTo_ = (("Myself", "Myself"),
              ("All User", "All User"),
              ("Select Users", "Select Users"),
              )
salutation = (('Mr', 'Mr'),
              ('Ms', 'Ms'),
              ('Mrs', 'Mrs'),
              ('Dr', 'Dr'))
gst_type = (('REGULAR', 'REGULAR'),
            ('UNREGISTERED/CONSUMER', 'UNREGISTERED/CONSUMER'),
            ('COMPOSITION', 'COMPOSITION'),
            ('GOVERNMENT ENTITY/TDS', 'GOVERNMENT ENTITY/TDS'),
            ('REGULAR-SEZ', 'REGULAR-SEZ'),
            ('REGULAR-DEEMED EXPORTER', 'REGULAR-DEEMED EXPORTER'),
            ('REGULAR-EXPORTS (EOU)', 'REGULAR-EXPORTS (EOU)'))

tcs = (('Sales', 'Sales'),
       ('Purchase', 'Purchase'),
       ('Both', 'Both'))
currencyFormate = (
    ('0,00,00,00', '0,00,00,00'),
    ('000,000,000', '000,000,000'))
Postypes_ = (('Sample', 'Sample'),
             ('Sales', 'Sales'))


class EditListView(models.Model):
    viewName = models.CharField(max_length=50)
    visibleTo = models.CharField(max_length=20, choices=visibleTo_, default=1)
    visibleTouser = models.ManyToManyField(User, blank=True)
    filiterConditions = models.JSONField(null=True, blank=True)
    ColoumnToDisplay = models.JSONField(null=True, blank=True)
    isDefault = models.BooleanField(default=True)
    Table = models.CharField(max_length=50)
    createdDate = models.DateField(auto_now_add=True)
    createdby = models.ForeignKey(User, related_name="createter", on_delete=models.CASCADE)


class Hsn(models.Model):
    hsn_type = models.CharField(max_length=5, choices=hsn_types, default=1)
    hsn_code = models.IntegerField(unique=True)
    Description = models.TextField(max_length=200)
    gst_rate = models.IntegerField(choices=gst_rate, null=True, blank=True)
    cess_rate = models.IntegerField(null=True, blank=True, )
    created_at = models.DateField(auto_now_add=True)
    rcm = models.BooleanField(default=0)
    itc = models.BooleanField(default=1)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


class Item_Groups_Name(models.Model):
    name = models.CharField(max_length=100)
    Parent_Group = models.CharField(max_length=100, null=True, blank=True)
    hsn = models.ForeignKey(Hsn, null=True, blank=True, on_delete=models.SET_NULL)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):
        self.name = self.name.title()
        if Item_Groups_Name.objects.exclude(pk=self.pk).filter(name=self.name).exists():
            raise ValidationError("Name must be unique.")
        super(Item_Groups_Name, self).save(*args, **kwargs)


class UOM(models.Model):
    name = models.CharField(max_length=255)
    e_way_bill_uom = models.CharField(choices=e_way_bill, max_length=50, null=True, blank=True)
    Description = models.TextField(max_length=300, null=True, blank=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        unique_together = ('name',)

    def save(self, *args, **kwargs):
        self.name = self.name.lower()
        if UOM.objects.exclude(pk=self.pk).filter(name=self.name).exists():
            raise ValidationError("Name must be unique.")

            # Save the object after performing necessary operations
        super(UOM, self).save(*args, **kwargs)
        return self


class Category(models.Model):
    name = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.lower()

        # Check if a record with the same normalized name already exists
        if Category.objects.exclude(pk=self.pk).filter(name=self.name).exists():
            raise ValidationError("Name must be unique.")

        # Save the object after performing necessary operations
        super(Category, self).save(*args, **kwargs)

        return self


class AccountsGroup(models.Model):
    Accounts_Group_Name = models.CharField(unique=True, max_length=50)
    Accounts_Type = models.CharField(choices=Accountsgroup_Type, max_length=20)
    Group_Active = models.BooleanField(default=True)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.Accounts_Group_Name

    def save(self, *args, **kwargs):
        self.Accounts_Group_Name = self.Accounts_Group_Name.lower()

        # Check if a record with the same normalized name already exists
        if AccountsGroup.objects.exclude(pk=self.pk).filter(Accounts_Group_Name=self.Accounts_Group_Name).exists():
            raise ValidationError("Accounts_Group_Name must be unique.")

        # Save the object after performing necessary operations
        super(AccountsGroup, self).save(*args, **kwargs)

        return self


class AccountsMaster(models.Model):
    Accounts_Name = models.CharField(unique=True, max_length=50, )
    Accounts_Group_Name = models.ForeignKey(AccountsGroup, null=True, blank=True, on_delete=models.CASCADE)
    AccountType = models.CharField(choices=Accounts_Type, max_length=20)
    Accounts_Active = models.BooleanField(default=True)
    GST_Applicable = models.BooleanField(default=False)
    TDS = models.BooleanField(default=False)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.Accounts_Name

    def save(self, *args, **kwargs):
        self.Accounts_Name = self.Accounts_Name.title()

        # Check if a record with the same normalized name already exists
        if AccountsMaster.objects.exclude(pk=self.pk).filter(Accounts_Name=self.Accounts_Name).exists():
            raise ValidationError("Accounts Name must be unique.")

        # Save the object after performing necessary operations
        super(AccountsMaster, self).save(*args, **kwargs)

        return self


class Alternate_unit(models.Model):
    addtional_unit = models.ForeignKey(UOM, on_delete=models.CASCADE)
    conversion_Factor = models.DecimalField(max_digits=10, decimal_places=3)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.addtional_unit)


class Store(models.Model):
    StoreName = models.CharField(max_length=100)
    StoreAccount = models.ForeignKey(AccountsMaster, null=True, blank=True, on_delete=models.CASCADE)
    StoreInCharge = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    matained = models.BooleanField(default=True)
    Action = models.BooleanField(default=True)

    def __str__(self):
        return self.StoreName


"""Item combo"""


class display_group(models.Model):
    display = models.CharField(max_length=100)

    def __str__(self):
        return self.display


class Item_Combo(models.Model):
    part_number = models.ForeignKey('ItemMaster', on_delete=models.CASCADE)
    Item_Qty = models.DecimalField(max_digits=10, decimal_places=3)
    item_display = models.ForeignKey(display_group, on_delete=models.CASCADE, null=True, blank=True)
    Is_Mandatory = models.BooleanField(default=True)
    Savedby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    createdat = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.part_number.Item_name


''' Supplier Form Data'''


class CustomerGroups(models.Model):
    name = models.CharField(max_length=50, unique=True)
    parent_group = models.CharField(max_length=50, null=True, blank=True)
    Active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    Saved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        self.name = self.name.title()

        # Check if a record with the same normalized name already exists
        if CustomerGroups.objects.exclude(pk=self.pk).filter(name=self.name).exists():
            raise ValidationError("Name must be unique.")

        # Save the object after performing necessary operations
        super(CustomerGroups, self).save(*args, **kwargs)

        return self


class SupplierGroups(models.Model):
    name = models.CharField(max_length=50, unique=True)
    parent_group = models.CharField(max_length=50, null=True, blank=True)
    Active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    Saved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name = self.name.title()

        # Check if a record with the same normalized name already exists
        if SupplierGroups.objects.exclude(pk=self.pk).filter(name=self.name).exists():
            raise ValidationError("Name must be unique.")

        # Save the object after performing necessary operations
        super(SupplierGroups, self).save(*args, **kwargs)

        return self


class contact_detalis(models.Model):
    Contact_Person_Name = models.CharField(max_length=100)
    Salutation = models.CharField(choices=salutation, max_length=10)
    Email = models.EmailField(null=True, blank=True)
    Phone_number = models.IntegerField()
    Default = models.BooleanField(default=False)
    WhatsappNo = models.IntegerField(null=True, blank=True)
    OtherNo = models.IntegerField(null=True, blank=True)


class company_address(models.Model):
    address_type = models.CharField(choices=address_types, max_length=30, null=True, blank=True)
    Address_Line_1 = models.CharField(max_length=100)
    Address_Line_2 = models.CharField(max_length=100, null=True, blank=True)
    City = models.CharField(max_length=100)
    pincode = models.IntegerField()
    State = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
    Default = models.BooleanField(default=False)

    def __str__(self):
        return str(self.address_type) + str(self.Address_Line_1)


class Supplier_Form_Data(models.Model):
    Company_Name = models.CharField(max_length=100, unique=True)
    Legal_Name = models.CharField(max_length=100, )
    Customer = models.BooleanField()
    Supplier = models.BooleanField()
    Transporter = models.BooleanField()
    TransporterId = models.CharField(max_length=100, null=True, blank=True)
    GSTIN_Type = models.CharField(choices=gst_type, max_length=50)
    GSTIN = models.CharField(max_length=15, unique=True)
    TCS = models.CharField(choices=tcs, max_length=10)
    Pan_no = models.CharField(max_length=100, unique=True)
    contact = models.ManyToManyField(contact_detalis)
    address = models.ManyToManyField(company_address)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, )
    Saved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    """customer"""
    customer_group = models.ForeignKey(CustomerGroups, on_delete=models.SET_NULL, null=True, blank=True)
    sales_person = models.CharField(max_length=100, null=True, blank=True)
    customer_credited_period = models.IntegerField(null=True, blank=True)
    credited_limit = models.IntegerField(null=True, blank=True)

    """Supplier"""
    supplier_group = models.ForeignKey(SupplierGroups, on_delete=models.CASCADE, null=True, blank=True)
    supplier_credited_period = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.Company_Name

    def save(self, *args, **kwargs):
        self.Company_Name = self.Company_Name.title()

        # self.TransporterId = self.TransporterId.title()  # This is where the error occurs
        self.GSTIN = self.GSTIN.title()
        self.Pan_no = self.Pan_no.title()
        if self.TransporterId != "":
            if Supplier_Form_Data.objects.exclude(pk=self.pk).filter(TransporterId=self.TransporterId).exists():
                raise ValidationError("Transporter Id must be unique.")
        if Supplier_Form_Data.objects.exclude(pk=self.pk).filter(Company_Name=self.Company_Name).exists():
            raise ValidationError("Company Name must be unique.")

        super(Supplier_Form_Data, self).save(*args, **kwargs)
        return self


class ItemMaster(models.Model):
    Item_PartCode = models.CharField(unique=True, max_length=40)
    Item_name = models.CharField(unique=True, max_length=100)
    Description = models.TextField(max_length=300, null=True, blank=True)
    Item_type = models.CharField(choices=item_types, null=True, blank=True, max_length=10)
    Item_UOM = models.ForeignKey(UOM, related_name="unit", on_delete=models.CASCADE, null=True, blank=True)

    Item_Group = models.ForeignKey(Item_Groups_Name, null=True, related_name="group", blank=True,
                                   on_delete=models.CASCADE)
    Alternate_uom = models.ManyToManyField(Alternate_unit, blank=True)
    Item_Indicator = models.CharField(choices=Item_Indicators, max_length=10, null=True, blank=True)
    category = models.ForeignKey(Category, related_name="Category", on_delete=models.CASCADE, null=True, blank=True)
    supplierData = models.ForeignKey(Supplier_Form_Data, on_delete=models.CASCADE, null=True, blank=True)
    '''Purchase'''
    Purchase_uom = models.ForeignKey(UOM, related_name="uom", on_delete=models.CASCADE, null=True, blank=True)
    Item_Cost = models.IntegerField(null=True, blank=True)
    Item_Safe_Stock = models.IntegerField(null=True, blank=True)
    Item_Order_Qty = models.IntegerField(null=True, blank=True)
    Item_Leadtime = models.IntegerField(null=True, blank=True)
    '''sell'''
    Item_Mrp = models.FloatField(null=True, blank=True)
    Item_min_price = models.FloatField(null=True, blank=True)
    Item_Sales_Account = models.ForeignKey(AccountsMaster, related_name="Accounts_Master_Sales_Account",
                                           on_delete=models.CASCADE, null=True, blank=True)
    Item_Purchase_Account = models.ForeignKey(AccountsMaster, related_name="Accounts_Master_Purchase_Account",
                                              on_delete=models.CASCADE, null=True, blank=True)
    Item_HSN = models.ForeignKey(Hsn, on_delete=models.CASCADE, null=True, blank=True)
    Keep_stock = models.BooleanField(default=0)
    '''serial number'''
    serial = models.BooleanField(default=0)
    serial_auto_gentrate = models.BooleanField(default=False)
    Serial_format = models.CharField(max_length=30, null=True, blank=True)
    Serial_starting = models.IntegerField(null=True, blank=True)

    '''batch number'''
    Batch_number = models.BooleanField(default=False)

    '''Service'''
    Service = models.BooleanField(default=False)
    Item_Warranty_based = models.CharField(choices=Item_Warranty_base_on, null=True, blank=True, max_length=20)
    Item_Installation = models.BooleanField(default=False)
    Invoicedate = models.DateField(null=True, blank=True)
    installation_data = models.DateField(null=True, blank=True)

    Item_Combo_bool = models.BooleanField(default=False)
    Item_Combo_data = models.ManyToManyField(Item_Combo, blank=True)
    Item_Barcode = models.BooleanField(default=False)
    Item_Active = models.BooleanField(default=True)
    item_qc = models.BooleanField(default=False)
    modified_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def save(self, *args, **kwargs):

        self.Item_PartCode = self.Item_PartCode.title()

        # Check if a record with the same normalized name already exists
        if ItemMaster.objects.exclude(pk=self.pk).filter(Item_PartCode=self.Item_PartCode).exists():
            raise ValidationError("PartCode must be unique.")

        self.Item_name = self.Item_name.title()

        # Check if a record with the same normalized name already exists
        if ItemMaster.objects.exclude(pk=self.pk).filter(Item_name=self.Item_name).exists():
            raise ValidationError("Item Name must be unique.")

        # Save the object after performing necessary operations
        super(ItemMaster, self).save(*args, **kwargs)

        return self

    def __str__(self):
        return self.Item_PartCode


class SerialNumbers(models.Model):
    SerialNumber = models.CharField(max_length=50, unique=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)


class BatchNumber(models.Model):
    part_no = models.ForeignKey(ItemMaster, on_delete=models.CASCADE)
    BatchNumberName = models.CharField(max_length=50, null=True, blank=True, unique=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)


class StockSerialHistory(models.Model):
    part_no = models.ForeignKey(ItemMaster, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, blank=True)
    lastSerialHistory = models.CharField(max_length=50, null=True, blank=True)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)


class ItemStock(models.Model):
    part_no = models.ForeignKey(ItemMaster, on_delete=models.CASCADE)
    currentStock = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    Serialnum = models.ManyToManyField(SerialNumbers, blank=True)
    BatchNumber = models.ForeignKey(BatchNumber, null=True, blank=True, on_delete=models.SET_NULL)
    UOM = models.ForeignKey(UOM, on_delete=models.SET_NULL, null=True, blank=True)
    """only for serialnum to track last serial number"""
    lastSerialHistory = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return str(self.part_no.Item_PartCode)

    def save(self, *args, **kwargs):
        if self.pk is not None:
            # The instance already exists in the database, meaning it's an update
            original_instance = ItemStock.objects.get(pk=self.pk)

            # Compare each field and create a StockHistoryLog for each modified field
            for field in self._meta.fields:
                field_name = field.name
                original_value = getattr(original_instance, field_name)
                new_value = getattr(self, field_name)

                if original_value != new_value:
                    StockHistoryLog.objects.create(
                        Action='Update',
                        StockLink=self,
                        PartNumber=self.part_no,
                        StoreLink=self.store,
                        ColumnName=field_name,
                        PreviousState=str(original_value),
                        UpdatedState=str(new_value),
                        modifiedDate=timezone.now(),
                        SavedBy=kwargs.get('user'),
                    )

            # Save the ItemStock instance before dealing with many-to-many relationships
            super().save(*args, **kwargs)

            # Now that the ItemStock instance is saved, create/update many-to-many relationships
            self.Serialnum.set(self.Serialnum.all())  # Adjust this based on your many-to-many relationships
        else:
            # The instance is new, meaning it's a new row
            super().save(*args, **kwargs)

            if self.currentStock:
                StockHistoryLog.objects.create(
                    Action='Add',
                    StockLink=self,
                    PartNumber=self.part_no,
                    StoreLink=self.store,
                    ColumnName="currentStock",
                    PreviousState=0,  # No previous state for a new row
                    UpdatedState=str(self.currentStock),
                    modifiedDate=timezone.now(),
                    SavedBy=kwargs.get('user'),
                )


class StockHistoryLog(models.Model):
    Action = models.CharField(choices=Action, max_length=10)
    StockLink = models.ForeignKey(ItemStock, on_delete=models.CASCADE)
    StoreLink = models.ForeignKey(Store, on_delete=models.CASCADE, null=True, blank=True)
    PartNumber = models.ForeignKey(ItemMaster, on_delete=models.CASCADE, null=True, blank=True)
    ColumnName = models.CharField(max_length=250)
    PreviousState = models.CharField(max_length=250)
    UpdatedState = models.CharField(max_length=250)
    modifiedDate = models.DateTimeField(max_length=250)
    SavedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


class ItemInventoryApproval(models.Model):
    part_no = models.ForeignKey(ItemMaster, on_delete=models.CASCADE)
    qty = models.CharField(max_length=50)
    Serialnum = models.ManyToManyField(SerialNumbers, blank=True)
    BatchNumber = models.ForeignKey(BatchNumber, on_delete=models.SET_NULL, null=True, blank=True)
    UOM = models.ForeignKey(UOM, on_delete=models.SET_NULL, null=True, blank=True)
    Store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, blank=True)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        if (self.BatchNumber != None):
            return str(self.part_no.Item_PartCode) + "  qty : " + str(self.qty) + "  BatchNumber:  " + str(
                self.BatchNumber) + "  Serialnum: " + str(self.Serialnum)
        else:
            return str(self.part_no.Item_PartCode) + "  qty : " + str(self.qty) + "  BatchNumber:  " + str(
                self.BatchNumber) + "  Serialnum: " + str(self.Serialnum)


class InventoryHandler(models.Model):
    InventoryHandlerId = models.CharField(max_length=20, unique=True, editable=False)
    InventoryId = models.ManyToManyField(ItemInventoryApproval)
    CreatedAt = models.DateTimeField(auto_now_add=True)
    UpdatedAt = models.DateTimeField(auto_now=True)
    SavedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    Store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, blank=True)
    Actions = models.CharField(choices=Action, max_length=10)

    def __str__(self):
        return self.InventoryHandlerId

    def save(self, *args, **kwargs):
        if not self.InventoryHandlerId:
            if self.Actions == 'Add':
                iaa_instances = InventoryHandler.objects.filter(InventoryHandlerId__startswith='IAA').order_by(
                    '-InventoryHandlerId').first()
                last_number = int(iaa_instances.InventoryHandlerId.split('-')[1]) if iaa_instances else 0
                new_number = last_number + 1
                self.InventoryHandlerId = f'IAA-{new_number:03d}'

            elif self.Actions == 'Delete':
                iad_instances = InventoryHandler.objects.filter(InventoryHandlerId__startswith='IAD').order_by(
                    '-InventoryHandlerId').first()
                last_number = int(iad_instances.InventoryHandlerId.split('-')[1]) if iad_instances else 0
                new_number = last_number + 1
                self.InventoryHandlerId = f'IAD-{new_number:03d}'

        # Call super().save outside the if conditions
        super().save(*args, **kwargs)


class CurrencyMaster(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    Currency_symbol = models.CharField(max_length=5)
    Formate = models.CharField(choices=currencyFormate, max_length=50)
    Active = models.BooleanField(default=True)
    createdAt = models.DateField(auto_now=True)
    SavedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.Name

    def save(self, *args, **kwargs):
        self.Name = self.Name.title()
        super(CurrencyMaster, self).save(*args, **kwargs)

        return self


class CurrencyExchange(models.Model):
    Name = models.CharField(max_length=50, unique=True)
    rate = models.DecimalField(max_digits=10, decimal_places=3)
    Date = models.DateField(auto_now=True)
    SavedBy = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.Name

    def save(self, *args, **kwargs):
        self.Name = self.Name.title()
        super(CurrencyExchange, self).save(*args, **kwargs)

        return self


class SalesOrderItem(models.Model):
    partCode = models.ForeignKey(ItemMaster, on_delete=models.SET_NULL, null=True)
    Description = models.CharField(max_length=500, null=True, blank=True)
    uom = models.ForeignKey(UOM, on_delete=models.SET_NULL, null=True)
    qty = models.DecimalField(max_digits=10, decimal_places=3)
    Serial = models.ManyToManyField(SerialNumbers, blank=True)
    Batch = models.ForeignKey(BatchNumber, null=True, blank=True, on_delete=models.SET_NULL)
    # rate = models.DecimalField(max_digits=10, decimal_places=3)

    BatchNo = models.CharField(max_length=50, null=True, blank=True)
    rate = models.DecimalField(max_digits=10, decimal_places=3, )
    amount = models.DecimalField(max_digits=10, decimal_places=3, )
    DiscountPercentage = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    DiscountValue = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    DiscountValueForPerItem = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    FinalValue = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    cretedDate = models.DateField(auto_now=True, editable=False)
    sgst = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    cgst = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    igst = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    createdby = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)


class SalesOrder(models.Model):
    IsPOS = models.BooleanField(default=True)
    posType = models.CharField(choices=Postypes_, max_length=50)
    marketingEvent = models.ForeignKey(Conferencedata, null=True, on_delete=models.SET_NULL)
    OrderDate = models.DateField()
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True)
    # Sample
    Mobile = models.IntegerField(null=True, blank=True)
    WhatsappNumber = models.IntegerField(null=True, blank=True)
    CosName = models.CharField(max_length=100, null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    City = models.CharField(max_length=50, null=True, blank=True)
    Remarks = models.CharField(max_length=200, null=True, blank=True)
    # Sales data
    customerName = models.ForeignKey(Supplier_Form_Data,null=True ,on_delete=models.SET_NULL )
    BillingAddress = models.ForeignKey(company_address,related_name= "BillingAddress",  null=True ,on_delete=models.SET_NULL)
    DeliverAddress = models.ForeignKey(company_address,related_name= "DeliverAddress",  null=True ,on_delete=models.SET_NULL)

    """Billing Details"""
    Currency = models.ForeignKey(CurrencyMaster, null=True, on_delete=models.SET_NULL)
    """Item Details"""
    itemDetails = models.ManyToManyField(SalesOrderItem, blank=True)
    OverallDiscountPercentage = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    OverallDiscountValue = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    DiscountFinalTotal = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    "Total amount"
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    igst = models.JSONField(null=True, blank=True)
    sgst = models.JSONField(null=True, blank=True)
    cgst = models.JSONField(null=True, blank=True)

    # AmountwithTax = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    FinalTotalValue = models.DecimalField(max_digits=10, decimal_places=2)


class testStaanTable(models.Model):
    name = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField()
    Salary = models.IntegerField()
