#get urls to find 2 views
#get 2 vies to find 2 templates, 1 each

from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.welcomeView, name='welcomeView'),
    path('main/', views.mainView, name='mainView'),
    path('addFood/', views.addFood, name='addFood')
]
