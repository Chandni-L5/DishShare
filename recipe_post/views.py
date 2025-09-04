from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import RecipePost
from .forms import CommentForm


# Create your views here.
class RecipeHubList(generic.ListView):
    # query set order to be amended once separate vote method is created
    queryset = RecipePost.objects.order_by('-created_on').filter(status=1)
    template_name = 'recipe_post/index.html'
    paginate_by = 6


def recipe_page(request, slug):
    """
    Displays an individual :model:'recipe_post.RecipePost'.

    **Context**
    ``post``
        An instance of :model:'recipe_post.RecipePost'.

    **Template**
    :template:`recipe_post/recipe_page.html`
    """
    queryset = RecipePost.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by('-created_on')
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                ('Your comment has been submitted successfully and is '
                 'awaiting approval.')
            )
    comment_form = CommentForm()

    ingredients_list = [i.strip() for i in post.ingredients.split(',')]
    return render(
        request,
        "recipe_post/recipe_page.html",
        {
            "post": post,
            "ingredients_list": ingredients_list,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        },
    )
