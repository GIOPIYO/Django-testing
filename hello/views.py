
from django.utils.timezone import datetime
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, "hello/home.html")

def about(request):
    return render(request, "hello/about.html")

def contact(request):
    return render(request, "hello/contact.html")

def catalog(request):
    return render(request, "hello/catalog.html")

def catalog1(request):
    return render(request, "hello/catalog1.html")

def prodDetails(request):
    return render(request, "hello/prodDetails.html")

def search(request):
    return render(request, "hello/search.html")