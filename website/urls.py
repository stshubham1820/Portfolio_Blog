from django.contrib import admin
from django.urls import path,include
from .views import *
from users.views import *
urlpatterns = [
    path('',home),
    path('about/',about),
    path('services/',service),
    path('contact/',contact),
    path('accounts/login/',loginview ),
    path('accounts/', include('allauth.urls')),
]
