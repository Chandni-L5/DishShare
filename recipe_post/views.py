from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import RecipePost, Comment
from .forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods


# Create your views here.
class RecipeHubList(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'recipepost_list'

    def get_queryset(self):
        qs = RecipePost.objects.filter(status=1)
        return qs.order_by('?')[:4]


class RecipeHubPage(generic.ListView):
    queryset = RecipePost.objects.order_by('-created_on').filter(status=1)
    template_name = 'recipe_post/recipe_hub.html'
    context_object_name = 'recipepost_list'


def recipe_page(request, slug):
    """
    Displays an individual :model:'recipe_post.RecipePost'.
    **Context**
    ``post``
        An instance of :model:'recipe_post.RecipePost'.

    **Template**
    :template:`recipe_post/recipe_page.html`
    """
    post = get_object_or_404(RecipePost, slug=slug)
    is_author = request.user.is_authenticated and request.user == post.author

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.recipe = post
            comment.save()
            messages.success(
                request,
                ('Your comment has been submitted successfully and is '
                 'awaiting approval.')
            )
            return redirect('recipe_page', slug=post.slug)
    else:
        comment_form = CommentForm()

    comment_qs = (
        post.comments.all()
        if is_author else post.comments.filter(approved=True)
    ).order_by('-created_on')

    context = {
        "post": post,
        "ingredients": post.ingredients_rel.order_by('order'),
        "steps": post.method_rel.order_by('order'),
        "comments": comment_qs,
        "comment_count": comment_qs.count(),
        "comment_form": comment_form,
        "is_author": is_author
    }

    return render(
        request,
        "recipe_post/recipe_page.html", context
    )


@login_required
@require_http_methods(["POST", "GET"])
def comment_edit(request, slug, comment_id):
    """
    view to edit a comment made by a user on a recipe post.
    """
    post = get_object_or_404(RecipePost, slug=slug)
    comment = get_object_or_404(
        Comment, id=comment_id, recipe=post, author=request.user
    )

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            updated = form.save(commit=False)
            updated.recipe = post
            updated.approved = False
            updated.save()
            messages.success(request, "Your comment has been updated!")
        else:
            messages.error(
                request,
                "There was an error updating your comment. Please try again."
            )
    return redirect('recipe_page', slug=post.slug)


@login_required
@require_http_methods(["GET"])
def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    post = get_object_or_404(RecipePost, slug=slug)
    comment = get_object_or_404(
        Comment, id=comment_id, recipe=post, author=request.user
    )

    comment.delete()
    messages.success(request, "Comment deleted!")
    return redirect("recipe_page", slug=slug)
