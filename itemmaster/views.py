import json

from django.http import HttpResponse
from rest_framework import status
from datetime import datetime, timezone
from rest_framework.views import APIView
from .serializer import *
from django.http import JsonResponse
from django.forms.models import model_to_dict
from decimal import Decimal
from collections import defaultdict
from django.db import connection

"""EditListViews"""
class EditListViews(APIView):
    def get(self, request):
        article = EditListView.objects.all().order_by('-id')

        serialzer = EditListViewSerializer(article, many=True)

        return Response(serialzer.data)

    def post(self, request):
        serializer = EditListViewSerializer(data=request.data)
        print(serializer)
        print(serializer.is_valid())
        print(serializer.errors)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EditListViewDetails(APIView):
    def get_object(self, pk):
        try:
            return EditListView.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = EditListViewSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = EditListViewSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"Hsn"


class HsnCreateView(APIView):
    def get(self, request):
        article = Hsn.objects.all().order_by('-id')

        serialzer = HsnSerializer(article, many=True)

        return Response(serialzer.data)

    def post(self, request):
        serializer = HsnSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HsnDetails(APIView):
    def get_object(self, pk):
        try:
            return Hsn.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = HsnSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = HsnSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""ItemGroup"""


class ItemGroupCreateView(APIView):
    def get(self, request):
        article = Item_Groups_Name.objects.all().order_by('-id')
        serialzer = ItemGroupSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = ItemGroupSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemGroupDetails(APIView):
    def get_object(self, pk):
        try:
            return Item_Groups_Name.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = ItemGroupSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ItemGroupSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"UOM"


class UOMCreateView(APIView):
    def get(self, request):
        article = UOM.objects.all().order_by('-id')
        serialzer = UOMSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = UOMSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UOMDetails(APIView):
    def get_object(self, pk):
        try:
            return UOM.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = UOMSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = UOMSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""Category"""


class CategoryCreateView(APIView):
    def get(self, request):
        article = Category.objects.all().order_by('-id')
        serialzer = CategorySerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""AccountsGroup"""


class AccountsGroupCreateView(APIView):
    def get(self, request):
        article = AccountsGroup.objects.all().order_by('-id')
        serialzer = AccountsGroupSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = AccountsGroupSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountsGroupDetails(APIView):
    def get_object(self, pk):
        try:
            return AccountsGroup.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = AccountsGroupSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = AccountsGroupSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""AccountsMaster"""


class AccountsMasterCreateView(APIView):
    def get(self, request):
        article = AccountsMaster.objects.all().order_by('-id')
        serialzer = AccountsMasterSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = AccountsMasterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AccountsMasterDetails(APIView):
    def get_object(self, pk):
        try:
            return AccountsMaster.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = AccountsMasterSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = AccountsMasterSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""Alternate_unit"""


class AlternateUnitCreateView(APIView):
    def get(self, request):
        article = Alternate_unit.objects.all().order_by('-id')
        serialzer = Alternate_unitSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = Alternate_unitSerializer(data=request.data)
        print(serializer.is_valid())
        print(serializer.errors)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AlternateUnitDetails(APIView):
    def get_object(self, pk):
        try:
            return Alternate_unit.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = Alternate_unitSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = Alternate_unitSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""ItemMaster"""


class ItemMasterCreateView(APIView):
    def get(self, request):
        article = ItemMaster.objects.all().order_by('-id')
        serialzer = ItemMasterSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = ItemMasterSerializer(data=request.data)
        print(request.data)
        print(serializer.is_valid())
        print(serializer.errors)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemMasterDetails(APIView):
    def get_object(self, pk):
        try:
            return ItemMaster.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = ItemMasterSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ItemMasterSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""Store"""


class StoreCreateView(APIView):
    def get(self, request):
        article = Store.objects.all().order_by('-id')
        serialzer = StoreSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = StoreSerializer(data=request.data)
        print(serializer, '---->>>')
        # print(serializer.errors)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StoreDetails(APIView):
    def get_object(self, pk):
        try:
            return Store.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = StoreSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = StoreSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""StockSerialHistory"""


