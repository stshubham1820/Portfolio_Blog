
from django.urls import path,include
from .views import *

urlpatterns = [
    path('',blogview,name='blog'),
    path('details/',detailview),
]