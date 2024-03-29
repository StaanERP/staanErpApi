import json

from django.db.models import ProtectedError
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
from django.core.serializers import serialize
from django.db.models import Prefetch

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
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


"Hsn"


class HsnCreateView(APIView):
    def get(self, request):
        article = Hsn.objects.all().order_by('-id').filter(is_delete=False)

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
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


"""ItemGroup"""


class ItemGroupCreateView(APIView):
    def get(self, request):
        article = Item_Groups_Name.objects.all().order_by('-id').filter(is_delete=False)
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
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


"UOM"


class UOMCreateView(APIView):
    def get(self, request):
        article = UOM.objects.all().order_by('-id').filter(is_delete=False)
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
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
        article = AccountsGroup.objects.all().order_by('-id').filter(is_delete=False)
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
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            # If the deletion is protected, handle the exception
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


"""AccountsMaster"""


class AccountsMasterCreateView(APIView):
    def get(self, request):
        article = AccountsMaster.objects.all().order_by('-id').filter(is_delete=False)
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
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


"""Alternate_unit"""


class AlternateUnitCreateView(APIView):
    def get(self, request):
        article = Alternate_unit.objects.all().order_by('-id')
        serialzer = Alternate_unitSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = Alternate_unitSerializer(data=request.data)

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
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


"""ItemMaster"""


class ItemMasterCreateView(APIView):
    def get(self, request):
        article = ItemMaster.objects.all().order_by('-id')
        serialzer = ItemMasterSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = ItemMasterSerializer(data=request.data)


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
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


"""Store"""


class StoreCreateView(APIView):
    def get(self, request):
        article = Store.objects.all().order_by('-id').filter(is_delete=False)
        serialzer = StoreSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = StoreSerializer(data=request.data)
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
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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


"""display_group"""


class displayGroupCreateView(APIView):
    def get(self, request):
        article = display_group.objects.all().order_by('-id')
        serialzer = displayGroupSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = displayGroupSerializer(data=request.data)
        # print(serializer)
        # print(serializer.is_valid())
        # print(serializer.errors)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class displayGroupDetails(APIView):
    def get_object(self, pk):
        try:
            return display_group.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = displayGroupSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = displayGroupSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


"""Contact Details"""


class ItemContactCreateView(APIView):
    def get(self, request):
        article = ContactDetalis.objects.all().order_by('-id')
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
            return ContactDetalis.objects.get(pk=pk)
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
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


"""Address"""


class ItemAddressCreateView(APIView):
    def get(self, request):
        article = CompanyAddress.objects.all().order_by('-id')
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
            return CompanyAddress.objects.get(pk=pk)
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
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


"""Supplier form"""


class ItemSupplierFormCreateView(APIView):

    def get(self, request):
        articles = SupplierFormData.objects.all().order_by('-id')
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
            return SupplierFormData.objects.get(pk=pk)
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
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CurrencyMasterCreateView(APIView):
    def get(self, request):
        article = CurrencyMaster.objects.all().order_by('-id')
        serialzer = CurrencyMasterSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = CurrencyMasterSerializer(data=request.data)
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
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class CurrencyExchangeCreateView(APIView):
    def get(self, request):
        article = CurrencyExchange.objects.all().order_by('-id').filter(isDelete=False)
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
            Currency = CurrencyExchange.objects.get(pk=pk)
            print(Currency,"""--->>>""")
            return Currency
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
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


"""PaymentMode"""


