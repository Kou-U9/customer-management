from django.urls import path
from .views import ProductListView,ProductCreateView,ProductUpdateView,ProductDeleteView

app_name='products'

urlpatterns = [
    path('',ProductListView.as_view(), name='product_list'),
    path('create/', ProductCreateView.as_view(), name='product_create'),
    path('<int:pk>/update/',ProductUpdateView.as_view(),name='product_update'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(),name='product_delete'),
]
