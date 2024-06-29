# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth import authenticate, login as auth_login, logout
from .models import User
# from .forms import RoomForm, UserForm, MyUserCreationForm

# Create your views here.
def home(request):
    return render(request, 'compfest/home.html')

def review(request):
    return render(request, 'compfest/review.html')

def book_reservation(request):
    return render(request, 'compfest/book_reservation.html')

def login_view(request):
    page = 'login'
    if request.user.is_authenticated:
        print("user is authenticated. redirecting to home")
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email = email)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, email = email, password = password)
        print(f"user: {user}")

        if user is not None:
            print("user is not none. doing login now")
            auth_login(request, user)
            print("login success. redirecting to home")
            return redirect('home')
        else:
            messages.error(request, 'Username or password does not exist')

    context = {'page': page}
    return render(request, 'compfest/login.html', context)

def logout_user(request):
    logout(request)
    return redirect('login')