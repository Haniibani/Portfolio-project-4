from django.test import TestCase
from django.urls import reverse
from blog.models import Recipe
from django.contrib.auth.models import User

class RecipeListViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Recipe.objects.create(
            title="Test Recipe",
            slug="test-recipe",
            tag="Normal",
            estimated_time=30,
            instructions="Some test instructions",
            status=1,
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('recipe'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('recipe'))
        self.assertTemplateUsed(response, 'index.html')  # Updated template name


class RecipeDetailViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        Recipe.objects.create(
            title="Test Recipe",
            slug="test-recipe",
            tag="Normal",
            estimated_time=30,
            instructions="Some test instructions",
            status=1,
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/test-recipe/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('recipe_detail', args=['test-recipe']))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('recipe_detail', args=['test-recipe']))
        self.assertTemplateUsed(response, 'recipe_detail.html')  # Updated template name


class RecipeLikeViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='testpass')
        Recipe.objects.create(
            title="Test Recipe",
            slug="test-recipe",
            tag="Normal",
            estimated_time=30,
            instructions="Some test instructions",
            status=1,
        )

    def test_like_view_post_request(self):
        self.client.login(username='testuser', password='testpass')
        url = reverse('recipe_like', args=['test-recipe'])
        response = self.client.post(url)
        self.assertRedirects(response, reverse('recipe_detail', args=['test-recipe']))
