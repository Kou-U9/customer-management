from django.urls import path
from xss_app.views import unsafe_xss_view

urlpatterns = [
    path("unsafe/", unsafe_xss_view, name="unsafe_xss")
]
