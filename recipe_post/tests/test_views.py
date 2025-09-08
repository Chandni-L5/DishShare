from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from recipe_post.models import RecipePost


User = get_user_model()


class RecipeViewsTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.author = User.objects.create_user(
            "author", "a@example.com", "pass12345"
        )
        cls.other = User.objects.create_user(
            "other", "o@example.com", "pass12345"
        )
        cls.pub = RecipePost.objects.create(
            title="Public Recipe", slug="public-recipe", author=cls.author,
            image="img.jpg", difficulty="easy", duration=10, summary="ok",
            status=1, approved=True
        )
        cls.draft = RecipePost.objects.create(
            title="Draft Recipe", slug="draft-recipe", author=cls.author,
            image="img.jpg", difficulty="easy", duration=10, summary="ok",
            status=0, approved=False
        )

    def test_home_lists_published_only(self):
        # Home page lists only published recipes
        url = reverse("home")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Public Recipe")
        self.assertNotContains(resp, "Draft Recipe")

    def test_recipe_detail_accessible(self):
        # Detail view of a published recipe is accessible
        url = reverse("recipe_page", args=[self.pub.slug])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Public Recipe")

    def test_recipe_detail_404_on_missing_slug(self):
        # Detail view of a non-existent recipe returns 404
        url = reverse("recipe_page", args=["does-not-exist"])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)

    def test_submit_recipe_requires_login(self):
        # Submit recipe view requires login
        url = reverse("submit_recipe")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        self.assertIn("/accounts/login", resp["Location"])
        self.assertIn("next=", resp["Location"])

    def test_my_submissions_requires_login(self):
        # My submissions view requires login
        url = reverse("my_submissions")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        self.assertIn("next=", resp["Location"])

    def test_only_author_can_access_edit(self):
        # Only the author can access the edit view
        self.client.login(username="author", password="pass12345")
        ok = self.client.get(reverse("recipe_edit", args=[self.pub.slug]))
        self.assertIn(ok.status_code, (200, 302))
        self.client.logout()
        self.client.login(username="other", password="pass12345")
        denied = self.client.get(reverse("recipe_edit", args=[self.pub.slug]))
        self.assertEqual(denied.status_code, 404)
