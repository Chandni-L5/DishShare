from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import RecipePost, Comment
from .forms import CommentForm


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
    queryset = (
        RecipePost.objects.filter(status=1)
        .prefetch_related('ingredients_rel', 'method_rel', 'comments')
    )
    post = get_object_or_404(queryset, slug=slug, status=1)
    comment = post.comments.filter(approved=True)
    is_author = request.user.is_authenticated and request.user == post.author

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
        "is_author": is_author
    }

    return render(
        request,
        "recipe_post/recipe_page.html", context
    )


def comment_edit(request, slug, comment_id):
    """
    view to edit a comment made by a user on a recipe post.
    """
    if request.method == "POST":
        queryset = RecipePost.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, id=comment_id, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)
        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                ('Comment Updated!')
            )
        else:
            messages.add_message(
                request, messages.ERROR,
                ('Error updating comment.')
            )
    return HttpResponseRedirect(reverse('recipe_page', args=[slug]))


def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    post = get_object_or_404(RecipePost, status=1, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id, recipe=post)

    comment.delete()
    messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    return HttpResponseRedirect(reverse('recipe_page', args=[slug]))
