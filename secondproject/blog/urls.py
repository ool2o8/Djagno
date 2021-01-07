from django.urls import path
import blog.views
urlpatterns=[
    path('', blog.views.home, name='home'),
    path('blog/<int:blog_id>', blog.views.detail,name='detail'),
    path('new/', blog.views.new, name='new'),
    path('create/', blog.views.create, name='create'),
]