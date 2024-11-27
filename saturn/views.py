from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def position(request):
    return HttpResponse('<h1>Saturn is the 6th planet from the sun</h1>')

def elements(request):
    return HttpResponse('<h1>Saturn is not solid like Earth, but is instead a giant gas planet. It is made up of 94% hydrogen, 6% helium and small amounts of methane and ammonia.</h1>')
