from django.urls import path
from . import views

urlpatterns = [
    path("recipe/new/", views.submit_recipe, name="submit_recipe"),
    path("recipe/<slug:slug>/edit/", views.recipe_edit, name="recipe_edit"),
    path(
        "recipe/<slug:slug>/delete/", views.recipe_delete, name="recipe_delete"
    ),
    path(
        "my-submissions/", views.MySubmissions.as_view(), name="my_submissions"
    ),
    path("recipe/<slug:slug>/edit/", views.recipe_edit, name="recipe_edit"),
    path(
        "recipe/<slug:slug>/delete/", views.recipe_delete, name="recipe_delete"
    ),
]
