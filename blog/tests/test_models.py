from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Recipe, Ingredient, Comment


class IngredientModelTest(TestCase):
    def test_string_representation(self):
        """
        This test verifies that the string representation of the Ingredient model
        is correctly configured. A Recipe and Ingredient instance are created for the
        test, and it checks if the __str__ method of the Ingredient returns its name.
        """
        recipe = Recipe.objects.create(
            title="Test Recipe", slug="test-recipe", estimated_time=30
        )
        ingredient = Ingredient.objects.create(
            recipe=recipe, ingredient="Sample Ingredient", unit="kg", amount=5
        )
        self.assertEqual(str(ingredient), "Sample Ingredient")


class RecipeModelTest(TestCase):
    def test_ordering(self):
        """
        This test verifies the default ordering of Recipe model instances.
        Two Recipe instances are created with different titles and estimated times.
        The test asserts that the recipes are ordered in the descending order of their creation
        (i.e., the most recently created recipe comes first).
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
        """
        This test verifies that the 'slug' field of the Recipe model is unique.
        After creating a recipe with a specific slug, an attempt to create another recipe
        with the same slug should raise an exception.
        """
        Recipe.objects.create(
            title="Recipe 1", slug="recipe-1", estimated_time=30
        )
        with self.assertRaises(
            Exception
        ):  # Check for the correct exception that fits your case
            Recipe.objects.create(
                title="Recipe 2", slug="recipe-1", estimated_time=40
            )

    def test_number_of_likes(self):
        """
        This test verifies the `number_of_likes` method of the Recipe model.
        It creates a Recipe instance and two User instances who like the recipe.
        The test checks if the `number_of_likes` method correctly returns the number of likes.
        """
        user1 = User.objects.create(username="user1")
        user2 = User.objects.create(username="user2")
        recipe = Recipe.objects.create(
            title="Recipe", slug="recipe", estimated_time=30
        )
        recipe.likes.add(user1, user2)
        self.assertEqual(recipe.number_of_likes(), 2)


class IngredientModelTest(TestCase):
    def test_string_representation(self):
        """
        This test verifies that the string representation (__str__ method) of an Ingredient model
        instance is correctly set up. A Recipe and Ingredient instance are created for the test.
        The test then asserts if the __str__ method of the Ingredient returns its 'ingredient' field.
        """
        recipe = Recipe.objects.create(
            title="Test Recipe", slug="test-recipe", estimated_time=30
        )
        ingredient = Ingredient.objects.create(
            recipe=recipe, ingredient="Sample Ingredient", unit="kg", amount=5
        )
        # The Ingredient's __str__ method must be updated to reflect the format you want to test against.
        self.assertEqual(
            str(ingredient), ingredient.ingredient
        )  # Update this based on the correct string format


class CommentModelTest(TestCase):
    def test_string_representation(self):
        """
        This test checks the string representation (__str__ method) of the Comment model.
        It asserts that the __str__ method of a Comment instance returns a string formatted
        as "Comment {comment_body} by {user_name}".
        """
        recipe = Recipe.objects.create(
            title="Test Recipe", slug="test-recipe", estimated_time=30
        )
        comment = Comment.objects.create(
            name="User 1", body="Comment 1", recipe=recipe
        )
        self.assertEqual(str(comment), f"Comment Comment 1 by User 1")

    def test_comment_ordering(self):
        """
        This test verifies the default ordering of Comment model instances.
        It creates two Comment instances and then asserts that they are ordered in the order of creation
        (i.e., the earliest created comment comes first).
        """
        recipe = Recipe.objects.create(
            title="Test Recipe", slug="test-recipe", estimated_time=30
        )
        Comment.objects.create(name="User 1", body="Comment 1", recipe=recipe)
        Comment.objects.create(name="User 2", body="Comment 2", recipe=recipe)
        comments = Comment.objects.all()
        self.assertEqual(comments[0].body, "Comment 1")
        self.assertEqual(comments[1].body, "Comment 2")