class StockSerialHistoryCreateView(APIView):
    def get(self, request):
        article = StockSerialHistory.objects.all().order_by('-id')
        serialzer = StockSerialHistorySerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = StockSerialHistorySerializer(data=request.data)
        print(serializer, '---->>>')
        # print(serializer.errors)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockSerialHistoryDetails(APIView):
    def get_object(self, pk):
        try:
            return StockSerialHistory.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = StockSerialHistorySerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = StockSerialHistorySerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""BatchNumber"""


class BatchNumberCreateView(APIView):
    def get(self, request):
        article = BatchNumber.objects.all().order_by('id')
        serialzer = BatchNumberSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = BatchNumberSerializer(data=request.data)
        print(serializer)

        if serializer.is_valid():
            serializer.save()
            serializer.save()

            return Response(serializer.data, )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BatchNumberDetails(APIView):
    def get_object(self, pk):
        try:
            return BatchNumber.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = BatchNumberSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = BatchNumberSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""SerialNumbers"""


class SerialNumbersCreateView(APIView):
    def get(self, request):
        article = SerialNumbers.objects.all().order_by('id')
        serialzer = SerialNumbersSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = SerialNumbersSerializer(data=request.data)
        print(serializer)

        if serializer.is_valid():
            serializer.save()
            serializer.save()

            return Response(serializer.data, )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SerialNumbersDetails(APIView):
    def get_object(self, pk):
        try:
            return SerialNumbers.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = SerialNumbersSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = SerialNumbersSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""Item Stock"""


class ItemStockCreateView(APIView):
    def get(self, request):
        article = ItemStock.objects.all().order_by('-id')
        serialzer = ItemStockSerializer(article, many=True)

        return Response(serialzer.data)

    def post(self, request):
        serializer = ItemStockSerializer(data=request.data)
        print(serializer.is_valid())
        print(serializer.errors)
        print(serializer)

        if serializer.is_valid():
            serializer.save()
            serializer.save()

            return Response(serializer.data, )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StockDetails(APIView):
    def get_object(self, pk):
        try:
            return ItemStock.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = ItemStockSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ItemStockSerializer(article, data=request.data)
        print(serializer)
        print(serializer.is_valid())
        print(serializer.errors)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""StockHistoryLog"""
class StockHistoryLogCreateView(APIView):
    def get(self, request):
        article = StockHistoryLog.objects.all().order_by('-id')
        serialzer = StockHistoryLogSerializer(article, many=True)

        return Response(serialzer.data)

"""Inventory Approvals"""


class ItemInventoryApprovalCreateView(APIView):
    def get(self, request):
        article = ItemInventoryApproval.objects.all().order_by('id')
        serialzer = ItemInventoryApprovalSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = ItemInventoryApprovalSerializer(data=request.data)
        # print(serializer)
        # print(serializer.is_valid())
        # print(serializer.errors)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""Inventory Handler"""


class InventoryHandlerCreateView(APIView):
    def get(self, request):
        article = InventoryHandler.objects.all().order_by('-id')
        serialzer = InventoryHandlerSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = InventoryHandlerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InventoryHandlerDetails(APIView):
    def get_object(self, pk):
        try:
            return InventoryHandler.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = InventoryHandlerSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = InventoryHandlerSerializer(article, data=request.data)
        print(serializer)
        print(serializer.is_valid())
        print(serializer.errors)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""Item Combo"""


class ItemComboCreateView(APIView):
    def get(self, request):
        article = Item_Combo.objects.all().order_by('-id')
        serialzer = ItemComboSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = ItemComboSerializer(data=request.data)
        print(serializer)
        print(serializer.is_valid())
        print(serializer.errors)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemComboDetails(APIView):
    def get_object(self, pk):
        try:
            return Item_Combo.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = ItemComboSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ItemComboSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""Customer Group"""


class CustomerGroupCreateView(APIView):
    def get(self, request):
        article = CustomerGroups.objects.all().order_by('-id')
        serialzer = CustomerGroupsSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = CustomerGroupsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomerGroupDetails(APIView):
    def get_object(self, pk):
        try:
            return CustomerGroups.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = CustomerGroupsSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = CustomerGroupsSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""Supplier Group"""


class SupplierGroupCreateView(APIView):
    def get(self, request):
        article = SupplierGroups.objects.all().order_by('-id')
        serialzer = SupplierGroupsSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = SupplierGroupsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SupplierGroupDetails(APIView):
    def get_object(self, pk):
        try:
            return SupplierGroups.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = SupplierGroupsSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = SupplierGroupsSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""Contact Details"""


