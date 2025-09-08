from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from recipe_post.models import RecipePost, Ingredients, Method, Comment


User = get_user_model()


class RecipePostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )

    def create_recipe(self, **overrides):
        data = dict(
            title='Test Recipe',
            slug='test-recipe',
            author=self.user,
            image='test.jpg',
            difficulty='easy',
            duration=30,
            summary='A delicious test recipe.',
            status=1,
            approved=True,
        )
        data.update(overrides)
        return RecipePost.objects.create(**data)

# RecipePost Tests
    def test_create_recipe_successfully(self):
        # Creates recipe successfully
        post = self.create_recipe(
            title='Tomato Soup',
            slug='tomato-soup',
            approved=False,
            status=0
        )
        self.assertEqual(str(post), 'Tomato Soup')
        self.assertFalse(post.approved)
        self.assertEqual(post.status, 0)

    def test_duration_valid(self):
        # duration - rejects value of less than 1
        post = RecipePost(
            title='Invalid Duration',
            slug='invalid-duration',
            author=self.user,
            image='test.jpg',
            difficulty='easy',
            duration=0,
            summary='Invalid duration test.',
            status=1,
            approved=True,
        )
        with self.assertRaises(ValidationError):
            post.full_clean()

    def test_unique_slug(self):
        # slug - generates unique slug
        self.create_recipe(slug='unique-slug')
        with self.assertRaises(IntegrityError):
            self.create_recipe(slug='unique-slug')

# Ingredients/Method Tests
    def test_ing_order_autoincrement(self):
        # auto increments order field correctly (unordered and ordered lists)
        post = self.create_recipe(slug="with-ingredients")
        ing1 = Ingredients.objects.create(recipe=post, text="Flour")
        ing2 = Ingredients.objects.create(recipe=post, text="Sugar")
        self.assertEqual(ing1.order, 1)
        self.assertEqual(ing2.order, 2)
        orders = list(post.ingredients_rel.values_list('order', flat=True))
        self.assertEqual(orders, [1, 2])

    def test_ing_order_per_recipe(self):
        post = self.create_recipe(slug="recipe-one")
        Ingredients.objects.create(recipe=post, order=1, text="Flour")
        with self.assertRaises(IntegrityError):
            Ingredients.objects.create(recipe=post, order=1, text="Sugar")

    def test_method_autoincrement_order(self):
        post = self.create_recipe(slug="with-method")
        m1 = Method.objects.create(recipe=post, text="Boil water")
        m2 = Method.objects.create(recipe=post, text="Add pasta")
        self.assertEqual(m1.order, 1)
        self.assertEqual(m2.order, 2)
        orders = list(post.method_rel.values_list("order", flat=True))
        self.assertEqual(orders, [1, 2])

    def test_method_unique_order_per_recipe(self):
        post = self.create_recipe(slug="method-constraint")
        Method.objects.create(recipe=post, order=1, text="Step A")
        with self.assertRaises(IntegrityError):
            Method.objects.create(recipe=post, order=1, text="Step B")

    def test_cascade_delete_ingredients_method(self):
        # cascades delete when RecipePost is deleted
        post = self.create_recipe(slug="to-delete")
        Ingredients.objects.create(recipe=post, text="Ingredient 1")
        Method.objects.create(recipe=post, text="Step 1")
        post.delete()
        self.assertEqual(Ingredients.objects.filter(recipe=post).count(), 0)
        self.assertEqual(Method.objects.filter(recipe=post).count(), 0)

# Comment Tests
    def test_comment_defaults_str_and_order(self):
        # creates comment successfully with approved=False status
        post = self.create_recipe(slug="with-comments")
        comment = Comment.objects.create(
            recipe=post,
            author=self.user,
            content="This is a test comment."
        )
        self.assertFalse(comment.approved)
        self.assertEqual(comment.status, 0)
        self.assertEqual(str(comment), f"on {post.title}")

        Comment.objects.create(
            recipe=post, author=self.user, content="Another comment."
        )
        newest_first = list(
            Comment.objects.filter(recipe=post).values_list(
                "content", flat=True
            )
        )
        self.assertEqual(newest_first[0], "This is a test comment.")
