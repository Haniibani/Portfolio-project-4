from django.test import TestCase
from blog.forms import CommentForm
from blog.models import Comment, Recipe


class CommentFormTest(TestCase):
    """Tests for the CommentForm."""

    def test_valid_data(self):
        """Verifies the form accepts valid body."""
        form = CommentForm(
            data={"body": "This is a valid comment."}
        )
        self.assertTrue(form.is_valid())

    def test_invalid_data_type(self):
        """Checks form handling for invalid data and foreign key."""
        recipe = Recipe.objects.create(title="Test Recipe", estimated_time=30)
        long_comment = "a" * 1001
        data = {"name": "John Doe", "body": long_comment, "recipe": recipe.id}
        form = CommentForm(data=data)
        self.assertFalse(form.is_valid())

    def test_max_length(self):
        """Verifies form handling for maximum comment length."""
        max_length = 1000
        long_comment = "a" * max_length
        form = CommentForm(data={"body": long_comment})
        self.assertTrue(form.is_valid())

    def test_max_length_exceeded(self):
        """Checks form handling when exceeding max comment length."""
        max_length = 1000
        long_comment = "a" * (max_length + 1)
        form = CommentForm(data={"body": long_comment})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['body'],
            ['Ensure this value has at most 1000 characters (it has 1001).']
        )

    def test_clean_special_characters(self):
        """Ensures form handling for special characters in comments."""
        recipe = Recipe.objects.create(title="Test Recipe", estimated_time=30)
        comment = "Test Comment with special characters !@#$%^&*()"
        data = {"body": comment, "recipe": recipe.id}
        form = CommentForm(data=data)
        self.assertTrue(form.is_valid())
        self.assertEqual(comment, form.cleaned_data["body"])

    def test_label(self):
        """Verifies form labels are correctly set."""
        form = CommentForm()
        self.assertEqual(form.fields["body"].label, "Write your comment here:")