class ItemContactCreateView(APIView):
    def get(self, request):
        article = contact_detalis.objects.all().order_by('-id')
        serialzer = ItemContactSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = ItemContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemContactDetails(APIView):
    def get_object(self, pk):
        try:
            return contact_detalis.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = ItemContactSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ItemContactSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""Address"""


class ItemAddressCreateView(APIView):
    def get(self, request):
        article = company_address.objects.all().order_by('-id')
        serialzer = ItemAddressSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = ItemAddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemAddressDetails(APIView):
    def get_object(self, pk):
        try:
            return company_address.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = ItemAddressSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ItemAddressSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""Supplier form"""


class ItemSupplierFormCreateView(APIView):

    def get(self, request):
        articles = Supplier_Form_Data.objects.all().order_by('-id')
        serializer = ItemSupplierSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemSupplierSerializer(data=request.data)
        print(serializer.is_valid())
        print(serializer.errors)
        print(serializer)

        if serializer.is_valid():
            # try:
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # except Exception as e:
        #     print(e)
        #
        #
        #     return Response(error, status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ItemSupplierFormDetails(APIView):
    def get_object(self, pk):
        try:
            return Supplier_Form_Data.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = ItemSupplierSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ItemSupplierSerializer(article, data=request.data)
        print(serializer.is_valid())
        print(serializer.errors)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CurrencyMasterCreateView(APIView):
    def get(self, request):
        article = CurrencyMaster.objects.all().order_by('-id')
        serialzer = CurrencyMasterSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = CurrencyMasterSerializer(data=request.data)
        print(serializer)
        print(serializer.is_valid())
        print(serializer.errors)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurrencyMasterDetails(APIView):
    def get_object(self, pk):
        try:
            return CurrencyMaster.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = CurrencyMasterSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = CurrencyMasterSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CurrencyExchangeCreateView(APIView):
    def get(self, request):
        article = CurrencyExchange.objects.all().order_by('-id')
        serialzer = CurrencyExchangeSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = CurrencyExchangeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurrencyExchangeDetails(APIView):
    def get_object(self, pk):
        try:
            return CurrencyExchange.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = CurrencyExchangeSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = CurrencyExchangeSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""SalesOrderItem"""


class SalesOrderItemCreateView(APIView):
    def get(self, request):
        article = SalesOrderItem.objects.all().order_by('-id')
        serialzer = SalesOrderItemSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = SalesOrderItemSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalesOrderItemDetails(APIView):
    def get_object(self, pk):
        try:
            return SalesOrderItem.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = SalesOrderItemSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = SalesOrderItemSerializer(article, data=request.data)
        print(serializer)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


"""SalesOrder"""


class SalesOrderCreateView(APIView):
    def get(self, request):
        article = SalesOrder.objects.all().order_by('-id')
        serialzer = SalesOrderSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = SalesOrderSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SalesOrderDetails(APIView):
    def get_object(self, pk):
        try:
            return SalesOrder.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = SalesOrderSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = SalesOrderSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# test table


class testStaanTableCreateView(APIView):
    def get(self, request):
        article = testStaanTable.objects.all().order_by('-id')
        serialzer = testStaanTableSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = testStaanTableSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class testStaanTableDetails(APIView):
    def get_object(self, pk):
        try:
            return testStaanTable.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = testStaanTableSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = testStaanTableSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# stock statement part start
def process_stock_statement(store_id=None, group_id=None):
    item_master_data = list(ItemMaster.objects.values('id', 'Item_PartCode', 'Item_name', 'Item_Group'))
    store_data = {item['id']: item['StoreName'] for item in list(Store.objects.values('id', 'StoreName'))}
    stock_data = list(ItemStock.objects.values('id', 'part_no', 'currentStock', 'store'))
    item_group_data = {item['id']: item['name'] for item in list(Item_Groups_Name.objects.values('id', 'name'))}
    filtered_master_items = []
    for item in item_master_data:
        part_no = item['id']
        data_result = {
            'part_no': part_no,
            'part_code': item['Item_PartCode'],
            'part_name': item['Item_name'],
            'item_group': item_group_data[item['Item_Group']]
        }
        if store_id is None:
            filtered_data = [(int(stock_item['currentStock']), stock_item['store']) for stock_item in stock_data if stock_item['part_no'] == part_no]
        else:
            filtered_data = [(int(stock_item['currentStock']), stock_item['store']) for stock_item in stock_data if stock_item['part_no'] == part_no and int(stock_item['store']) == int(store_id)]
        sum_of_stocks_in_store = 0
        stores = ''
        store_ids = []
        if filtered_data:
            sum_of_stocks_in_store = sum(item[0] for item in filtered_data if len(item) > 1)
            store_ids = list(set([item[1] for item in filtered_data if len(item) > 1]))
            try:
                stores = ', '.join(list(set([store_data[item[1]] for item in filtered_data])))
            except:
                stores = ''
        data_result['qty'] = sum_of_stocks_in_store
        data_result['stores'] = stores
        data_result['store_ids'] = store_ids
        filtered_master_items.append(data_result)
    if group_id:
        filtered_master_items = [item for item in filtered_master_items if item['item_group'] == item_group_data[int(group_id)]]
    return filtered_master_items


# def get_stock_statement_by_all_store(request):
#     """ get stock details in the all stores """
#     if request.method == 'GET':
#         filtered_data = process_stock_statement()
#         return JsonResponse(filtered_data, safe=False)
#
#
# def get_stock_statement_by_given_store(request, store_id):
#     """ get stock details in the all stores """
#     if request.method == 'GET':
#         filtered_data = process_stock_statement(store_id=store_id)
#         return JsonResponse(filtered_data, safe=False)


def process_stock_statement_for_single_item(part_no, store_id=None, group_id=None):
    item_master_instance = ItemMaster.objects.get(id=part_no)
    if group_id:
        item_master_instance = ItemMaster.objects.get(id=part_no, Item_Group=int(group_id))
    item_master_dict = model_to_dict(item_master_instance)
    store_data = {item['id']: item['StoreName'] for item in list(Store.objects.values('id', 'StoreName'))}
    item_group_data = {item['id']: item['name'] for item in list(Item_Groups_Name.objects.values('id', 'name'))}
    stock_data = list(ItemStock.objects.values('id', 'part_no', 'currentStock', 'store',  'BatchNumber', 'Serialnum'))
    is_serial = item_master_dict['serial']
    is_batch = item_master_dict['Batch_number']
    if store_id is None:
        filtered_data = [stock_item for stock_item in stock_data if stock_item['part_no'] == int(part_no)]
    else:
        filtered_data = [stock_item for stock_item in stock_data if stock_item['part_no'] == int(part_no) and int(stock_item['store']) == int(store_id)]
    stock_statement_data = []
    if is_serial:
        for filtered_item in filtered_data:
            serial_number = model_to_dict(SerialNumbers.objects.get(id=filtered_item['Serialnum']))['SerialNumber']
            result_data = {
                'part_no': part_no,
                'part_code': item_master_dict['Item_PartCode'],
                'part_name': item_master_dict['Item_name'],
                'Serialnum': serial_number,
                'Batch Number': None,
                'Qty': 1,
                'Store': store_data[filtered_item['store']],
                'store_ids': [filtered_item['store']],
                'item_group': item_group_data[item_master_dict['Item_Group']]
            }
            stock_statement_data.append(result_data)
    elif is_batch:
        # Use a defaultdict to store the aggregated data
        aggregated_data = defaultdict(Decimal)

        # Aggregate the data based on BatchNumber and store
        for item in filtered_data:
            key = (item['BatchNumber'], item['store'])
            aggregated_data[key] += item['currentStock']

        # Convert the defaultdict to a list of dictionaries
        for key, value in aggregated_data.items():
            batch_number = model_to_dict(BatchNumber.objects.get(id=key[0]))['BatchNumberName']
            result_data = {
                'part_no': part_no,
                'part_code': item_master_dict['Item_PartCode'],
                'part_name': item_master_dict['Item_name'],
                'Serialnum': None,
                'Batch Number': batch_number,
                'Qty': value,
                'Store': store_data[key[1]],
                'store_ids': [key[1]],
                'item_group': item_group_data[item_master_dict['Item_Group']]
            }
            stock_statement_data.append(result_data)
    else:
        try:
            sum_of_stocks_in_store = sum(item['currentStock'] for item in filtered_data)
        except:
            sum_of_stocks_in_store = 0
        try:
            stores = ', '.join(list(set([store_data[item['store']] for item in filtered_data])))
        except:
            stores = ''
        try:
            store_ids = list(set([item['store'] for item in filtered_data]))
        except:
            store_ids = []
        result_data = {
            'part_no': part_no,
            'part_code': item_master_dict['Item_PartCode'],
            'part_name': item_master_dict['Item_name'],
            'Serialnum': None,
            'Batch Number': None,
            'Qty': sum_of_stocks_in_store,
            'Store': stores,
            'store_ids': store_ids,
            'item_group': item_group_data[item_master_dict['Item_Group']]
        }
        stock_statement_data.append(result_data)
    return stock_statement_data


# def get_stock_statement_by_all_store_for_single_part_number(request, part_no):
#     """ get stock details in the all stores """
#     if request.method == 'GET':
#         filtered_data = process_stock_statement_for_single_item(part_no)
#         return JsonResponse(filtered_data, safe=False)
#
#
# def get_stock_statement_by_given_store_for_single_part_number(request, part_no, store_id):
#     """ get stock details in the all stores """
#     if request.method == 'GET':
#         filtered_data = process_stock_statement_for_single_item(part_no, store_id=store_id)
#         return JsonResponse(filtered_data, safe=False)


def get_stock_history_details(part_no, StockHistoryMasterData):
    processed_data = []
    for date_key in StockHistoryMasterData:
        data = {
            'part_no': part_no,
            'start_stock': int(Decimal(StockHistoryMasterData[date_key][0]['PreviousState'])),
            'end_stock': int(Decimal(StockHistoryMasterData[date_key][-1]['UpdatedState'])),
            'date': date_key
        }
        total_item_added = 0
        total_item_deleted = 0
        for history_item in StockHistoryMasterData[date_key]:
            modified_data = int(Decimal(history_item['UpdatedState'])) - int(Decimal(history_item['PreviousState']))
            if modified_data < 0:
                total_item_deleted += modified_data
            elif modified_data > 0:
                total_item_added += modified_data
        data['added'] = total_item_added
        data['reduced'] = total_item_deleted
        processed_data.append(data)
    return processed_data


def getStockHistory(request):
    store_id = request.GET.get('store')
    part_id = request.GET.get('part_id')
    if store_id == 'null' or store_id == 'all':
        store_id = None
    if part_id == 'null' or part_id == 'all':
        part_id = None
    if store_id is None:
        stockData = StockHistoryLog.objects.filter(PartNumber=int(part_id), ColumnName="currentStock")
    else:
        stockData = StockHistoryLog.objects.filter(PartNumber=int(part_id), ColumnName="currentStock", StoreLink=int(store_id))

    StockHistoryMasterData = {}
    for StockItem in stockData:
        StockItem = model_to_dict(StockItem)
        timestamp = datetime.fromisoformat(str(StockItem['modifiedDate']))
        formatted_date = timestamp.strftime("%d-%m-%Y")
        if formatted_date in StockHistoryMasterData.keys():
            temp_list = StockHistoryMasterData[formatted_date]
            temp_list.append(StockItem)
            StockHistoryMasterData[formatted_date] = temp_list
        else:
            StockHistoryMasterData[formatted_date] = [StockItem]
    processed_data = get_stock_history_details(part_id, StockHistoryMasterData)
    return JsonResponse(processed_data, safe=False)


# def getStockHistoryWithStore(request, partCode, store_id):
#     stockData = StockHistoryLog.objects.all()
#     StockHistoryMasterData = {}
#     for StockItem in stockData:
#         StockItem = model_to_dict(StockItem)
#         if str(partCode) == str(StockItem['PartNumber']) and str(StockItem['ColumnName']) == "currentStock" and str(store_id) == str(StockItem['StoreLink']):
#             timestamp = datetime.fromisoformat(str(StockItem['modifiedDate']))
#             formatted_date = timestamp.strftime("%Y-%m-%d")
#             if formatted_date in StockHistoryMasterData.keys():
#                 temp_list = StockHistoryMasterData[formatted_date]
#                 temp_list.append(StockItem)
#                 StockHistoryMasterData[formatted_date] = temp_list
#             else:
#                 StockHistoryMasterData[formatted_date] = [StockItem]
#     processed_data = get_stock_history_details(partCode, StockHistoryMasterData)
#     return JsonResponse(processed_data, safe=False)


def stock_statement_store_group_filter(request):
    if request.method == 'GET':
        try:
            store_id = request.GET.get('store')
            group_id = request.GET.get('group')
            part_id = request.GET.get('part_id')
            if store_id == 'null' or store_id == 'all':
                store_id = None
            if group_id == 'null' or group_id == 'all':
                group_id = None
            if part_id == 'null' or part_id == 'all':
                part_id = None

            if part_id:
                filtered_data = process_stock_statement_for_single_item(part_id, store_id, group_id)
            else:
                filtered_data = process_stock_statement(store_id, group_id)

            return JsonResponse(filtered_data, safe=False)
        except Exception as e :
            print(e)


