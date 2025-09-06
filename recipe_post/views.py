from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from .models import RecipePost
from .forms import CommentForm


# Create your views here.
class RecipeHubList(generic.ListView):
    # query set order to be amended once separate vote method is created
    queryset = RecipePost.objects.order_by('-created_on').filter(status=1)
    template_name = 'index.html'
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
    queryset = (
        RecipePost.objects.filter(status=1)
        .prefetch_related('ingredients_rel', 'method_rel', 'comments')
    )
    post = get_object_or_404(queryset, slug=slug)

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

    context = {
        "post": post,
        "ingredients": post.ingredients_rel.order_by('order'),
        "steps": post.method_rel.order_by('order'),
        "comments": post.comments.all().order_by('-created_on'),
        "comment_count": post.comments.filter(approved=True).count(),
        "comment_form": comment_form,
    }

    return render(
        request,
        "recipe_post/recipe_page.html", context
    )
