from django.urls import path, include
from parent import views


urlpatterns = [
    path(
        "auto-complete/",
        include("parent.auto_complete_urls")
    ),
    path(
        "edit/",
        include("parent.edit_urls")
    ),
    path('parent/', views.ParentView.as_view(), name='parent')
]
