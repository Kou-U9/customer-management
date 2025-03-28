from django.urls import path
from .views import session_list,login_view, logout_view,sign_up

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('sign-up/', sign_up, name='sign_up'),
    path('session_list/', session_list, name='session_list'),
]
