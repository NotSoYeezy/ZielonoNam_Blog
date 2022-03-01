from django.urls import path
from .views import post_list_view, PostDetailView, post_create_view

app_name = 'Posts'

urlpatterns = [
    path('list/', post_list_view, name='post_list'),
    path('create/', post_create_view, name='post_create'),
    path('<slug:slug>/', PostDetailView.as_view(), name='post_detail'),
]
