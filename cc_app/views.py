from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return render(request, 'cc_app/index.html')


def sign_up(request):
    return render(request, 'cc_app/signup.html')
