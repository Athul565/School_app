from django.views import View
from dal import autocomplete
from driver import models


class RelatedFieldWidgetCanAdd(autocomplete.ModelSelect2):

    def __init__(self, related_model, related_url=None, *args, **kw):

        super(RelatedFieldWidgetCanAdd, self).__init__(*args, **kw)
        self.custom_url = False
        if not related_url:
            related_url = '/{0}/?add'.format(related_model.__name__.lower())
            self.custom_url = True

        # Be careful that here "reverse" is not allowed
        self.related_url = related_url


class MultipleRelatedFieldWidgetCanAdd(autocomplete.ModelSelect2Multiple):

    def __init__(self, related_model, related_url=None, *args, **kw):

        super(MultipleRelatedFieldWidgetCanAdd, self).__init__(*args, **kw)
        self.custom_url = False
        if not related_url:
            related_url = '/{0}/?add'.format(related_model.__name__.lower())
            self.custom_url = True

        # Be careful that here "reverse" is not allowed
        self.related_url = related_url


class TaxiAutoComplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = models.Taxi.objects.all().order_by('name')

        if self.q:
            qs = qs.filter(name__istartswith=self.q)
        return qs