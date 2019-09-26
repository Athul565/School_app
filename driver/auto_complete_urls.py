from django.urls import path
from driver import auto_complete

urlpatterns = [
    path('taxi/', auto_complete.TaxiAutoComplete.as_view(), name='taxi_autocomplete')
]