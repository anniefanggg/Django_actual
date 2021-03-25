from django.contrib import admin
from .models import userProfile, food, userFood

# Register your models here.

#class foodAdmin(admin.ModelAdmin):
#    class Meta:
#        model = food
#    list_display=['name']
#    list_filter=['name']

admin.site.register(userProfile)
admin.site.register(food)
admin.site.register(userFood)
