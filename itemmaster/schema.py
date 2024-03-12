import graphene
from django.db.models import F
from django.db.models.functions import Lower
from graphene import ObjectType, List, Int
from graphene_django.types import DjangoObjectType
from graphene_django.rest_framework.mutation import SerializerMutation
from django.core.paginator import Paginator
from graphql_relay import PageInfo
from .serializer import *
from .models import *
from django.contrib.auth.models import User


class PageInfoType(graphene.ObjectType):
    total_items = graphene.Int()
    has_next_page = graphene.Boolean()
    has_previous_page = graphene.Boolean()
    total_pages = graphene.Int()


class ItemMasterType(DjangoObjectType):
    class Meta:
        model = ItemMaster
        fields = "__all__"


class ItemMasterConnection(graphene.ObjectType):
    items = graphene.List(ItemMasterType)
    page_info = graphene.Field(PageInfoType)


class ItemIndicatorsType(DjangoObjectType):
    class Meta:
        model = Item_Indicator
        fields = "__all__"


class ItemIndicatorsConnection(graphene.ObjectType):
    items = graphene.List(ItemIndicatorsType)


class ItemTypeType(DjangoObjectType):
    class Meta:
        model = ItemType
        fields = "__all__"


class ItemTypeConnection(graphene.ObjectType):
    items = graphene.List(ItemTypeType)


class UOMType(DjangoObjectType):
    class Meta:
        model = UOM
        fields = "__all__"


class UomConnection(graphene.ObjectType):
    items = graphene.List(UOMType)
    page_info = graphene.Field(PageInfoType)


class ItemGroupsNameType(DjangoObjectType):
    class Meta:
        model = Item_Groups_Name  # Corrected from Model to model (case sensitive)
        fields = "__all__"  # This includes all fields from the model


class ItemGroupsNameConnection(graphene.ObjectType):
    items = graphene.List(ItemGroupsNameType)
    page_info = graphene.Field(PageInfoType)


class Alternate_Unit_Type(DjangoObjectType):
    class Meta:
        model = Alternate_unit
        fields = "__all__"


class CategoryType(DjangoObjectType):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryConnection(graphene.ObjectType):
    items = graphene.List(CategoryType)


class ContactDetalisType(DjangoObjectType):
    class Meta:
        model = ContactDetalis
        fields = "__all__"


class ContactDetalisConnection(graphene.ObjectType):
    items = graphene.List(ContactDetalisType)
    page_info = graphene.Field(PageInfoType)


class CompanyAddressType(DjangoObjectType):
    class Meta:
        model = CompanyAddress
        fields = "__all__"


class CompanyAddressConnection(graphene.ObjectType):
    items = graphene.List(CompanyAddressType)
    page_info = graphene.Field(PageInfoType)


class SupplierFormDataType(DjangoObjectType):
    class Meta:
        model = SupplierFormData
        fields = "__all__"


class SupplierFormDataConnection(graphene.ObjectType):
    items = graphene.List(SupplierFormDataType)
    page_info = graphene.Field(PageInfoType)


class AccountsMaster_Type(DjangoObjectType):
    class Meta:
        model = AccountsMaster
        fields = "__all__"


class AccountsMasterConnection(graphene.ObjectType):
    items = graphene.List(AccountsMaster_Type)
    page_info = graphene.Field(PageInfoType)


class AccountsGroupType(DjangoObjectType):
    class Meta:
        model = AccountsGroup
        fields = "__all__"


class AccountsGroupConnection(graphene.ObjectType):
    items = graphene.List(AccountsGroupType)
    page_info = graphene.Field(PageInfoType)


class HsnType_Type(DjangoObjectType):
    class Meta:
        model = HsnType
        fields = "__all__"


class HsnType_TypeConnection(graphene.ObjectType):
    items = graphene.List(HsnType_Type)


class GstRateType(DjangoObjectType):
    class Meta:
        model = GstRate
        fields = "__all__"


class GstRate_TypeConnection(graphene.ObjectType):
    items = graphene.List(GstRateType)


class Hsn_Type(DjangoObjectType):
    class Meta:
        model = Hsn
        fields = "__all__"


class HsnConnection(graphene.ObjectType):
    items = graphene.List(Hsn_Type)
    page_info = graphene.Field(PageInfoType)


