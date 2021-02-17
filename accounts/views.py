from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.http import HttpResponseRedirect

# Create your views here.


def login(request):
    context = {}
    if request.method == "POST":
        username = request.POST['user']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            dj_login(request, user)
            return HttpResponseRedirect(reverse('movements:movements'))
        else:
            context['error'] = 'Bad username or password.'

    return render(request, 'login.html')


def logout(request):
    dj_logout(request)
    return render(request, 'login.html')


def signUp(request):
    context = {}
    if request.method == "POST":
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user_name = request.POST['user']
        email = request.POST['email']
        if password == confirm_password:
            if User.objects.create_user(user_name, email, password):
                return HttpResponseRedirect(reverse('accounts:login'))
            else:
                context['error'] = "Could not create user account - Please try again"
        else:
            context['error'] = 'Passwords did not match. Please'
    return render(request, 'sign-up.html', context)
