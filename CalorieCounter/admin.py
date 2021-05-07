from django.contrib import admin
from .models import UserProfile, Food, UserFood
from django.contrib.auth.models import User

# user = User.objects.create_user('john', 'john@gmail.com', 'johnpassword')

# Register your models here.

admin.site.register(UserProfile)
admin.site.register(Food)
admin.site.register(UserFood)
