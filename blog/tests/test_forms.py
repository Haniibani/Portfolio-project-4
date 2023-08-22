from django.test import TestCase
from blog.forms import CommentForm
from blog.models import Comment, Recipe


class CommentFormTest(TestCase):
    """
    This is the main test class for the CommentForm.
    It extends the TestCase class from Django's test framework.
    """

    def test_valid_data(self):
        """
        This test verifies that the CommentForm accepts valid data.
        Here, valid data means a name and a body of the comment are provided.
        """
        form = CommentForm(
            data={"name": "John Doe", "body": "This is a valid comment."}
        )
        self.assertTrue(form.is_valid())  # Asserts if the form is valid

    def test_invalid_data_type(self):
        """
        This test checks that the form correctly handles invalid data.
        Here, the body of the comment exceeds the maximum allowed length,
        which is likely defined as 1000 characters in the form validation.
        It also verifies that the form correctly handles a foreign key (recipe).
        """
        recipe = Recipe.objects.create(title="Test Recipe", estimated_time=30)
        long_comment = (
            "a" * 1001
        )  # Create a long comment with more than 1000 characters
        data = {"name": "John Doe", "body": long_comment, "recipe": recipe.id}
        form = CommentForm(data=data)
        self.assertFalse(form.is_valid())  # Asserts if the form is not valid

    def test_max_length(self):
        """
        This test verifies that the CommentForm correctly handles the
        maximum length condition. Here, a comment of exactly 1000 characters
        (the assumed maximum limit) is considered valid.
        """
        max_length = 1000
        long_comment = "a" * max_length
        form = CommentForm(data={"name": "John Doe", "body": long_comment})
        self.assertTrue(form.is_valid())  # Asserts if the form is valid

    def test_max_length_exceeded(self):
        """
        This test checks that the CommentForm handles cases where the
        maximum length of the comment body is exceeded. A comment with
        1001 characters (one more than the maximum) is correctly
        flagged as invalid.
        """
        max_length = 1000
        long_comment = "a" * (max_length + 1)
        form = CommentForm(data={"name": "John Doe", "body": long_comment})
        self.assertFalse(form.is_valid())  # Asserts if the form is not valid
        # Checks if the error message is correct when the max_length is exceeded
        self.assertEqual(
            form.errors["body"],
            [
                f"Ensure this value has at most {max_length} characters (it has {len(long_comment)})."
            ],
        )

    def test_clean_special_characters(self):
        """
        This test case ensures that the CommentForm correctly handles special characters.
        Given that the 'clean' method of the form doesn't do any special character cleaning,
        this test case provides input that includes special characters and checks if the form is still valid.
        """
        recipe = Recipe.objects.create(title="Test Recipe", estimated_time=30)
        special_character_comment = (
            "Test Comment with special characters !@#$%^&*()"
        )
        data = {"body": special_character_comment, "recipe": recipe.id}
        form = CommentForm(data=data)
        self.assertTrue(form.is_valid())  # Asserts if the form is valid

        cleaned_comment = form.cleaned_data["body"]
        # Assuming that special characters are not removed during the cleaning process
        self.assertEqual(special_character_comment, cleaned_comment)

    def test_label(self):
        """
        This test verifies that the labels of the CommentForm are correctly set.
        It now checks the label for the 'body' field.
        """
        form = CommentForm()

        # Checks label for 'body' field
        self.assertEqual(form.fields["body"].label, "Write your comment here:")
