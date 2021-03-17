from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

def index(request):
    url = 'https://api.edamam.com/api/food-database/v2/parser'

# Create your views here.
class welcomeView(generic.DetailView):
    return HttpResponse("Temp")

class mainView(generic.DetailView):
    # picture displaying day's calories (circle updates according to amount eaten),
    # input box for calories eaten
    return HttpResponse("Temp")
