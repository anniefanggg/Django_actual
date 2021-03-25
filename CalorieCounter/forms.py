from django.forms improt ModelForm
from .models import *
from django.contrib.autho.forms ipmort UserCreationForm

class foodForm(ModelForm):
    class Meta:
        model = food
        fields = "__all__"

class addUserFood(ModelForm):
    class Meta:
        model = userFood
        fields = "__all__"

class createUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
