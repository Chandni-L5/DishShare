from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column
from recipe_post.models import RecipePost, Ingredients, Method
from django.forms import inlineformset_factory


class RecipePostForm(forms.ModelForm):
    """
    Form for users to submit a recipe to be reviewed by admin.
    related to :model:`recipe_post.RecipePost`.`authUser`
    """

    class Meta:
        model = RecipePost
        fields = ["title", "difficulty", "duration", "summary", "image"]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "Recipe title"}),
            "summary": forms.Textarea(
                attrs={"rows": 2, "placeholder": "Brief description"}
            ),
            "duration": forms.NumberInput(
                attrs={"min": 1, "placeholder": "in minutes"}
            ),
            "image": forms.FileInput(attrs={"class": "form-control"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name in self.fields:
            self.fields[name].required = True
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            "title",
            Row(
                Column("difficulty", css_class="col-md-6"),
                Column("duration", css_class="col-md-6"),
            ),
            "summary",
            "image",
        )


IngredientsFormSetCreate = inlineformset_factory(
    parent_model=RecipePost,
    model=Ingredients,
    fields=["text"],
    extra=0,
    can_delete=False,
    min_num=1,
    validate_min=True,
    widgets={"text": forms.TextInput(attrs={"placeholder": "e.g. 2 cups of flour"})},
)

IngredientsFormSetEdit = inlineformset_factory(
    parent_model=RecipePost,
    model=Ingredients,
    fields=["text"],
    extra=0,
    can_delete=True,
    min_num=1,
    validate_min=True,
    widgets={"text": forms.TextInput(attrs={"placeholder": "e.g. 2 cups of flour"})},
)

MethodFormSetCreate = inlineformset_factory(
    parent_model=RecipePost,
    model=Method,
    fields=["text"],
    extra=0,
    can_delete=False,
    min_num=1,
    validate_min=True,
    widgets={
        "text": forms.Textarea(
            attrs={
                "placeholder": "e.g. Preheat the oven to 180C",
                "rows": 2,
            }
        )
    },
)

MethodFormSetEdit = inlineformset_factory(
    parent_model=RecipePost,
    model=Method,
    fields=["text"],
    extra=0,
    can_delete=True,
    min_num=1,
    validate_min=True,
    widgets={
        "text": forms.Textarea(
            attrs={
                "placeholder": "e.g. Preheat the oven to 180C",
                "rows": 2,
            }
        )
    },
)
