from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def position(request):
    return HttpResponse('<h1>Venus is the 2nd planet from the sun</h1>')

def elements(request):
    return HttpResponse('<h1>Venus is made up of a rocky mantle, a central iron core, and a thick atmosphere</h1>')
