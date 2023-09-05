from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Recipe, Ingredient, Comment


class IngredientInline(admin.TabularInline):
    """
    Inline admin view for the Ingredient model.
    Enables managing ingredients directly within the Recipe form.
    """
    model = Ingredient
    extra = 1


@admin.register(Recipe)
class RecipeAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    """
    Admin configuration for the Recipe model.

    - Populates 'slug' based on 'title'.
    - Defines display, filtering, and searching fields.
    - Integrates Summernote for rich text editing of instructions.
    - Manages ingredients through inline forms.
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
    Admin configuration for the Comment model.

    - Defines display, filtering, and searching fields.
    - Allows bulk actions like comment approval.
    """
    list_display = ("name", "body", "created_on", "approved")
    list_filter = ("approved", "created_on")
    search_fields = ("name", "email", "body")
