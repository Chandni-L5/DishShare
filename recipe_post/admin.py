from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import RecipePost, Comment


@admin.register(RecipePost)
class PostAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'status')
    search_fields = ['title', 'author__username']
    list_filter = ('status', 'approved', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('method', 'ingredients', 'summary')

# Register your models here.
admin.site.register(Comment)
