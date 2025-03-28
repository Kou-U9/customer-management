from django.urls import path
from . import views

urlpatterns = [
    path("", views.list_2,name='customer_list'),
    # path('', views.customer_list, name='customer_list'),
    path('create/', views.customer_create, name='customer_create'),
    path('<int:pk>/edit/', views.customer_update, name='customer_update'),
    path('<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('export/csv',views.export_customers_csv, name='customer_export_csv'),
    path('import/', views.import_customers,name='customer_import'),
    path('export/pdf/',views.customer_export_pdf, name="customer_export_pdf"),
    path("customers/bulk_update/", views.customer_bulk_update, name="customer_bulk_update"),
    path("base/", views.base, name="base"),
]