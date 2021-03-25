from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#create models, user porfile that adds to user model, food model

class userProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    userName = models.CharField(max_length=200, null=True)
    userEmail = models.CharField(max_length=200, null=True)

    def __str__ (self):
        return str(self.userName)

class food(models.Model):
    foodName = models.CharField(max_length=200)
    calorie = models.DecimalField(max_digits=6, decimal_places=2, default=0, blank=True)
    quantity = models.IntegerField(default=1, null=True, blank=True)

    def __str__ (self):
        return str(self.foodName)

class userFood(models.Model):
    user = models.ManyToManyField(userProfile, blank=True)
    food = models.ManyToManyField(food)
