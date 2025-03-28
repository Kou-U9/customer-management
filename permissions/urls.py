from django.urls import path

from .views import permissioin_list,permission_edit,no_permission

app_name = 'permissions'

urlpatterns = [
    path('',permissioin_list,name='permission_list'),
    path('edit/<int:pk>/', permission_edit, name='permission_edit'),
    path('new/', permission_edit, name='permission_new'),
    path('no-permission/', no_permission, name='no_permission')
]

