from django.contrib import admin
from .models import Recipe, Ingredient, Comment
from django_summernote.admin import SummernoteModelAdmin


class IngredientInline(admin.TabularInline):
    """
    Define an inline admin view for `Ingredient` model.
    Allows managing ingredients directly within the `Recipe` form.
    """

    model = Ingredient
    extra = 1


@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    """
    Admin view for the `Recipe` model.
    Integrates Summernote for rich text editing.
    - Automatically populates 'slug' based on 'title'.
    - Provides specific fields for display, filtering, and searching.
    - Uses Summernote rich text editor for `instructions`.
    - Includes inline view for ingredients.
    """

    prepopulated_fields = {"slug": ("title",)}
    list_display = ("title", "tag")
    list_filter = ("status", "created_on")
    search_fields = ("title", "ingredient")
    summernote_fields = ("instructions",)
    inlines = (IngredientInline,)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    Admin view for the `Comment` model.
    - Specifies fields for display, filtering, and searching.
    - Provides a bulk action to approve selected comments.
    """

    list_display = ("name", "body", "created_on", "approved")
    list_filter = ("approved", "created_on")
    search_fields = ("name", "email", "body")
    actions = ["approved_comments"]

    def approved_comments(self, request, queryset):
        """
        Action to bulk-approve selected comments.
        """
        queryset.update(approved=True)
