from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#function based views
def home(request):
    return HttpResponse('hello welcome to home')
