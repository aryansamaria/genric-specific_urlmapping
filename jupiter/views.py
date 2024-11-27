from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def position(request):
    return HttpResponse('<h1>Jupiter is the 5th planet from the sun</h1>')

def elements(request):
    return HttpResponse('<h1>The largest planet in our solar system, Jupiter is made up of trapped helium, hydrogen, and water.</h1>')
