from django.db import models
from django.contrib.autho.models import User

# Create your models here.

#create models, user porfile that adds to user model, food model

class userProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    userName = models.CharField(null=True)
    userEmail = models.CharField(null=True)

    def __str__ (self):
        return str(self.userName)

class Food(models.Model):
    foodName = models.CharField()
    calorie = models.DecimalField(default=0)
    quantity = models.IntegerField(default=1, null=True, blank=True)

    def __str__ (self):
        return str(self.foodName)

class userFood(models.Model):
    user = models.ManyToManyField(Customer, blank=True)
    food = models.ManyToManyField(Food)
