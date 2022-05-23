from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from wndrland_app.views import *

urlpatterns = [
    path('', home, name='home'),
    path('about', about, name='about'),
    path('vision', vision, name='vision'),
    path('contact', contact, name='contact'),


]