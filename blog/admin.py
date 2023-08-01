from django.contrib import admin
from .models import Recipe, Ingredient

class IngredientInline(admin.TabularInline):
    model = Ingredient
    extra = 2

class RecipeAdmin(admin.ModelAdmin):
    inlines = (IngredientInline,)

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
