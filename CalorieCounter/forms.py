from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm

class foodForm(ModelForm):
    class Meta:
        model = Food
        fields = "__all__"

class addUserFood(ModelForm):
    class Meta:
        model = UserFood
        fields = "__all__"

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
