from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'user/index.html')

def login_view(request):
    return render(request, 'user/login.html')

def cadastro(request):
    return render(request, 'user/cadastro.html')
