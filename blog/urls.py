from django.urls import path
from .views import post_list, post_detail
urlpatterns = [
    path('list', post_list),
    path('detail', post_detail),
]