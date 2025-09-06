from django.contrib import admin
from .models import RecipePost, Comment, Ingredients, Method


class IngredientsInline(admin.TabularInline):
    model = Ingredients
    extra = 1
    fields = ("order", "text")


class MethodInline(admin.TabularInline):
    model = Method
    extra = 1
    fields = ("order", "text")


@admin.register(RecipePost)
class RecipePostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "created_on")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [IngredientsInline, MethodInline]


# Register your models here.
admin.site.register(Comment)
