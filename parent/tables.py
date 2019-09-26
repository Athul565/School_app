import django_tables2 as tables
from django_tables2.utils import A
from django.utils.safestring import mark_safe
from parent import models


class ParentTable(tables.Table):
    name = tables.LinkColumn('edit_parent', args=[A('pk')])
    delete = tables.LinkColumn(
        'parent_delete',
        args=['Parent', A('pk')],
        text=mark_safe('<span class="delete-icon" uk-icon="trash"></span>'),
        orderable=False)

    class Meta:
        model = models.Parent
        attrs = {'class': 'uk-table uk-table-striped uk-table-divider'}