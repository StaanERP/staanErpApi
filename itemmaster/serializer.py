from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.authtoken.views import Token
from rest_framework.response import Response


class EditListViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = EditListView
        fields = "__all__"


class HsnSerializer(serializers.ModelSerializer):
    gst_rate = serializers.ChoiceField(choices=gst_rate, required=False, allow_null=True)

    class Meta:
        model = Hsn
        fields = "__all__"


class ItemGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Groups_Name
        fields = "__all__"


class UOMSerializer(serializers.ModelSerializer):
    class Meta:
        model = UOM
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class AccountsGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountsGroup
        fields = "__all__"


class AccountsMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountsMaster
        fields = "__all__"


class Alternate_unitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alternate_unit
        fields = "__all__"


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = "__all__"

class BatchNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatchNumber
        fields = "__all__"

class StockSerialHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = StockSerialHistory
        fields = "__all__"

class StockHistoryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockHistoryLog
        fields = "__all__"


class ItemMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemMaster
        fields = "__all__"


class SerialNumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = SerialNumbers
        fields = "__all__"


class ItemStockSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemStock
        fields = "__all__"


class ItemInventoryApprovalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemInventoryApproval
        fields = "__all__"

class InventoryHandlerSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryHandler
        fields = "__all__"

class ItemComboSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item_Combo
        fields = "__all__"


class CustomerGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerGroups
        fields = "__all__"


class SupplierGroupsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierGroups
        fields = "__all__"


class ItemContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = contact_detalis
        fields = "__all__"


class ItemAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = company_address
        fields = "__all__"


class ItemSupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier_Form_Data
        fields = "__all__"

    # def validate_Legal_Name(self, value):
    #     """
    #     Validate that Legal_Name is unique.
    #     """
    #     existing_supplier = Supplier_Form_Data.objects.filter(Legal_Name=value).first()
    #
    #     if existing_supplier:
    #         raise serializers.ValidationError("Legal_Name must be unique.")
    #
    #     return value


class CurrencyMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyMaster
        fields = "__all__"


class CurrencyExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyExchange
        fields = "__all__"


class SalesOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrderItem
        fields = "__all__"


class SalesOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesOrder
        fields = "__all__"

class testStaanTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = testStaanTable
        fields = "__all__"

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["id", "username", "password"]
#         extra_kwargs = {
#             'password': {
#                 'write_only': True,
#                 'required': True
#             }
#         }

# def create(self, validated_data):
#     username = validated_data.get('username')
#     password = validated_data.get('password')
#
#     # Check if a user with the provided username already exists
#     existing_user = User.objects.filter(username=username).first()
#     if existing_user:
#         # If the user exists, return the existing user's token
#         token, created = Token.objects.get_or_create(user=existing_user)
#         return Response({'token': token.key})
#
#     # If the user doesn't exist, create a new user and return the token
#     user = User.objects.create_user(username=username, password=password)
#     token = Token.objects.create(user=user)
#
#     return Response({'token': token.key})
