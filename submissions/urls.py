
from django.urls import path
from .views import submit_recipe

urlpatterns = [
    path('', submit_recipe, name='submit_recipe'),
]
