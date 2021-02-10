from django.urls import path
from .views import post_list, post_detail
urlpatterns = [
    path('list/', post_list, name='list'),
    path('detail/', post_detail, name='detail'),
]