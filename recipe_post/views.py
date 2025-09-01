from django.http import HttpResponse

def home(request):
    return HttpResponse('Welcome to Recipe Post Home!')
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello, World!")
