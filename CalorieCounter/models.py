from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#create models, user profile that adds to user model, food model

class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    userName = models.CharField(max_length=200, null=True)
    userEmail = models.CharField(max_length=200, null=True)
    userPassword = models.CharField(max_length=200, null=True)

    def __str__ (self):
        return str(self.userName)

class Food(models.Model):
    foodName = models.CharField(max_length=200)
    calorie = models.DecimalField(max_digits=6, decimal_places=2, default=0, blank=True)
    servingSize = models.IntegerField()
    servingSizeUnits = models.CharField(max_length=20)
    def __str__ (self):
        return str(self.foodName)

class UserFood(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, null=True, blank=True)
    def __str__ (self):
        return str(self.food) + " " + str(self.user)
