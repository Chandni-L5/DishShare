from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.files.uploadedfile import SimpleUploadedFile
from recipe_post.models import RecipePost
from submissions.forms import RecipePostForm


# Create your tests here.
User = get_user_model()


class RecipeFormsTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="author", email="a@example.com", password="pass12345"
        )
        cls.post = RecipePost.objects.create(
            title="Seed",
            slug="seed",
            author=cls.user,
            image="seed.jpg",
            difficulty="easy",
            duration=10,
            summary="ok",
            status=1,
            approved=True,
        )

    def test_recipe_post_form_valid_data_is_valid(self):
        # Test that RecipePostForm is valid with correct data
        data = {
            "title": "Apple Pie",
            "difficulty": "easy",
            "duration": 25,
            "summary": "Yum",
        }
        file = SimpleUploadedFile(
            "img.jpg", b"fake-bytes", content_type="image/jpeg"
        )
        form = RecipePostForm(data=data, files={"image": file})
        self.assertTrue(form.is_valid(), form.errors)

    def test_recipe_post_form_invalid_duration(self):
        # Test that RecipePostForm is invalid with duration less than 1
        data = {
            "title": "Bad",
            "difficulty": "easy",
            "duration": 0,
            "summary": "no",
        }
        file = SimpleUploadedFile("img.jpg", b"x", content_type="image/jpeg")
        form = RecipePostForm(data=data, files={"image": file})
        self.assertFalse(form.is_valid())
        self.assertIn("duration", form.errors)
        self.assertIn("at least 1 minute", str(form.errors["duration"]))