class PaymentModeCreateView(APIView):
    def get(self, request):
        article = paymentMode.objects.all().order_by('-id')
        serialzer = PaymentModeSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = PaymentModeSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentModeDetails(APIView):
    def get_object(self, pk):
        try:
            return paymentMode.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = PaymentModeSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = PaymentModeSerializer(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
"""SalesOrder"""


class SalesOrderCreateView(APIView):
    def get(self, request):
        article = SalesOrder.objects.all().order_by('-id')
        serialzer = SalesOrderSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        print(request.data)
        serializer = SalesOrderSerializer(data=request.data)
        print(serializer.is_valid())
        print(serializer.errors)
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
        print(request.data)
        article = self.get_object(pk)
        serializer = SalesOrderSerializer(article, data=request.data)

        if serializer.is_valid():
            print(serializer.is_valid())
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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


class NumberingSeriesCreateView(APIView):

    def get(self, request):
        article = NumberingSeries.objects.all().order_by('-id').filter(isDelete=False)
        serialzer = NumberingSeriesSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        """In same resource, only one item allowed to be true. make others false"""
        for singleSeries in NumberingSeries.objects.all().filter(is_delete=False).filter(
                Resource=request.data['Resource']):
            if singleSeries.Resource == "Pos":
                if singleSeries.ReSourceIsPosType == "Sample":
                    if singleSeries.Default:
                        singleSeries.Default = False
                        singleSeries.save()
                elif singleSeries.ReSourceIsPosType == "Sales":
                    if singleSeries.Default:
                        singleSeries.Default = False
                        singleSeries.save()
        """after change send all data"""
        article = NumberingSeries.objects.all().order_by('-id').filter(is_delete=False)
        Change_Data = NumberingSeriesSerializer(article, many=True)
        serializer = NumberingSeriesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(Change_Data.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NumberingSeriesDetails(APIView):
    def get_object(self, pk):
        try:
            return NumberingSeries.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = NumberingSeriesSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = NumberingSeriesSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class FinishedGoodsCreateView(APIView):
    def get(self, request):
        article = FinishedGoods.objects.all().order_by('-id').filter(isDelete=False)
        print(article)
        serialzer = FinishedGoodsSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = FinishedGoodsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FinishedGoodsDetails(APIView):
    def get_object(self, pk):
        try:
            return FinishedGoods.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = FinishedGoodsSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = FinishedGoodsSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RawMaterialCreateView(APIView):
    def get(self, request):
        article = RawMaterial.objects.all().order_by('-id').filter(isDelete=False)
        serialzer = RawMaterialSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = RawMaterialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class RawMaterialDetails(APIView):
    def get_object(self, pk):
        try:
            return RawMaterial.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = RawMaterialSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = RawMaterialSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ScrapCreateView(APIView):
    def get(self, request):
        article = Scrap.objects.all().order_by('-id').filter(isDelete=False)
        serialzer = ScrapSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = ScrapSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ScrapDetails(APIView):
    def get_object(self, pk):
        try:
            return Scrap.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = ScrapSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ScrapSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RoutingCreateView(APIView):
    def get(self, request):
        article =  Routing.objects.all().order_by('-id').filter(isDelete=False)
        serialzer = RoutingSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = RoutingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BomCreateView(APIView):
    def get(self, request):
        article = Bom.objects.all().order_by('-id').filter(isDelete=False)
        serialzer = BomSerializer(article, many=True)
        return Response(serialzer.data)

    def post(self, request):
        serializer = BomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BomDetails(APIView):
    def get_object(self, pk):
        try:
            return Bom.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = BomSerializer(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = BomSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            article = self.get_object(pk)
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            print(e)
            error_message = "This data Linked with other modules"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            #         # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


"""stock statement part start"""


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
            filtered_data = [(int(stock_item['currentStock']), stock_item['store']) for stock_item in stock_data if
                             stock_item['part_no'] == part_no]
        else:
            filtered_data = [(int(stock_item['currentStock']), stock_item['store']) for stock_item in stock_data if
                             stock_item['part_no'] == part_no and int(stock_item['store']) == int(store_id)]
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
        filtered_master_items = [item for item in filtered_master_items if
                                 item['item_group'] == item_group_data[int(group_id)]]
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
    stock_data = list(ItemStock.objects.values('id', 'part_no', 'currentStock', 'store', 'BatchNumber', 'Serialnum'))
    is_serial = item_master_dict['serial']
    is_batch = item_master_dict['Batch_number']
    if store_id is None:
        filtered_data = [stock_item for stock_item in stock_data if stock_item['part_no'] == int(part_no)]
    else:
        filtered_data = [stock_item for stock_item in stock_data if
                         stock_item['part_no'] == int(part_no) and int(stock_item['store']) == int(store_id)]
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
        stockData = StockHistoryLog.objects.filter(PartNumber=int(part_id), ColumnName="currentStock",
                                                   StoreLink=int(store_id))

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


class getItemMasterHistory(APIView):
    def get_object(self, pk):
        try:
            return ItemMasterHistory.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = ItemMasterHistorySerializer(article)
        return Response(serialzer.data)


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
        except Exception as e:
            print(e)


def get_item_combo_(request):
    if request.method == 'GET':
        item_combo_ids = request.GET.getlist('ids', [])[0].split(',')
        item_combo_ids = [int(a) for a in item_combo_ids]
        filtered_objects = Item_Combo.objects.filter(id__in=item_combo_ids).values('id', 'part_number', 'Item_Qty',
                                                                                   'item_display', 'Is_Mandatory')
        # print(filtered_objects)
        if filtered_objects:
            # filtered_objects = serialize('json', filtered_objects)
            filtered_objects = list(filtered_objects.values())
        return JsonResponse(filtered_objects, safe=False)


def pos_report_data_filter(event_name, user, start_date, end_date):
    start_date_obj = datetime.strptime(start_date, "%d-%m-%Y")
    end_date_obj = datetime.strptime(end_date, "%d-%m-%Y")
    formatted_start_date = start_date_obj.strftime("%Y-%m-%d")
    formatted_end_date = end_date_obj.strftime("%Y-%m-%d")

    payment_prefetch = Prefetch('payments', queryset=paymentMode.objects.filter(
            UpdatedAt__gte=start_date,
            UpdatedAt__lte=end_date))
    if not event_name and not user:
        pos_with_payments = SalesOrder.objects.filter(
                marketingEvent__name=event_name,
                date__range=(start_date, end_date)
        ).prefetch_related(payment_prefetch)
    elif event_name and not user:
        pos_with_payments = SalesOrder.objects.filter(
            marketingEvent=event_name,
            order_date__gte=start_date,
            order_date__lte=end_date
        ).prefetch_related('payment').all()
    elif not event_name and user:
        pos_with_payments = SalesOrder.objects.filter(
            marketingEvent=event_name,
            order_date__gte=start_date,
            order_date__lte=end_date
        ).prefetch_related('payment').all()
    else:
        pos_with_payments = SalesOrder.objects.filter(
            marketingEvent=event_name,
            order_date__gte=start_date,
            order_date__lte=end_date
        ).prefetch_related('payment').all()

    print(pos_with_payments)
    instance_dict = model_to_dict(pos_with_payments[0])
    print(instance_dict)
    pass


def get_report_details(request):
    if request.method == 'GET':
        try:
            event_name = request.GET.get('eventname')
            user = request.GET.get('user')
            start_date = request.GET.get('startdate')
            end_date = request.GET.get('enddate')
            if event_name == 'null' or event_name == 'all':
                event_name = None
            if user == 'null' or user == 'all':
                user = None
            pos_report_data_filter(event_name, user, start_date, end_date)
            return JsonResponse([], safe=False)
        except Exception as e:
            print(e)
    pass