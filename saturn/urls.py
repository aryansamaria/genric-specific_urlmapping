from django.urls import path
from saturn.views import *

urlpatterns=[
    path('position/',position,name='position'),
    path('elements/',elements,name='elements'),
]