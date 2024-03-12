import graphene
from django.db.models import ProtectedError

from itemmaster.schema import *
from itemmaster.models import *
from itemmaster.serializer import *


class ItemMasterCreateMutation(graphene.Mutation):
    """ItemMaster Create and update"""

    class Arguments:
        id = graphene.ID()
        item_part_code = graphene.String()
        item_name = graphene.String()
        description = graphene.String()
        item_types = graphene.Int()
        item_uom = graphene.Int()
        item_group = graphene.Int()
        alternate_uom_ids = graphene.List(graphene.Int)
        item_indicators = graphene.Int()
        category = graphene.Int()
        supplier_data = graphene.Int()
        purchase_uom = graphene.Int()
        item_cost = graphene.Int()
        item_safe_stock = graphene.Int()
        item_order_qty = graphene.Int()
        item_lead_time = graphene.Int()
        total_stock = graphene.Decimal()
        rejected_stock = graphene.Decimal()
        item_mrp = graphene.Decimal()
        item_min_price = graphene.Decimal()
        item_sales_account = graphene.Int()
        item_purchase_account = graphene.Int()
        item_hsn = graphene.Int()
        keep_stock = graphene.Boolean()
        sell_on_mrp = graphene.Boolean()
        serial = graphene.Boolean()
        serial_auto_gentrate = graphene.Boolean()
        serial_format = graphene.String()
        serial_starting = graphene.Int()
        batch_number = graphene.Boolean()
        service = graphene.Boolean()
        item_warranty_based = graphene.String()
        item_installation = graphene.Boolean()
        invoice_date = graphene.Date()
        installation_data = graphene.Date()
        item_combo_bool = graphene.Boolean()
        item_combo_data = graphene.List(graphene.Int)
        item_barcode = graphene.Boolean()
        item_active = graphene.Boolean()
        item_qc = graphene.Boolean()
        modified_by = graphene.Int()
        created_by = graphene.Int()
        is_delete = graphene.Boolean()
        created_at = graphene.Date()
        updated_at = graphene.Date()

    item_master = graphene.Field(ItemMasterType)
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    def mutate(self, info, **kwargs):
        serializer = ''
        item_master_instance = None
        success = False
        errors = []
        print(item_master_instance)
        if 'id' in kwargs:
            # Update operation
            item_master_instance = ItemMaster.objects.filter(id=kwargs['id']).first()
            if not item_master_instance:
                errors.append("Item Master not found.")
            else:
                serializer = ItemMasterSerializer(item_master_instance, data=kwargs, partial=True)
        else:
            serializer = ItemMasterSerializer(data=kwargs)
            print(serializer.is_valid())
            print(serializer.errors)
        if serializer.is_valid():
            serializer.save()
            item_master_instance = serializer.instance
            success = True

        else:
            print(serializer.errors)
            errors = [f"{field}: {'; '.join([str(e) for e in error])}" for field, error in serializer.errors.items()]
        return ItemMasterCreateMutation(item_master=item_master_instance, success=success, errors=errors)


class ItemMasterDeleteMutation(graphene.Mutation):
    """ItemMaster Delete"""

    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    def mutate(self, info, id):
        success = False
        errors = []
        print(id)
        try:
            item_master_instance = ItemMaster.objects.get(pk=id)
            item_master_instance.delete()
            success = True
        except ProtectedError as e:
            errors.append('This data Linked with other modules')
        except Exception as e:
            errors.append(str(e))
        return ItemMasterDeleteMutation(success=success, errors=errors)


class ItemGroupsNameCreateMutation(graphene.Mutation):
    """ItemGroupsName Create and update"""

    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        parent_group = graphene.Int()
        hsn = graphene.Int()
        modified_by = graphene.Int()
        created_by = graphene.Int()

    Item_groups_name = graphene.Field(ItemGroupsNameType)
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    def mutate(self, info, **kwargs):
        serializer = ''
        item_groups_name = None
        success = False
        errors = []
        print(kwargs)
        if 'id' in kwargs:
            # Update operation
            item_groups_name_instance = Item_Groups_Name.objects.filter(id=kwargs['id']).first()
            if not item_groups_name_instance:
                errors.append("item groups not found.")
            else:
                serializer = ItemGroupSerializer(item_groups_name_instance, data=kwargs, partial=True)
        else:
            serializer = ItemGroupSerializer(data=kwargs)

        if serializer.is_valid():
            serializer.save()
            item_groups_name = serializer.instance
            success = True

        else:
            errors = [f"{field}: {'; '.join([str(e) for e in error])}" for field, error in serializer.errors.items()]
        return ItemGroupsNameCreateMutation(Item_groups_name=item_groups_name, success=success, errors=errors)


class ItemGroupNameDeleteMutation(graphene.Mutation):
    """ItemGroupName Delete"""

    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    def mutate(self, info, id):
        success = False
        errors = []
        try:
            item_groups_name_instance = Item_Groups_Name.objects.get(pk=id)
            item_groups_name_instance.delete()
            success = True
        except ProtectedError as e:
            errors.append('This data Linked with other modules')
        except Exception as e:
            errors.append(str(e))
        return ItemGroupNameDeleteMutation(success=success, errors=errors)


