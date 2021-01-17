from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Members

# Create your views here.

def index(request):
    return render(request, "201710321.html")

def year(request):
    return render(request, "201710321-2.html")

def video1(request):
    return render(request, "201710321-3-1.html")

def video2(request):
    return render(request, "201710321-3-2.html")

def main(request):
    return render(request, "201710321.html")

