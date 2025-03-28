from django.urls import path

from .views import OrderListView, OrderCreateView, OrderUpdateView, OrderDeleteView,OrderPdfView

app_name = 'orders'

urlpatterns = [
    path('',OrderListView.as_view(),name= 'order_list'),
    path('new/', OrderCreateView.as_view(), name = 'order_create'),
    path('<int:pk>/edit/', OrderUpdateView.as_view(), name = 'order_edit'),
    path('<int:pk>/delete/', OrderDeleteView.as_view(), name = 'order_delete'),
    path('<int:pk>/pdf/', OrderPdfView.as_view(),name='order_pdf'),
]
