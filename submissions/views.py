from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db import transaction
from .forms import RecipePostForm, IngredientsFormSet, MethodFormSet
from recipe_post.models import RecipePost


@login_required
def submit_recipe(request):
    """
    View to handle the submission of a new recipe by a logged-in user.
    """
    parent = RecipePost(author=request.user)
    if request.method == "POST":
        form = RecipePostForm(request.POST, request.FILES, instance=parent)
        ing_formset = IngredientsFormSet(
            request.POST, prefix="ing",  instance=parent
        )
        step_formset = MethodFormSet(
            request.POST, prefix="step", instance=parent
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
            return redirect("submit_recipe")
    else:
        form = RecipePostForm(instance=parent)
        ing_formset = IngredientsFormSet(prefix="ing", instance=parent)
        step_formset = MethodFormSet(prefix="step", instance=parent)
    return render(request, "submissions/submit_recipe.html", {
        "form": form,
        "ing_formset": ing_formset,
        "step_formset": step_formset,
    })
