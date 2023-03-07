from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def see(request):
    return HttpResponse('<marquee>This is done in class</marquee>')