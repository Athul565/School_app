from django.urls import path, include
from driver import views


urlpatterns = [
    path(
        "auto-complete/",
        include("driver.auto_complete_urls")
    ),
    path(
        "edit/",
        include("driver.edit_urls")
    ),
    path('driver/', views.DriverView.as_view(), name='driver'),
    path('taxi/', views.TaxiView.as_view(), name='taxi')
]