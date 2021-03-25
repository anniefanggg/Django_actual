from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from django.contrib.auth import authenticate, login, logout
from django.template import loader
# add my models
from .models import food
from .models import userProfile
from .models import userFood

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

food.objects.all
# Create your views here.
def welcomeView(request):
    template = loader.get_template('CalorieCounter/welcomeView.html')
    return HttpResponse(template.render({}, request))

def mainView(request):
    # picture displaying day's calories (circle updates according to amount eaten),
    # input box for calories eaten
    template = loader.get_template('CalorieCounter/mainView.html')
    return HttpResponse(template.render({}, request))
