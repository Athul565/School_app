from django.urls import path
from parent import auto_complete

urlpatterns = [
    path('parent/', auto_complete.ParentAutoComplete.as_view(), name='parent_autocomplete')
]