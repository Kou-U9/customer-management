from django.urls import path
from . import views

urlpatterns = [
    path('', views.sale_list, name='sale_list'),
    path('<int:pk>/', views.sale_detail, name='sale_detail'),
    path('create/',views.sale_create,name='sale_create'),
    path('<int:pk>/delete/', views.sale_delete,name='sale_delete'),
]
