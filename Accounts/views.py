import re
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import UserRegisterForm, UserChangePasswordForm


class UserLoginView(View):
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        user = authenticate(request=request ,username=username, password=password)

        if user is not None:
            if user.is_active:
                login(request=request, user=user)
                return HttpResponseRedirect(reverse('index'))
            else:
                messages.error(request, "Użytkownik nieaktywny")
                return render(request, 'accounts/login.html')
        else:
            messages.error(request, "Złe hasło lub nazwa użytkownika")
            return render(request, 'accounts/login.html', {})


    def get(self, request):
        return render(request, 'accounts/login.html', {})


class LogOutView(View, LoginRequiredMixin):
    login_url = '/user/login'

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse('index'))


def user_register_view(request):
    user_form = UserRegisterForm()

    if request.method == 'POST':
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return HttpResponseRedirect(reverse('accounts:login'))
        else:
            messages.info(request, user_form.errors)

    return render(request, 'accounts/register.html', {'form': user_form})


@login_required
def change_password_view(request):
    if request.method == 'POST':
        form = UserChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return HttpResponseRedirect(reverse('accounts:login')) 
        else:
            messages.info(request, form.errors)
    else:
        form = UserChangePasswordForm(request.user)

    return render(request, 'accounts/change_password.html', {'form': form})






