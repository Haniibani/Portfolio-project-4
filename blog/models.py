"""
This module defines the data models for the blog application.
"""

from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))
GLUTENFREE = "Glutenfree"
LACTOSEFREE = "Lactosefree"
NORMAL = "Normal"
VEGAN = "Vegan"
NUTFREE = "Nutfree"
TAGS = [
    (GLUTENFREE, "Glutenfree"),
    (LACTOSEFREE, "Lactosefree"),
    (NORMAL, "Normal"),
    (VEGAN, "Vegan"),
    (NUTFREE, "Nutfree"),
]


class Recipe(models.Model):
    """
    Represents a recipe with ingredients, an image, and related comments.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    tag = models.CharField(max_length=100, choices=TAGS, default=NORMAL)
    featured_image = CloudinaryField("image", default="placeholder")
    updated_on = models.DateTimeField(auto_now=True)
    estimated_time = models.IntegerField("Estimated time")
    instructions = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name="recipe_like", blank=True
    )

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        ingredients_list = [
            f"{ingredient.amount} {ingredient.unit} {ingredient.ingredient}"
            for ingredient in self.ingredient_set.all()
        ]
        return f"{self.title} - {' | '.join(ingredients_list)}"

    def number_of_likes(self):
        """
        Return the count of likes for this recipe.
        """
        return self.likes.count()


class Ingredient(models.Model):
    """
    Represents an ingredient which is associated with a specific recipe.
    """
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)
    amount = models.IntegerField()

    def __str__(self):
        return self.ingredient


class Comment(models.Model):
    """
    Represents a comment made on a specific recipe.
    """
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments"
    )
    name = models.CharField(max_length=80)
    body = models.TextField(max_length=1000)
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"
