from django_filters import FilterSet, CharFilter
from driver import models
from django.contrib.auth.models import User

class TaxiFilter(FilterSet):

    class Meta:
        model = models.Taxi
        fields = {'name': ['icontains']}

class DriverFilter(FilterSet):

    class Meta:
        model = models.Driver
        fields = {'name': ['icontains']}
