from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeHubList.as_view(), name='home'),
    path('<slug:slug>/', views.recipe_page, name='recipe_page')
]
