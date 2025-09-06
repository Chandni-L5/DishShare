from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import RecipePostForm


@login_required
def submit_recipe(request):
    if request.method == "POST":
        form = RecipePostForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            messages.success(request, "Your recipe was submitted successfully!")
            return redirect("submit_recipe")
    else:
        form = RecipePostForm()

    return render(request, "submissions/submit_recipe.html", {"form": form})
