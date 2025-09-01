from django.shortcuts import render
from django.views import generic
from .models import RecipePost


# Create your views here.
class RecipePostList(generic.ListView):
    # query set order to be amended once separate vote method is created
    queryset = RecipePost.objects.order_by('-created_on')
    template_name = 'recipe_post/recipe_hub.html'