class StoreType(DjangoObjectType):
    class Meta:
        model = Store
        fields = "__all__"


class StoreConnection(graphene.ObjectType):
    items = graphene.List(StoreType)
    page_info = graphene.Field(PageInfoType)


class DisplayGroupType(DjangoObjectType):
    class Meta:
        model = display_group
        fields = "__all__"


class CustomerGroupsType(DjangoObjectType):
    class Meta:
        model = CustomerGroups
        fields = "__all__"


class CustomerGroupsConnection(graphene.ObjectType):
    items = graphene.List(CustomerGroupsType)
    page_info = graphene.Field(PageInfoType)


class SupplierGroupsType(DjangoObjectType):
    class Meta:
        model = SupplierGroups
        fields = "__all__"


class SupplierGroupsConnection(graphene.ObjectType):
    items = graphene.List(SupplierGroupsType)
    page_info = graphene.Field(PageInfoType)


class ItemComboType(DjangoObjectType):
    class Meta:
        model = Item_Combo
        fields = "__all__"


class User_Type(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"


class Query(ObjectType):
    item_master = graphene.Field(ItemMasterConnection, page=graphene.Int(), page_size=graphene.Int(),
                                 order_by=graphene.String(), descending=graphene.Boolean(), id=graphene.Int(),
                                 item_part_code=graphene.String(), item_name=graphene.String(),
                                 item_group=graphene.String(),
                                 category=graphene.String(), item_uom=graphene.String(),
                                 item_types=graphene.String(), item_indicators=graphene.String(),
                                 service=graphene.Boolean(),
                                 item_combo_bool=graphene.Boolean(), keep_stock=graphene.Boolean(),
                                 item_active=graphene.Boolean())
    item_indicators = graphene.Field(ItemIndicatorsConnection)
    item_Type = graphene.Field(ItemTypeConnection)
    uom = graphene.Field(UomConnection, page=graphene.Int(), page_size=graphene.Int(), order_by=graphene.String(),
                         descending=graphene.Boolean(), name=graphene.String(), e_way_bill_uom=graphene.String(),
                         description=""
                         )
    item_groups_name = graphene.Field(ItemGroupsNameConnection, page=graphene.Int(), page_size=graphene.Int(),
                                      order_by=graphene.String(), descending=graphene.Boolean(),
                                      name=graphene.String(), parent_group=graphene.String(), hsn=graphene.String())
    alternate_unit = List(Alternate_Unit_Type, id=graphene.Int())
    categories = graphene.Field(CategoryConnection)
    supplier_form_data = graphene.Field(SupplierFormDataConnection, page=graphene.Int(), page_size=graphene.Int(),
                                        order_by=graphene.String(), descending=graphene.Boolean(),
                                        company_name=graphene.String(), legal_name=graphene.String(),
                                        gstin=graphene.String(), pan_no=graphene.String(),
                                        Contact_Person_Name=graphene.String(), Phone_number=graphene.String(),
                                        address_type=graphene.String(), city=graphene.String(),
                                        country=graphene.String()
                                        )
    accounts_master = graphene.Field(AccountsMasterConnection, page=graphene.Int(), page_size=graphene.Int(),
                                     order_by=graphene.String(), descending=graphene.Boolean(),
                                     accounts_name=graphene.String(), accounts_group_name=graphene.String()
                                     , gst_applicable=graphene.Boolean(), tds=graphene.Boolean(),
                                     accounts_active=graphene.Boolean())
    accounts_group = graphene.Field(AccountsGroupConnection, page=graphene.Int(), page_size=graphene.Int(),
                                    order_by=graphene.String(), descending=graphene.Boolean(),
                                    accounts_group_name=graphene.String(), accounts_type=graphene.String(),
                                    group_active=graphene.Boolean())
    Store = graphene.Field(StoreConnection, page=graphene.Int(), page_size=graphene.Int(), order_by=graphene.String(),
                           descending=graphene.Boolean(), store_name=graphene.String(), store_account=graphene.String()
                           , store_incharge=graphene.String(), matained=graphene.Boolean(), action=graphene.Boolean())

    hsn_type = graphene.Field(HsnType_TypeConnection)
    gst_rate = graphene.Field(GstRate_TypeConnection)

    hsn = graphene.Field(HsnConnection, page=graphene.Int(), page_size=graphene.Int(), order_by=graphene.String(),
                         descending=graphene.Boolean(), hsn_types=graphene.String(), hsn_code=graphene.Int(),
                         description="", gst_rate=graphene.Int(), cess_rate=graphene.Int(), rcm=graphene.Boolean(),
                         itc=graphene.Boolean())
    display_group = graphene.Field(DisplayGroupType, id=graphene.Int())
    customer_groups = graphene.Field(CustomerGroupsConnection, page=graphene.Int(), page_size=graphene.Int(),
                                     order_by=graphene.String(), descending=graphene.Boolean(), )
    contact_detalis = graphene.Field(ContactDetalisConnection, id=graphene.Int())
    company_address = graphene.Field(CompanyAddressConnection, id=graphene.Int())
    supplier_groups = graphene.Field(SupplierGroupsConnection, page=graphene.Int(), page_size=graphene.Int(),
                                     order_by=graphene.String(), descending=graphene.Boolean(), )

    item_combo = graphene.Field(ItemComboType, id=graphene.Int(), page=graphene.Int(), page_size=graphene.Int(),
                                order_by=graphene.String(), descending=graphene.Boolean())
    User = List(User_Type)

    def resolve_item_master(self, info, page=1, page_size=20, order_by=None, descending=False, id=None,
                            item_part_code=None,
                            item_name=None, category=None, item_group=None,
                            item_uom=None, item_types=None, item_indicators=None, service=None, item_combo_bool=None
                            , keep_stock=None, item_active=None):
        """retun the data with filiter"""
        queryset = ItemMaster.objects.all().order_by('-id')
        """Apply filters"""
        filter_kwargs = {}
        if id:
            filter_kwargs['id__icontains'] = id
        if item_part_code:
            filter_kwargs['item_part_code__icontains'] = item_part_code
        if item_name:
            filter_kwargs['item_name__icontains'] = item_name
        if category:
            filter_kwargs['category__name__icontains'] = category
        if item_group:
            filter_kwargs['item_group__name__icontains'] = item_group
        if item_uom:
            filter_kwargs['item_uom__name__icontains'] = item_uom
        if item_types:
            filter_kwargs['item_types__name__icontains'] = item_types
        if item_indicators:
            filter_kwargs['item_indicators__name__icontains'] = item_indicators
        if service is not None:
            filter_kwargs['service'] = service
        if item_combo_bool is not None:
            filter_kwargs['item_combo_bool'] = item_combo_bool
        if keep_stock is not None:
            filter_kwargs['keep_stock'] = keep_stock
        if item_active is not None:
            filter_kwargs['item_active'] = item_active
        db_s = {
            "id": {"field": "id", "is_text": False},
            'itemPartCode': {"field": 'item_part_code', "is_text": True},
            'itemName':  {"field": 'item_name', "is_text": True},
            "itemGroup":  {"field": 'item_group', "is_text": True},
            "category": {"field": 'category', "is_text": True},
            "itemUom": {"field": 'item_uom', "is_text": True},
            "itemTypes": {"field": 'item_types', "is_text": True},
            "itemIndicators": {"field": 'item_indicators', "is_text": True},
            "service": {"field": 'service', "is_text": True},
            "itemComboBool": {"field": 'item_combo_bool', "is_text": True},
            "keepStock": {"field": 'keepStock', "is_text": True},
            "itemActive": {"field": 'item_active', "is_text": True},
        }




        # Apply case-insensitive sorting
        queryset = queryset.filter(**filter_kwargs)
        if order_by:
            order_by_config = db_s.get(order_by)

            if order_by_config:
                order_by_field = order_by_config["field"]
                is_text_field = order_by_config["is_text"]

                if is_text_field:
                    # For text fields, annotate with a lowercased version for case-insensitive sorting
                    annotated_field_name = f'lower_{order_by_field}'
                    queryset = queryset.annotate(**{annotated_field_name: Lower(order_by_field)})
                    order_by_field = annotated_field_name
    
                # Determine sorting direction
                if descending:
                    order_by_field = f'-{order_by_field}'

                # Apply sorting
                queryset = queryset.order_by(order_by_field)

        # Pagination
        paginator = Paginator(queryset, page_size)
        paginated_data = paginator.get_page(page)

        page_info = PageInfoType(
            total_items=paginator.count,
            has_next_page=paginated_data.has_next(),
            has_previous_page=paginated_data.has_previous(),
            total_pages=paginator.num_pages,
        )

        return ItemMasterConnection(
            items=paginated_data.object_list,
            page_info=page_info
        )

    def resolve_item_indicators(self, info):
        queryset = Item_Indicator.objects.all()

        return ItemIndicatorsConnection(
            items=queryset,
        )

    def resolve_item_Type(self, info):
        queryset = ItemType.objects.all()
        return ItemTypeConnection(
            items=queryset,
        )

    def resolve_uom(self, info, page=1, page_size=20, order_by=None, descending=False, name=None,
                    e_way_bill_uom=None,
                    description=None
                    ):
        """retun the data with filiter"""
        queryset = UOM.objects.all()

        """Apply filters"""
        filter_kwargs = {}
        if name:
            filter_kwargs['name__icontains'] = name
        if e_way_bill_uom:
            filter_kwargs['e_way_bill_uom__icontains'] = e_way_bill_uom
        if description:
            filter_kwargs['description__icontains'] = description
        """Apply sorting"""
        if order_by:
            if descending:
                order_by = f"-{order_by}"
            queryset = queryset.filter(**filter_kwargs).order_by(order_by)
        else:
            queryset = queryset.filter(**filter_kwargs)
        paginator = Paginator(queryset, page_size)
        paginated_data = paginator.get_page(page)

        page_info = PageInfoType(
            total_items=paginator.count,
            has_next_page=paginated_data.has_next(),
            has_previous_page=paginated_data.has_previous(),
            total_pages=paginator.num_pages,
        )

        return UomConnection(
            items=paginated_data.object_list,
            page_info=page_info
        )

    def resolve_item_groups_name(self, info, page=1, page_size=20, order_by=None, descending=False, name=None,
                                 parent_group=None, hsn=None):

        """retun the data with filiter"""
        queryset = Item_Groups_Name.objects.all()
        """Apply filters"""
        filter_kwargs = {}
        if name:
            filter_kwargs['name__icontains'] = name
        if parent_group:
            filter_kwargs['parent_group__icontains'] = parent_group
        if hsn:
            filter_kwargs['hsn__hsn_code__icontains'] = hsn

        """Apply sorting"""
        if order_by:
            if descending:
                order_by = f"-{order_by}"
            queryset = queryset.filter(**filter_kwargs).order_by(order_by)
        else:
            queryset = queryset.filter(**filter_kwargs)
        paginator = Paginator(queryset, page_size)
        paginated_data = paginator.get_page(page)

        page_info = PageInfoType(
            total_items=paginator.count,
            has_next_page=paginated_data.has_next(),
            has_previous_page=paginated_data.has_previous(),
            total_pages=paginator.num_pages,
        )

        return UomConnection(
            items=paginated_data.object_list,
            page_info=page_info
        )

    def resolve_alternate_unit(self, info, id=None):
        queryset = Alternate_unit.objects.filter(id=id)

        return queryset

    def resolve_categories(self, info, **kwargs):
        queryset = Category.objects.all()
        return CategoryConnection(
            items=queryset
        )

    def resolve_contact_detalis(self, info, id=None):
        queryset = ContactDetalis.objects.filter(id=id)
        return queryset

    def resolve_company_address(self, info, id=None):
        queryset = CompanyAddress.objects.filter(id=id)
        return queryset

    def resolve_supplier_form_data(self, info, page=1, page_size=20, order_by=None, descending=False, company_name=None
                                   , legal_name=None, gstin=None, pan_no=None, Contact_Person_Name=None,
                                   Phone_number=None,
                                   address_type=None, city=None, country=None):
        """retun the data with filiter"""
        queryset = SupplierFormData.objects.all()
        """Apply filters"""
        filter_kwargs = {}
        if company_name:
            filter_kwargs['company_name__icontains'] = company_name
        if legal_name:
            filter_kwargs['legal_name__icontains'] = legal_name
        if gstin:
            filter_kwargs['gstin__icontains'] = gstin
        if pan_no:
            filter_kwargs['pan_no__icontains'] = pan_no
        if Contact_Person_Name:
            filter_kwargs['contact__Contact_Person_Name__icontains'] = Contact_Person_Name
        if Phone_number:
            filter_kwargs['contact__Phone_number__icontains'] = Phone_number
        if address_type:
            filter_kwargs['address__address_type__icontains'] = address_type
        if city:
            filter_kwargs['contact__city__icontains'] = city
        if country:
            filter_kwargs['contact__country__icontains'] = country
        """Apply sorting"""
        if order_by:
            if descending:
                order_by = f"-{order_by}"
            queryset = queryset.filter(**filter_kwargs).order_by(order_by)
        else:
            queryset = queryset.filter(**filter_kwargs)
        paginator = Paginator(queryset, page_size)
        paginated_data = paginator.get_page(page)

        page_info = PageInfoType(
            total_items=paginator.count,
            has_next_page=paginated_data.has_next(),
            has_previous_page=paginated_data.has_previous(),
            total_pages=paginator.num_pages,
        )
        #
        return SupplierFormDataConnection(
            items=paginated_data.object_list,
            page_info=page_info
        )

    def resolve_accounts_group(self, info, page=1, page_size=20, order_by=None, descending=False,
                               accounts_group_name=None, accounts_type=None, group_active=None):
        #
        """retun the data with filiter"""
        queryset = AccountsGroup.objects.all()
        """Apply filters"""
        filter_kwargs = {}
        if accounts_group_name:
            filter_kwargs['accounts_group_name__icontains'] = accounts_group_name
        if accounts_type:
            filter_kwargs['accounts_type__icontains'] = accounts_type
        if group_active:
            filter_kwargs['group_active'] = group_active
        """Apply sorting"""
        if order_by:
            if descending:
                order_by = f"-{order_by}"
            queryset = queryset.filter(**filter_kwargs).order_by(order_by)
        else:
            queryset = queryset.filter(**filter_kwargs)
        paginator = Paginator(queryset, page_size)
        paginated_data = paginator.get_page(page)

        page_info = PageInfoType(
            total_items=paginator.count,
            has_next_page=paginated_data.has_next(),
            has_previous_page=paginated_data.has_previous(),
            total_pages=paginator.num_pages,
        )

        return AccountsGroupConnection(
            items=paginated_data.object_list,
            page_info=page_info
        )

    def resolve_accounts_master(self, info, page=1, page_size=20, order_by=None, descending=False, accounts_name=None,
                         accounts_group_name=None, gst_applicable=None, tds=None, accounts_active=None):
        """retun the data with filiter"""
        queryset = AccountsMaster.objects.all()
        """Apply filters"""
        filter_kwargs = {k: v for k, v in {
            'accounts_name__icontains': accounts_name,
            'accounts_group_name__icontains': accounts_group_name,
            'gst_applicable': gst_applicable,
            'tds': tds,
            'accounts_active': accounts_active,
        }.items() if v is not None}
        """Apply sorting"""
        if order_by:
            if descending:
                order_by = f"-{order_by}"
            queryset = queryset.filter(**filter_kwargs).order_by(order_by)
        else:
            queryset = queryset.filter(**filter_kwargs)
        paginator = Paginator(queryset, page_size)
        paginated_data = paginator.get_page(page)
        #
        page_info = PageInfoType(
            total_items=paginator.count,
            has_next_page=paginated_data.has_next(),
            has_previous_page=paginated_data.has_previous(),
            total_pages=paginator.num_pages,
        )
        return AccountsMasterConnection(
            items=paginated_data.object_list,
            page_info=page_info
        )

    def resolve_hsn_type(self, info):
        queryset = HsnType.objects.all()
        return HsnType_TypeConnection(
            items=queryset,
        )

    def resolve_gst_rate(self, info):
        queryset = GstRate.objects.all()
        return GstRate_TypeConnection(
            items=queryset,
        )

    def resolve_hsn(self, info, page=1, page_size=20, order_by=None, descending=False, hsn_types=None,
                    hsn_code=None, description=None, gst_rate=None, cess_rate=None, rcm=None,
                    itc=None):
        """retun the data with filiter"""
        queryset = Hsn.objects.all()
        """Apply filters"""
        filter_kwargs = {k: v for k, v in {
            'hsn_types__name__icontains': hsn_types,
            'hsn_code__icontains': hsn_code,
            'description__icontains': description,
            'gst_rate__rate__icontains': gst_rate,
            'cess_rate__icontains': cess_rate,
            'rcm__icontains': rcm,
            'itc__icontains': itc
        }.items() if v is not None}
        """Apply sorting"""
        if order_by:
            if descending:
                order_by = f"-{order_by}"
            queryset = queryset.filter(**filter_kwargs).order_by(order_by)
        else:
            queryset = queryset.filter(**filter_kwargs)
        paginator = Paginator(queryset, page_size)
        paginated_data = paginator.get_page(page)
        page_info = PageInfoType(
            total_items=paginator.count,
            has_next_page=paginated_data.has_next(),
            has_previous_page=paginated_data.has_previous(),
            total_pages=paginator.num_pages,
        )

        return HsnConnection(
            items=paginated_data.object_list,
            page_info=page_info
        )

    def resolve_Store(self, info, page=1, page_size=20, order_by=None, descending=False, store_name=None,
                      store_account=None, store_incharge=None,
                      matained=None, action=None):
        """retun the data with filiter"""
        queryset = Store.objects.all()
        """Apply filters"""
        filter_kwargs = {k: v for k, v in {
            'store_name__icontains': store_name,
            'store_account__accounts_name__icontains': store_account,
            'store_incharge__Username__icontains': store_incharge,
            'matained__icontains': matained,
            'action__icontains': action,
        }.items() if v is not None}
        """Apply sorting"""
        if order_by:
            if descending:
                order_by = f"-{order_by}"
            queryset = queryset.filter(**filter_kwargs).order_by(order_by)
        else:
            queryset = queryset.filter(**filter_kwargs)
        paginator = Paginator(queryset, page_size)
        paginated_data = paginator.get_page(page)
        page_info = PageInfoType(
            total_items=paginator.count,
            has_next_page=paginated_data.has_next(),
            has_previous_page=paginated_data.has_previous(),
            total_pages=paginator.num_pages,
        )
        return StoreConnection(
            items=paginated_data.object_list,
            page_info=page_info
        )

    def resolve_display_group(self, id=None):
        queryset = display_group.objects.filter(id=id)
        return queryset

    def resolve_item_combo(self, id=None):
        queryset = Item_Combo.objects.filter(id=id)
        return queryset

    def resolve_customer_groups(self, info, page=1, page_size=20, order_by=None, descending=False):
        """retun the data with filiter"""
        queryset = CustomerGroups.objects.all()
        filter_kwargs = {}
        """Apply sorting"""
        if order_by:
            if descending:
                order_by = f"-{order_by}"
            queryset = queryset.filter(**filter_kwargs).order_by(order_by)
        else:
            queryset = queryset.filter(**filter_kwargs)
        paginator = Paginator(queryset, page_size)
        paginated_data = paginator.get_page(page)
        page_info = PageInfoType(
            total_items=paginator.count,
            has_next_page=paginated_data.has_next(),
            has_previous_page=paginated_data.has_previous(),
            total_pages=paginator.num_pages,
        )
        return CustomerGroupsConnection(
            items=paginated_data.object_list,
            page_info=page_info
        )

    def resolve_supplier_groups(self, page=1, page_size=20, order_by=None, descending=False):
        """retun the data with filiter"""
        queryset = SupplierGroups.objects.all()
        filter_kwargs = {}
        """Apply sorting"""
        if order_by:
            if descending:
                order_by = f"-{order_by}"
            queryset = queryset.filter(**filter_kwargs).order_by(order_by)
        else:
            queryset = queryset.filter(**filter_kwargs)
        paginator = Paginator(queryset, page_size)
        paginated_data = paginator.get_page(page)
        page_info = PageInfoType(
            total_items=paginator.count,
            has_next_page=paginated_data.has_next(),
            has_previous_page=paginated_data.has_previous(),
            total_pages=paginator.num_pages,
        )
        return SupplierGroupsConnection(
            items=paginated_data.object_list,
            page_info=page_info
        )

    def resolve_user(self, info):
        return User.objects.all()


# schema = graphene.Schema(query=Query, )
