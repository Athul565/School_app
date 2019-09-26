from django.urls import path
from driver import edit_views

urlpatterns = [
    path(
        "delete/<str:model>/<int:pk>",
        edit_views.delete,
        name="delete"
    ),
    path(
        "driver/<int:pk>/",
        edit_views.EditDriver.as_view(),
        name="edit_driver"
    ),
    path(
        "taxi/<int:pk>/",
        edit_views.EditTaxi.as_view(),
        name="edit_taxi"
    ),
]