class UomCreateMutation(graphene.Mutation):
    """Uom Create and update"""

    class Arguments:
        id = graphene.ID()
        name = graphene.String()
        e_way_bill_uom = graphene.String()
        description = graphene.String()
        modified_by = graphene.Int()
        created_by = graphene.Int()

    Uom = graphene.Field(UOMType)
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    def mutate(self, info, **kwargs):
        serializer = ''
        uom = None
        success = False
        errors = []
        if 'id' in kwargs:
            # Update operation
            uom_instance = UOM.objects.filter(id=kwargs['id']).first()
            if not uom_instance:
                errors.append("Uom not found.")
            else:
                serializer = UOMSerializer(uom_instance, data=kwargs, partial=True)
        else:
            serializer = UOMSerializer(data=kwargs)

        if serializer.is_valid():
            serializer.save()
            uom = serializer.instance
            success = True

        else:
            errors = [f"{field}: {'; '.join([str(e) for e in error])}" for field, error in serializer.errors.items()]
        return UomCreateMutation(Uom=uom, success=success, errors=errors)


class UomDeleteMutation(graphene.Mutation):
    """uom Delete"""

    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    def mutate(self, info, id):
        success = False
        errors = []
        try:
            uom_instance = UOM.objects.get(pk=id)
            uom_instance.delete()
            success = True
        except ProtectedError as e:
            errors.append('This data Linked with other modules')
        except Exception as e:
            errors.append(str(e))
        return UomDeleteMutation(success=success, errors=errors)


class HsnCreateMutation(graphene.Mutation):
    """hsn Create and update"""

    class Arguments:
        id = graphene.ID()
        hsn_types = graphene.Int()
        hsn_code = graphene.Int()
        description = graphene.String()
        cess_rate = graphene.Int()
        rcm = graphene.Boolean()
        itc = graphene.Boolean()
        gst_rates = graphene.Int()
        modified_by = graphene.Int()
        created_by = graphene.Int()

    hsn = graphene.Field(Hsn_Type)
    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    def mutate(self, info, **kwargs):
        serializer = ''
        hsn = None
        success = False
        errors = []
        if 'id' in kwargs:
            # Update operation
            hsn_instance = Hsn.objects.filter(id=kwargs['id']).first()
            if not hsn_instance:
                errors.append("HSN not found.")
            else:
                serializer = HsnSerializer(hsn_instance, data=kwargs, partial=True)
        else:
            serializer = HsnSerializer(data=kwargs)

        if serializer.is_valid():
            serializer.save()
            hsn = serializer.instance
            success = True

        else:
            errors = [f"{field}: {'; '.join([str(e) for e in error])}" for field, error in serializer.errors.items()]
        return HsnCreateMutation(hsn=hsn, success=success, errors=errors)


class HsnDeleteMutation(graphene.Mutation):
    """hsn Delete"""

    class Arguments:
        id = graphene.ID(required=True)

    success = graphene.Boolean()
    errors = graphene.List(graphene.String)

    def mutate(self, info, id):
        success = False
        errors = []
        try:
            hsn_instance = Hsn.objects.get(pk=id)
            hsn_instance.delete()
            success = True
        except ProtectedError as e:
            errors.append('This data Linked with other modules')
        except Exception as e:
            errors.append(str(e))
        return HsnDeleteMutation(success=success, errors=errors)

# class AccountsMasterCreateMutation(graphene.Mutation):
#     """hsn Create and update"""
#
#     class Arguments:
#         id = graphene.ID()
#         accounts_name = graphene.String()
#         accounts_group_name = graphene.Int()
#         account_type = graphene.String()
#         accounts_active = graphene.Boolean()
#         gst_applicable = graphene.Boolean()
#         itc = graphene.Boolean()
#         gst_rates = graphene.Int()
#         modified_by = graphene.Int()
#         created_by = graphene.Int()
#
#     hsn = graphene.Field(Hsn_Type)
#     success = graphene.Boolean()
#     errors = graphene.List(graphene.String)
#
#     def mutate(self, info, **kwargs):
#         serializer = ''
#         hsn = None
#         success = False
#         errors = []
#         if 'id' in kwargs:
#             # Update operation
#             hsn_instance = Hsn.objects.filter(id=kwargs['id']).first()
#             if not hsn_instance:
#                 errors.append("HSN not found.")
#             else:
#                 serializer = HsnSerializer(hsn_instance, data=kwargs, partial=True)
#         else:
#             serializer = HsnSerializer(data=kwargs)
#
#         if serializer.is_valid():
#             serializer.save()
#             hsn = serializer.instance
#             success = True
#
#         else:
#             errors = [f"{field}: {'; '.join([str(e) for e in error])}" for field, error in serializer.errors.items()]
#         return HsnCreateMutation(hsn=hsn, success=success, errors=errors)
class Mutation(graphene.ObjectType):
    item_master_create_mutation = ItemMasterCreateMutation.Field()
    item_master_delete_mutation = ItemMasterDeleteMutation.Field()
    item_groups_name_create_mutation = ItemGroupsNameCreateMutation.Field()
    item_group_name_delete_mutation = ItemGroupNameDeleteMutation.Field()
    uom_create_mutation = UomCreateMutation.Field()
    uom_delete_mutation = UomDeleteMutation.Field()
    hsn_create_mutation = HsnCreateMutation.Field()
    hsn_delete_mutation = HsnDeleteMutation.Field()