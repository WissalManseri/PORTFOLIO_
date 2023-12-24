from django.urls import path
from .views import *

urlpatterns = [
    path('', resume, name='index'),
    path('contact/', contact_form, name='contact_form'),



    # Add more URL patterns as needed
]
