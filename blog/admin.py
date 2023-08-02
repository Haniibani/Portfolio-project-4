from django.contrib import admin
from .models import Recipe, Ingredient
from django_summernote.admin import SummernoteModelAdmin


class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 2


@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'tag')
    list_filter = ('status', 'created_on')
    search_fields = ('title', 'ingredient')
    summernote_fields = ('instructions',)
    inlines = (IngredientInline,)


admin.site.register(Ingredient)
