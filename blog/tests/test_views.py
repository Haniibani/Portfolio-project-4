from django.test import TestCase
from django.urls import reverse
from blog.models import Recipe
from django.contrib.auth.models import User


class RecipeListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        This method is used for setup that is needed for all test
        cases in this class. Here, we are creating a Recipe instance
        to be used for subsequent tests.
        """
        Recipe.objects.create(
            title="Test Recipe",
            slug="test-recipe",
            tag="Normal",
            estimated_time=30,
            instructions="Some test instructions",
            status=1,
        )

    def test_view_url_exists_at_desired_location(self):
        """
        This test checks whether the URL for the view exists
        at the desired location, in this case the root URL ('/').
        It sends a GET request to the root URL
        and checks if the HTTP response has a status code of 200 (HTTP OK).
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        This test verifies that the URL for the view can
        be accessed using its name. It sends a GET request
        to the URL with the name 'recipe' and checks if the
        HTTP response has a status code of 200 (HTTP OK).
        """
        response = self.client.get(reverse("recipe"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        This test checks whether the view uses the correct template.
        It sends a GET request to the URL with the name 'recipe'
        and then verifies if the response used the 'index.html' template.
        """
        response = self.client.get(reverse("recipe"))
        self.assertTemplateUsed(response, "index.html")


class RecipeDetailViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        This method is used for setup that is needed
        for all test cases in this class. A Recipe instance
        is created to be used for subsequent tests. The Recipe
        has a title of "Test Recipe", a slug of "test-recipe",
        a tag of "Normal", an estimated time of 30 minutes,
        and a status of 1 (published).
        """
        Recipe.objects.create(
            title="Test Recipe",
            slug="test-recipe",
            tag="Normal",
            estimated_time=30,
            instructions="Some test instructions",
            status=1,
        )

    def test_view_url_exists_at_desired_location(self):
        """
        This test verifies that the URL for the RecipeDetail
        view exists at the expected location. It sends a GET
        request to the '/test-recipe/' URL and checks if the
        HTTP response has a status code of 200, which indicates success.
        """
        response = self.client.get("/test-recipe/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """
        This test verifies that the URL for the RecipeDetail
        view can be accessed using its name and the appropriate arguments.
        It uses Django's reverse function to find the URL of the
        view named 'recipe_detail', providing the slug 'test-recipe'
        as an argument. The test then sends a GET request to this
        URL and checks if the HTTP response
        has a status code of 200, indicating success.
        """
        response = self.client.get(
            reverse("recipe_detail", args=["test-recipe"])
        )
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """
        This test checks if the RecipeDetail view uses the correct template.
        It sends a GET request to the URL for the 'recipe_detail'
        view and then checks if the 'recipe_detail.html'
        template was used in the response.
        """
        response = self.client.get(
            reverse("recipe_detail", args=["test-recipe"])
        )
        self.assertTemplateUsed(response, "recipe_detail.html")


class RecipeLikeViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Sets up data for all test methods in this class.
        Creates a user and a recipe instance for subsequent tests.
        """
        cls.user = User.objects.create_user(
            username="testuser", password="testpass"
        )
        Recipe.objects.create(
            title="Test Recipe",
            slug="test-recipe",
            tag="Normal",
            estimated_time=30,
            instructions="Some test instructions",
            status=1,
        )

    def test_like_view_post_request(self):
        """
        This test verifies the 'like' functionality of a recipe.
        The test logs in as a user, makes a POST request to 'like' a recipe,
        and then checks if the response correctly redirects
        to the recipe detail page.
        """
        self.client.login(username="testuser", password="testpass")
        url = reverse("recipe_like", args=["test-recipe"])
        response = self.client.post(url)
        self.assertRedirects(
            response, reverse("recipe_detail", args=["test-recipe"])
        )
