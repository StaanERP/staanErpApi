import graphene
from graphene import ObjectType, List, Int
from graphene_django.types import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from django.core.paginator import Paginator
from graphql_relay import PageInfo
from .serializer import *
from .models import *
from django.contrib.auth.models import User


class ItemMasterType(DjangoObjectType):
    class Meta:
        model = ItemMaster
        fields = "__all__"


class UOMType(DjangoObjectType):
    class Meta:
        model = UOM
        fields = "__all__"


class Item_Groups_NameType(DjangoObjectType):
    class Meta:
        model = Item_Groups_Name  # Corrected from Model to model (case sensitive)
        fields = "__all__"  # This includes all fields from the model


class Alternate_Unit_Type(DjangoObjectType):
    class Meta:
        model = Alternate_unit
        fields = "__all__"


class Category_Type(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"


class Supplier_Form_Data_Type(DjangoObjectType):
    class Meta:
        model = Supplier_Form_Data
        fields = "__all__"


class AccountsMaster_Type(DjangoObjectType):
    class Meta:
        model = AccountsMaster
        fields = "__all__"


class Hsn_Type(DjangoObjectType):
    class Meta:
        model = Hsn
        fields = "__all__"


class Item_Combo_Type(DjangoObjectType):
    class Meta:
        model = Item_Combo
        fields = "__all__"


class User_Type(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"


class PageInfoType(graphene.ObjectType):
    total_items = graphene.Int()
    has_next_page = graphene.Boolean()
    has_previous_page = graphene.Boolean()
    total_pages = graphene.Int()


def create_connection_type_with_items(item_type):
    class ConnectionType(graphene.ObjectType):
        items = graphene.List(item_type)
        page_info = graphene.Field(PageInfoType)

    return ConnectionType


ItemMasterConnection = create_connection_type_with_items(ItemMasterType)


class Query(ObjectType):
    item_master = graphene.Field(
        ItemMasterConnection,
        page=graphene.Int(default_value=1),
        page_size=graphene.Int(default_value=10)
        # partNumber = graphene

    )
    uom = List(UOMType)
    item_groups_name = List(Item_Groups_NameType)
    alternate_unit = List(Alternate_Unit_Type)
    category = List(Category_Type)
    supplier_form_data = List(Supplier_Form_Data_Type)
    accounts_master = List(AccountsMaster_Type)
    hsn = List(Hsn_Type)
    item_combo = List(Item_Combo_Type)
    User = List(User_Type)

    def resolve_item_master(self, info, page=1, page_size=100):
        queryset = ItemMaster.objects.all()
        paginator = Paginator(queryset, page_size)
        paginated_data = paginator.get_page(page)
        # Create PageInfo object
        total_pages = paginator.num_pages
        page_info = PageInfoType(
            total_items=paginator.count,
            has_next_page=paginated_data.has_next(),
            has_previous_page=paginated_data.has_previous(),
            total_pages=total_pages,
        )
        return ItemMasterConnection(items=paginated_data.object_list, page_info=page_info)

    def resolve_uom(self, info):
        return UOM.objects.all()

    def resolve_item_groups_name(self, info):
        return Item_Groups_Name.objects.all()

    def resolve_alternate_unit(self, info):
        return Alternate_unit.objects.all()

    def resolve_category_type(self, info):
        return Category.objects.all()

    def resolve_supplier_form_data(self, info):
        return Supplier_Form_Data.objects.all()

    def resolve_accounts(self, info):
        return AccountsMaster.objects.all()

    def resolve_hsn(self, info):
        return Hsn.objects.all()

    def resolve_item_combo(self, info):
        return Item_Combo.objects.all()

    def resolve_user(self, info):
        return User.objects.all()


schema = graphene.Schema(query=Query,)
