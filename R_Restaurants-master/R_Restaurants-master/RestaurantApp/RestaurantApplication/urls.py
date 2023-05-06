from django.urls import path

from .views import homePage

urlpatterns = [
    path('home', homePage, name='Home'),


]
