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
    """
        Parameters: None
        Return: None
        Purpose: The purpose of this class is to authenticate the user with their username
        and password. If they are not logged in, a message will notify them. If they
        are successfuly authenticated, the user will be sent to the main page.
    """
    # Check if user is already logged in
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('mainView')
        else:
            template = loader.get_template('CalorieCounter/welcomeView.html')
            return HttpResponse(template.render({}, request))
    # Check if username and password are correct to authenticate
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
        template = loader.get_template('CalorieCounter/mainView.html')
        context = {
        'user': request.user,
        }
        return HttpResponse(template.render(context, request))

class MainView(View):
    """
        Parameters: None
        Return: None
        Purpose: The purpose of this class is to display the user's information, such
        as their username, the foods they've eaten, and the quantities of said foods.
        It will also display the total list of foods they may select from. A button
        will allow them to go to the page for adding additional foods, and they will
        also be able to log out.
    """
    def get(self, request):
        template = loader.get_template('CalorieCounter/mainView.html')
        foods = Food.objects.all()
        total_temp = UserFood.objects.all()
        total = []
        totalCalories = 0
        # Create dictionary to store info about user's food
        for item_temp in total_temp:
            item = {}
            item["food"] = item_temp.food.foodName
            item["user"] = item_temp.user.username
            item["quantity"] = item_temp.quantity
            food = Food.objects.get(foodName = item["food"])
            calorie = food.calorie
            item["calorie"] = calorie
            totalCalories += (calorie * item["quantity"])
            item["totalCalories"] = totalCalories
            total.append(item)
        print (total)


        # Get data from view to template
        context = {
        "foods": foods,
        "total": total,
        }

        return HttpResponse(template.render(context, request))

class AddFood(View):
    """
        Parameters: None
        Return: None
        Purpose: The purpose of this class is to allow the user to select foods and
        their quantites. Upon submitting the information, they will be sent back
        to the main page.
    """
    def get(self, request):
        form = addUserFood(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        form = addUserFood()
        return render(request, 'CalorieCounter/addFoodView.html')
    def post(self, request):
        # Get food as a class object
        food = Food.objects.get(foodName = request.POST['Food'])
        userFood = UserFood(
            user = request.user,
            food = food,
            quantity = request.POST['Quantity'],
        )
        userFood.save()
        print (userFood.__dict__)
        return redirect('mainView')

def LogoutView(request):
    # Allow user to log out
    logout(request)
    return render(request, 'CalorieCounter/logoutView.html')
