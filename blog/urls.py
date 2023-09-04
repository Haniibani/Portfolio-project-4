from . import views
from django.urls import path


urlpatterns = [
    path("", views.RecipeList.as_view(), name="recipe"),
    path("like/<slug:slug>/", views.RecipeLike.as_view(), name="recipe_like"),
    path('<slug:slug>/<int:comment_id>/', views.RecipeDetail.as_view(), name='recipe_detail_edit_comment'),
    path("<slug:slug>/", views.RecipeDetail.as_view(), name="recipe_detail"),
]
