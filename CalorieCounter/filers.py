import django_filters
from .models import *

class foodFilter(django_filters.FilterSet):
    class Meta:
        model = food
        fields = ['name']
