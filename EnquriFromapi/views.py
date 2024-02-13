import os
import json

from django.db.models import ProtectedError
from django.http import HttpResponse, JsonResponse
from rest_framework.response import Response

from rest_framework.views import APIView
from .serializers import *
from rest_framework import viewsets, status
from django.core.mail import EmailMessage
from pathlib import Path
import requests

from django.contrib.auth.models import User

tenant_id = "2708cf11-c83a-466f-9399-671ebba3e8fc"
Client_ID = "52a3b712-cbab-461d-a03d-a6b234a9ed21"


def send_email(request, to, pdf_file_paths):
    subject = ''
    body = """Dear Sir/Madam,

It’s very nice meeting you at conference.

We, STAAN Biomed Engineering Private Limited was established in the year of 2003, as a leading manufacturer of Surgical Operating Tables, Surgical Operating Lights, Anesthesia Workstation, ICU Ventilators, HFNC (High Flow Nasal Cannula), Tourniquet, Surgical Instruments, Critical Care Devices. Our Organisation is an ISO 9001:2015 (Quality Management Systems & Requirements) & EN ISO 13485:2016 (Medical Devices – Quality Management Systems – Requirements) Certified Company.

Also, we do have recognition from world’s leading certification bodies like TUV SUD, ITC, ICR Polaska Co Ltd. And our Class I – Medical Devices are CE marked and US FDA registered. We are doing PAN India supply as a competitive manufacturer and exporter of Medical Devices.

We have successfully completed more than 550 Hospital projects directly and as well as through our dealer network, particularly in Orthopaedics, Gynaecology & Obsterics, Neuro, Vascular, Laparoscopy, Gastroenterology, Spine and General Surgery Operation Theatres and Intensive Care Units.

Please feel free to contact us for your requirements.

STAAN Biomed Engineering Private Limited

+91-98422 19018 | sales@staan.in | www.staan.in
T: +91-422 2533806 | +91-422 2531008 | +91-422 2537440"""
    To = [to]

    # Create an EmailMessage object
    email = EmailMessage(subject, body, 'marketing@staan.in', To)

    BASE_DIR = Path(__file__).resolve().parent.parent
    pdf_path = BASE_DIR / "PDF"

    # Attach multiple PDF files to the email
    for pdf_file_path in pdf_file_paths:
        try:
            # Normalize the path using os.path.join to handle backslashes
            normalized_path = os.path.join(pdf_path, pdf_file_path)

            with open(normalized_path, 'rb') as file:
                file_name = os.path.basename(pdf_file_path)  # Extract file name using os.path.basename
                print(normalized_path, "with base name")
                email.attach(file_name, file.read(), 'application/pdf')
        except Exception as e:
            print(f"Error attaching file {pdf_file_path}: {e}")

    # Send the email
    try:
        email.send()
        print("Email sent successfully.")
        print("--->>>5")
    except Exception as e:
        print(f"Error sending email: {e}")


"""To get user Data"""


def get_user_info(access_token):
    graph_api_url = 'https://graph.microsoft.com/v1.0/me'
    headers = {'Authorization': f'Bearer {access_token}'}

    response = requests.get(graph_api_url, headers=headers)

    if response.status_code == 200:
        user_info = response.json()
        print(user_info)
        return user_info
    else:
        # Handle error
        print(f"Error accessing Graph API: {response.status_code}, {response.text}")
        return None


"""Save user Details"""


def create_or_authenticate_user(user_info):
    user_id = user_info.get('id')
    username = user_info.get('displayName')
    email = user_info.get('userPrincipalName')

    existing_user = User.objects.filter(email=email).first()

    if existing_user:

        # User already exists, return the existing user
        return existing_user
    else:
        # User doesn't exist, create a new user
        new_user = User.objects.create_user(username=username, email=email)

        # You can set additional properties or perform other actions here
        return new_user


# Example usage in a Django view
"""To check User """


def checker(request):
    access_token = request.headers.get('Authorization').split('Bearer ')[1]
    user_info = get_user_info(access_token)

    if user_info:
        # Extract relevant information
        user = create_or_authenticate_user(user_info)
        response_data = {
            'id': user.id,
            'name': user.username,
            "email": user.email,
        }
        print(response_data)
        return JsonResponse(response_data, safe=False)

    else:
        return HttpResponse("access_token need to contect admin")


"""EnquiryApi get and post """


class EnquiryApi(APIView):

    def get(self, request):
        Enquiry = enquiryDatas.objects.all().order_by('-id')

        serializer_datas = EnquirySerializers(Enquiry, many=True)

        return Response(serializer_datas.data)

    def post(self, request):
        serializer = EnquirySerializers(data=request.data)
        print(serializer)
        print(serializer.is_valid())
        print(serializer.errors)

        if serializer.is_valid():
            serializer.save()

            email_value = serializer.validated_data.get('Email')
            intrested = serializer.validated_data.get('Interesteds')
            BASE_DIR = Path(__file__).resolve().parent.parent
            pdf_path = BASE_DIR / "PDF"
            intrested_list = []
            for data in (intrested):
                # print(pdf_path / str(data))
                data = str(data) + ".pdf"

                intrested_list.append(pdf_path / str(data))
            try:
                send_email(request, email_value, intrested_list)
            except Exception as e:
                print(e + ">>>>>")
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""EnquiryApi get and  and Put """


class EnquiryDetails(APIView):
    def get_object(self, pk):
        try:
            return enquiryDatas.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = EnquirySerializers(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = EnquirySerializers(article, data=request.data)
        print(serializer.is_valid())
        print(serializer)
        print(serializer.errors)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""productDetails get and post """


class productApi(APIView):
    def get(self, request):
        product_ = product.objects.all()
        print(product_)
        serializer_datas = productSerializers(product_, many=True)

        return Response(serializer_datas.data)

    def post(self, request):
        serializer = productSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""productDetails get and  put and delete """


class productDetails(APIView):
    def get_object(self, pk):
        try:
            return product.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = productSerializers(article)
        return Response(serialzer.data)


"""conferenceApi get and post """


class conferenceApi(APIView):
    def get(self, request):
        Conference_ = Conferencedata.objects.all().order_by('-id')
        # print(Conference_)
        serializer_datas = ConferenceSerializers(Conference_, many=True)

        return Response(serializer_datas.data)

    def post(self, request):
        serializer = ConferenceSerializers(data=request.data)
        print(serializer)
        print(serializer.is_valid())
        print(serializer.errors)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""conferenceDetails get and  put and delete """


class conferenceDetails(APIView):
    def get_object(self, pk):
        try:
            return Conferencedata.objects.get(pk=pk)
        except Exception as e:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, pk):
        article = self.get_object(pk)
        serialzer = ConferenceSerializers(article)
        return Response(serialzer.data)

    def put(self, request, pk):
        print(request)
        article = self.get_object(pk)
        serializer = ConferenceSerializers(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        try:
            article.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ProtectedError as e:
            # If the deletion is protected, handle the exception

            error_message = "This data Linked with other models"
            return Response({"error": error_message}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            # Handle other exceptions
            print(e)
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


"""user get"""


class passUser(APIView):
    def get(self, request):
        User_ = User.objects.all()
        serializer_datas = userSerializer(User_, many=True)

        return Response(serializer_datas.data)
