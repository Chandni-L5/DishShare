from django.shortcuts import render
from django.views import generic
from .models import RecipePost


# Create your views here.
class RecipeHubList(generic.ListView):
    # query set order to be amended once separate vote method is created
    queryset = RecipePost.objects.order_by('-created_on').filter(status=1)
    template_name = 'recipe_post/index.html'
    paginate_by = 6
