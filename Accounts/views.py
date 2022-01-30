from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from django.http import HttpResponseRedirect


class UserLoginView(View):
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                login(user)
                return HttpResponseRedirect('index')
            else:
                return render(request, 'accounts/login.html', {})
        else:
            return render(request, 'accounts/login.html', {})


    def get(self, request):
        return render(request, 'accounts/login.html', {})
