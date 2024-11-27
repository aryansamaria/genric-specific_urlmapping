from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def position(request):
    return HttpResponse('<h1>Earth is the 3rd planet from the sun</h1>')

def elements(request):
    return HttpResponse('<h1>The most abundant element on Earth is oxygen, but it also contains nitrogen, phosphorus, hydrogen, aluminum, iron, and calcium.</h1>')
