from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.template import loader
# add my models
from .models import Food
from .models import UserProfile
from .models import UserFood

from .forms import addUserFood

class WelcomeView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('mainView')
        else:
            template = loader.get_template('CalorieCounter/welcomeView.html')
            return HttpResponse(template.render({}, request))
    def post(self, request):
        if 'username' in request.POST.keys():
            user = authenticate(username=request.POST['username'],
                password=request.POST['password'])
            if user is not None:
                login(request, user)
            else:
                pass
        if request.user.is_authenticated:
            return redirect('mainView')
        if 'logout' in request.POST.keys():
            logout(request)
        template = loader.get_template('CalorieCounter/welcomeView.html')
        context = {
        'user': request.user,
        }
        return HttpResponse(template.render(context, request))

class MainView(View):
    def get(self, request):
        template = loader.get_template('CalorieCounter/mainView.html')
        foods = Food.objects.all()
        total_temp = UserFood.objects.all()
        total = []

        for item_temp in total_temp:
            item = {}
            item["food"] = item_temp.food.foodName
            item["user"] = item_temp.user.username
            item["quantity"] = item_temp.quantity
            total.append(item)

        print (total)

        # get data from view to template
        context = {
        "foods": foods,
        "total": total,
        }

        return HttpResponse(template.render(context, request))

class AddFood(View):
    def get(self, request):
        form = addUserFood(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        form = addUserFood()
        return render(request, 'CalorieCounter/addFoodView.html')
    def post(self, request):
        userFood = UserFood(
            user = request.user,
            food = request.POST['Food'],
            quantity = request.POST['Quantity'],
        )
        userFood.save()
