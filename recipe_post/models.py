from django.db import models
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
    ingredients = models.TextField(
        help_text=(
            "Enter ingredients with measurements,"
            "one per line, separated by a comma "
            "(e.g., '200g flour, '2tbsp sugar')."
        )
    )
    method = models.TextField(
        help_text="Please enter each step on a new line.")
    created_on = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    status = models.IntegerField(choices=STATUS, default=0)
    summary = models.TextField(max_length=500, blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


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
