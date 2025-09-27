"""
URL configuration for booking_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from booking_app import views
from django.shortcuts import redirect


urlpatterns = [
    path("admin/", admin.site.urls),
    path("rooms/", views.room_list, name="room_list"),
    path("bookings/", views.booking_list, name="booking_list"),
    path("bookings/new/", views.create_booking, name="create_booking"),
    path("", views.room_list),  
]
