from django.urls import path
from .views import base,index

urlpatterns = [
    path('base/',base, name='base'),
    path('index/',index, name='index'),
]
