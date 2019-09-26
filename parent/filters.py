from parent import models
from django_filters import FilterSet, CharFilter
class ParentFilter(FilterSet):

    class Meta:
        model = models.Parent
        fields = {'name': ['icontains']}