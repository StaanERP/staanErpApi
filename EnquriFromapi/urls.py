"""
URL configuration for Staanenquiryfromwithazure project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from .views import *
urlpatterns = [
   path("user",checker),
   path('api/',  EnquiryApi.as_view()),
   path('api/<int:pk>',   EnquiryDetails.as_view()),
   path('api/product', productApi.as_view()),
   path('api/product/<int:pk>', productDetails.as_view()),
   path('api/Conference',  conferenceApi.as_view()),
   path('api/Conference/<int:pk>',  conferenceDetails.as_view()),
   path('api/user', passUser.as_view()),
]
