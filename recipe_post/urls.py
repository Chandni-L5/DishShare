from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeHubList.as_view(), name='recipe-hub'),
]
