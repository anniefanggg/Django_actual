from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.template import loader
# add my models
from .models import Food
from .models import UserProfile
from .models import UserFood

#class view might be better
# class indexView(View):
#     def get(self, request):
#         form = AuthenticateForm()
#         context = {
#         'form': form,
#         'user': request.user,
#         }
#         return render(request, )
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

def welcomeView(request):
    template = loader.get_template('CalorieCounter/welcomeView.html')
    return HttpResponse(template.render({}, request))

def mainView(request):
    template = loader.get_template('CalorieCounter/mainView.html')
    foods = Food.objects.all()
    total = UserFood.objects.all()

    # get data from view to template
    context = {
    "foods": foods,
    "total": total,
    }

    return HttpResponse(template.render(context, request))


def addFood(request):
    if request.method=="POST":
        form = addUserFood(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    form = addUserFood()
    return render(request, 'addUserFood.html')
