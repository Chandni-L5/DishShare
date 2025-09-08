from . import views
from django.urls import path
from .views import RecipeHubPage


urlpatterns = [
    path("", RecipeHubPage.as_view(), name="recipe_hub"),
    path("<slug:slug>/", views.recipe_page, name="recipe_page"),
    path(
        "<slug:slug>/edit_comment/<int:comment_id>/",
        views.comment_edit,
        name="comment_edit",
    ),
    path(
        "<slug:slug>/delete_comment/<int:comment_id>",
        views.comment_delete,
        name="comment_delete"
    ),
]
