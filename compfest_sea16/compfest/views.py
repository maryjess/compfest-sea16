# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'compfest/home.html')

def review(request):
    return render(request, 'compfest/review.html')

def book_reservation(request):
    return render(request, 'compfest/book_reservation.html')
