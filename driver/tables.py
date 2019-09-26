import django_tables2 as tables
from django_tables2.utils import A
from django.utils.safestring import mark_safe
from driver import models


class TaxiTable(tables.Table):
    name = tables.LinkColumn('edit_taxi', args=[A('pk')])
    delete = tables.LinkColumn(
        'delete',
        args=['Taxi', A('pk')],
        text=mark_safe('<span class="delete-icon" uk-icon="trash"></span>'),
        orderable=False)

    class Meta:
        model = models.Taxi
        attrs = {'class': 'uk-table uk-table-striped uk-table-divider'}


class DriverTable(tables.Table):
    name = tables.LinkColumn('edit_driver', args=[A('pk')])
    delete = tables.LinkColumn(
        'delete',
        args=['Driver', A('pk')],
        text=mark_safe('<span class="delete-icon" uk-icon="trash"></span>'),
        orderable=False)

    class Meta:
        model = models.Driver
        attrs = {'class': 'uk-table uk-table-striped uk-table-divider'}

