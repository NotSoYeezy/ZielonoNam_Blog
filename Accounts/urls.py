from unicodedata import name
from django.urls import path
from .views import UserLoginView, LogOutView, user_register_view, change_password_view

app_name = 'accounts'

urlpatterns = [
    path('login/', UserLoginView.as_view() , name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('register/', user_register_view, name='register'),
    path('change_password/', change_password_view, name='pass_change'),
]