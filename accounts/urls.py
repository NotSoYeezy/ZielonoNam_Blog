from unicodedata import name
from django.urls import path, reverse_lazy
from .views import UserLoginView, LogOutView, user_register_view, change_password_view
from django.contrib.auth import views as auth_views
from .forms import UserPasswordResetForm

app_name = 'accounts'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('register/', user_register_view, name='register'),
    path('change_password/', change_password_view, name='pass_change'),

    # Password reset views
    path('password_reset/', auth_views.PasswordResetView.as_view(
        success_url=reverse_lazy('accounts:password_reset_done'), form_class=UserPasswordResetForm),
         name='password_reset'),

    path('password/reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy("accounts:password_reset_complete")), name='password_reset_confirm'),

    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]