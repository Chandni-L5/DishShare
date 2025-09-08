from django.db import models, transaction
from django.db.models import Max
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


# Create your models here.
class RecipePost(models.Model):
    """
    Stores a single recipe post entry related to :model:`auth.User`.
    Meta: Orders the list of recipe posts by creation date.
    Methods: Returns a string representation of the recipe post.
    """
    recipe_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    difficulty = models.CharField(max_length=100, choices=[
        ('easy', 'Easy peasy'),
        ('medium', 'Medium rare'),
        ('hard', 'Hard boiled'),
    ])
    duration = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1, message="Duration must be at least 1 minute.")
        ], help_text="Please enter the cooking time in minutes."
    )
    summary = models.TextField(max_length=500, blank=True)
    created_on = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Ingredients(models.Model):
    """
    Stores individual ingredients related to :model:`recipe_post.RecipePost`.
    Methods: returns a string representation of the ingredient.
    """
    recipe = models.ForeignKey(
        RecipePost, on_delete=models.CASCADE, related_name='ingredients_rel'
    )
    order = models.PositiveSmallIntegerField(null=True, blank=True)
    text = models.CharField(
        max_length=255,
    )

    class Meta:
        ordering = ['order']
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'order'],
                name='unique_ingredient_order_per_recipe'
            )
        ]

    def save(self, *args, **kwargs):
        if self.pk is None and not self.order:
            with transaction.atomic():
                last = (
                    Ingredients.objects
                    .filter(recipe=self.recipe)
                    .aggregate(m=Max('order'))['m'] or 0
                )
                self.order = last + 1
        super().save(*args, **kwargs)


class Method(models.Model):
    """
    Stores individual method steps related to :model:`recipe_post.RecipePost`.
    Methods: returns a string representation of the method step.
    """
    recipe = models.ForeignKey(
        RecipePost, on_delete=models.CASCADE, related_name='method_rel'
    )
    order = models.PositiveSmallIntegerField(null=True, blank=True)
    text = models.TextField(
        help_text="Enter each step of the method individually."
    )

    class Meta:
        ordering = ['order']
        constraints = [
            models.UniqueConstraint(
                fields=['recipe', 'order'],
                name='unique_method_order_per_recipe'
            )
        ]

    def save(self, *args, **kwargs):
        if self.pk is None and not self.order:
            with transaction.atomic():
                last = (
                    Method.objects
                    .filter(recipe=self.recipe)
                    .aggregate(m=Max('order'))['m'] or 0
                )
                self.order = last + 1
        super().save(*args, **kwargs)


class Comment(models.Model):
    """
    Stores a single comment entry related to :model:`recipe_post.RecipePost`.
    Meta: Orders the list of comments by creation date.
    Methods: returns a string indicating which recipe the comment is
    associated with.
    """
    recipe = models.ForeignKey(
        RecipePost, on_delete=models.CASCADE, related_name='comments'
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"on {self.recipe.title}"
