from django.shortcuts import render
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
#
# def index(request):
#     if request.POST:
#         if 'inputUsername' in request.POST.keys():
#             user = authenticate(username=request.POST['inputUsername']),
#             password = request.POST['inputPassword']),
#             if user is not None:
#                 login(request, user)
#             else:
#                 pass
#         elif 'logout' in request.POST.keys():
#             logout(request)
#
#     loggedIn = request.user.is_authenticated
# Create your views here.

class WelcomeView(View):
    def get(self, request):
        if request.POST:
            if 'inputUsername' in request.POST.keys():
                user = authenticate(username=request.POST['inputUsername'],
                    password=request.POST['inputPassword'])
                if user is not None:
                    login(request, user)
                else:
                    pass
            elif 'logout' in request.POST.keys():
                logout(request)
        if request.user.is_aunthenticated:
            loggedIn = True
        else:
            loggedIn = False
        template = loader.get_template('CalorieCounter/welcomeView.html')
        allUserProfiles = UserProfile.objects.all()
        for UserProfile in allUserProfiles:
            userProfile.firstName = UserProfile.first_name

        context = {
        'allUserProfiles': allUserProfiles,
        'loggedIn': loggedIn,
        'userProfile': request.user,
        }
        return HttpResponse(template.render({}, request))
    def post(self, request):
        pass

class MainView(View):
    def get(self, request):
        template = loader.get_template('CalorieCounter/mainView.html')
        foods = Food.objects.all()
        total = UserFood.objects.all()

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
