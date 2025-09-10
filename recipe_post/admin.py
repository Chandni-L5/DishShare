from django.contrib import admin
from .models import RecipePost, Comment, Ingredients, Method
from allauth.account.models import EmailAddress
from django_summernote.models import Attachment
from django.contrib.auth.models import Group
from django.contrib.sites.models import Site


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
    verbose_name_plural = (
        "Method - Enter each step of the method "
        "individually."
    )


@admin.register(RecipePost)
class RecipePostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "status", "created_on")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [IngredientsInline, MethodInline]
    list_filter = ("status", "created_on", "author")


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("recipe", "created_on", "approved")
    list_filter = ("status", "created_on", "author")


# Register your models here.
admin.site.unregister(EmailAddress)
admin.site.unregister(Attachment)
admin.site.unregister(Group)
admin.site.unregister(Site)
