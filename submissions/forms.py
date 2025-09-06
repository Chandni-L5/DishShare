from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Submit
from recipe_post.models import RecipePost  # import your existing model


class RecipePostForm(forms.ModelForm):
    class Meta:
        model = RecipePost
        fields = ["title", "difficulty", "duration", "summary", "image"]
        widgets = {
            "summary": forms.Textarea(attrs={"rows": 3, "placeholder": "Brief description"}),
            "duration": forms.NumberInput(attrs={"min": 1, "placeholder": "in minutes"}),
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
