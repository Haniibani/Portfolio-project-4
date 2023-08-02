from django.contrib import admin
from .models import Recipe, Ingredient, Comment
from django_summernote.admin import SummernoteModelAdmin


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 1


@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'tag')
    list_filter = ('status', 'created_on')
    search_fields = ('title', 'ingredient')
    summernote_fields = ('instructions',)
    inlines = (IngredientInline,)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approved_comments']

    def approved_comments(self, request, queryset):
        queryset.update(approved=True)