from django.contrib import admin
from .models import UserProfile, Food, UserFood

# Register your models here.

#class foodAdmin(admin.ModelAdmin):
#    class Meta:
#        model = food
#    list_display=['name']
#    list_filter=['name']

admin.site.register(UserProfile)
admin.site.register(Food)
admin.site.register(UserFood)
