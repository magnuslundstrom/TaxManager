from accounts.models import PasswordResetRequest
from django.shortcuts import render, reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
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


def resetPassword(request):
    if request.method == "POST":
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        token = request.POST['token']

        if password == confirmPassword:
            try:
                prr = PasswordResetRequest.objects.get(token=token)
            except:
                print("invalid password reset attempt")
                return render(request, 'reset-password.html')
            try:
                user = prr.user
                user.set_password(password)
                user.save()
            except:
                print("something went wrong")
            return HttpResponseRedirect(reverse('accounts:login'))

    return render(request, 'reset-password.html')


def requestResetPassword(request):
    if request.method == "POST":
        userName = request.POST['username']
        user = None

        if userName:
            try:
                user = User.objects.get(username=userName)
            except:
                print(f"Invalid password request: {userName}")

        if user:
            prr = PasswordResetRequest()
            prr.user = user
            prr.save()
            print(prr)
            return HttpResponseRedirect(reverse('accounts:resetPassword'))

    return render(request, 'reset-password-request.html')
