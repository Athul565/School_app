from dal import autocomplete
from parent import models

class ParentAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = models.Parent.objects.all().order_by('name')

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs