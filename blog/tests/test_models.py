from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Recipe, Ingredient, Comment


class IngredientModelTest(TestCase):
    """Tests for the Ingredient model."""

    def test_string_representation(self):
        """Checks if string representation returns the ingredient's name."""
        recipe = Recipe.objects.create(
            title="Test Recipe", slug="test-recipe", estimated_time=30
        )
        ingredient = Ingredient.objects.create(
            recipe=recipe,
            ingredient="Sample Ingredient",
            unit="kg",
            amount=5
        )
        self.assertEqual(str(ingredient), "Sample Ingredient")


class RecipeModelTest(TestCase):
    """Tests for the Recipe model."""

    def test_ordering(self):
        """
        Checks if recipes are ordered by their creation in descending order.
        """
        Recipe.objects.create(
            title="Recipe 1", slug="recipe-1", estimated_time=30
        )
        Recipe.objects.create(
            title="Recipe 2", slug="recipe-2", estimated_time=40
        )
        recipes = Recipe.objects.all()
        self.assertEqual(recipes[0].title, "Recipe 2")
        self.assertEqual(recipes[1].title, "Recipe 1")

    def test_slug_uniqueness(self):
        """Verifies that the slug field is unique."""
        Recipe.objects.create(
            title="Recipe 1", slug="recipe-1", estimated_time=30
        )
        with self.assertRaises(Exception):
            Recipe.objects.create(
                title="Recipe 2", slug="recipe-1", estimated_time=40
            )

    def test_number_of_likes(self):
        """Verifies that the number_of_likes method returns correct count."""
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        recipe = Recipe.objects.create(
            title="Recipe", slug="recipe", estimated_time=30
        )
        recipe.likes.add(user1, user2)
        self.assertEqual(recipe.number_of_likes(), 2)


class CommentModelTest(TestCase):
    """Tests for the Comment model."""

    def test_string_representation(self):
        """
        Verifies correct string format 'Comment {comment_body} by {user_name}'.
        """
        recipe = Recipe.objects.create(
            title="Test Recipe", slug="test-recipe", estimated_time=30
        )
        comment = Comment.objects.create(
            name="User 1", body="Comment 1", recipe=recipe
        )
        self.assertEqual(str(comment), "Comment Comment 1 by User 1")

    def test_comment_ordering(self):
        """Checks if comments are ordered by their creation order."""
        recipe = Recipe.objects.create(
            title="Test Recipe", slug="test-recipe", estimated_time=30
        )
        Comment.objects.create(
            name="User 1", body="Comment 1", recipe=recipe
        )
        Comment.objects.create(
            name="User 2", body="Comment 2", recipe=recipe
        )
        comments = Comment.objects.all()
        self.assertEqual(comments[0].body, "Comment 1")
        self.assertEqual(comments[1].body, "Comment 2")
