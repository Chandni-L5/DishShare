from django.contrib import admin
from .models import RecipePost, Comment, Ingredients, Method
from allauth.account.models import EmailAddress


class IngredientsInline(admin.TabularInline):
    model = Ingredients
    extra = 1
    fields = ("order", "text")
    verbose_name_plural = (
        "Ingredients - Enter each ingredient with its measurements"
        " individually (e.g. '200g flour')."
    )


class MethodInline(admin.TabularInline):
    model = Method
    extra = 1
    fields = ("order", "text")
    verbose_name_plural = "Method - Enter each step of the method individually."


@admin.register(RecipePost)
class RecipePostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "created_on")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [IngredientsInline, MethodInline]


# Register your models here.
admin.site.register(Comment)
admin.site.unregister(EmailAddress)
