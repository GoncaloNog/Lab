from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the index.")

def VIEWNAME(request):
    return HttpResponse("hei!")

def index(request):
    return render(request, 'sgrhapp/index.html')

def login_view(request):
    return render(request, 'sgrhapp/login.html')