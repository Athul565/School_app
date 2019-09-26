from django_filters import FilterSet, CharFilter
from home import models

class StudentFilter(FilterSet):

    class Meta:
        model = models.Students
        fields = {'name': ['icontains']}