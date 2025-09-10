from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.db import transaction
from .forms import (
    IngredientsFormSetEdit,
    RecipePostForm,
    IngredientsFormSetCreate,
    MethodFormSetEdit,
    MethodFormSetCreate,
)
from recipe_post.models import RecipePost
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.decorators.http import require_POST


@login_required
def submit_recipe(request):
    """
    View to handle the submission of a new recipe by a logged-in user.
    """
    parent = RecipePost(author=request.user)
    if request.method == "POST":
        form = RecipePostForm(request.POST, request.FILES, instance=parent)
        ing_formset = IngredientsFormSetCreate(
            request.POST or None, prefix="ing", instance=parent
        )
        step_formset = MethodFormSetCreate(
            request.POST or None, prefix="step", instance=parent
        )
        if (
            form.is_valid()
            and ing_formset.is_valid()
            and step_formset.is_valid()
        ):
            from django.utils.text import slugify

            with transaction.atomic():
                recipe = form.save(commit=False)
                recipe.author = request.user
                # Generates a unique slug from the title
                base_slug = slugify(recipe.title)
                slug = base_slug
                counter = 1
                while RecipePost.objects.filter(slug=slug).exists():
                    slug = f"{base_slug}-{counter}"
                    counter += 1
                recipe.slug = slug
                recipe.save()
                ing_formset.instance = recipe
                step_formset.instance = recipe
                ing_formset.save()
                step_formset.save()
            messages.success(
                request,
                "Your recipe was submitted for moderation successfully!"
            )
            return redirect("my_submissions")
    else:
        form = RecipePostForm(instance=parent)
        ing_formset = IngredientsFormSetCreate(prefix="ing", instance=parent)
        step_formset = MethodFormSetCreate(prefix="step", instance=parent)
    return render(
        request,
        "submissions/submit_recipe.html",
        {
            "form": form,
            "ing_formset": ing_formset,
            "step_formset": step_formset,
            "object": None,
        },
    )


@login_required
def recipe_edit(request, slug):
    """
    View to handle editing an existing recipe by its author, including
    ingredients and method steps via inline formsets.
    """
    post = get_object_or_404(
        RecipePost, slug=slug, author=request.user
    )
    if request.method == "POST":
        form = RecipePostForm(request.POST, request.FILES, instance=post)
        ing_formset = IngredientsFormSetEdit(
            request.POST, prefix="ing", instance=post
        )
        step_formset = MethodFormSetEdit(
            request.POST, prefix="step", instance=post
        )
        if (
            form.is_valid()
            and ing_formset.is_valid()
            and step_formset.is_valid()
        ):
            with transaction.atomic():
                form.save()
                ing_formset.save()
                step_formset.save()
            messages.success(request, "Your recipe has been updated!")
            return redirect("recipe_page", slug=post.slug)

    else:
        form = RecipePostForm(instance=post)
        ing_formset = IngredientsFormSetEdit(
            request.POST or None, prefix="ing", instance=post
        )
        step_formset = MethodFormSetEdit(
            request.POST or None, prefix="step", instance=post
        )
    return render(
        request,
        "submissions/submit_recipe.html",
        {
            "form": form,
            "ing_formset": ing_formset,
            "step_formset": step_formset,
            "object": post,
        },
    )


@login_required
@require_POST
def recipe_delete(request, slug):
    """
    View to handle deleting an existing recipe by its author.
    """
    recipe = get_object_or_404(RecipePost, slug=slug, author=request.user)
    recipe.delete()
    messages.success(request, "Your recipe has been deleted!")
    return redirect("my_submissions")


class MySubmissions(LoginRequiredMixin, ListView):
    """
    View to display the list of recipes submitted by the logged-in user.
    """

    model = RecipePost
    template_name = "submissions/my_submissions.html"
    context_object_name = "recipes"

    def get_queryset(self):
        """
        Returns the queryset of recipes submitted by the logged-in user,
        optionally filtered by status (published or draft).
        """
        submitted_recipes = RecipePost.objects.filter(
            author=self.request.user
        ).order_by("-created_on")
        status = self.request.GET.get("status")
        if status == "published":
            submitted_recipes = submitted_recipes.filter(status=1)
        elif status == "draft":
            submitted_recipes = submitted_recipes.filter(status=0)
        return submitted_recipes.select_related("author")

    def get_context_data(self, **kwargs):
        """
        Adds additional context data for the template, including counts of
        all, published, and draft recipes.
        """
        context = super().get_context_data(**kwargs)
        base = RecipePost.objects.filter(author=self.request.user)
        context["counts"] = {
            "all": base.count(),
            "published": base.filter(status=1).count(),
            "draft": base.filter(status=0).count(),
        }
        context["selected_status"] = self.request.GET.get("status")
        return context
