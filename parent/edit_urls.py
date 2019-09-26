from django.urls import path
from parent import edit_views

urlpatterns = [
    path(
        "parent_delete/<str:model>/<int:pk>",
        edit_views.delete,
        name="parent_delete"
    ),
    path(
        "parent/<int:pk>/",
        edit_views.EditParent.as_view(),
        name="edit_parent"
    )
]