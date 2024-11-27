from django.urls import path
from jupiter.views import *

urlpatterns=[
    path('position/',position,name='position'),
    path('elements/',elements,name='elements'),
]