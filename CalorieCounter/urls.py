#get urls to find 2 views
#get 2 vies to find 2 templates, 1 each

from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.WelcomeView.as_view(), name='welcomeView'),
    path('main/', views.MainView.as_view(), name='mainView'),
    path('addFood/', views.AddFood.as_view(), name='addFood')
]
