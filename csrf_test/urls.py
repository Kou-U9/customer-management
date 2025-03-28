from django.urls import path
from .views import post_comment,comment_list

urlpatterns = [
     path('comment/', post_comment, name='post_comment'),
     path('comments/', comment_list, name='comment_list'),
]
