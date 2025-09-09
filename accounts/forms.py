from allauth.account.forms import SignupForm, LoginForm
from django import forms
from django.core.exceptions import ValidationError


class CustomSignupForm(SignupForm):
    # Function to override the default django allauth signup form
    username = forms.CharField(
        label="Create Username",
        required=True,
        error_messages={"required": "Username is required"},
        widget=forms.TextInput(
            attrs={"placeholder": "Create username"}
        ),
    )
    email = forms.EmailField(
        label="Email",
        required=True,
        error_messages={"required": "Email is required"},
        widget=forms.EmailInput(attrs={"placeholder": "Email"}),
    )
    confirm_email = forms.EmailField(
        label="Confirm Email",
        required=True,
        error_messages={"required": "Please confirm your email"},
        widget=forms.EmailInput(attrs={"placeholder": "Confirm Email"}),
    )
    password1 = forms.CharField(
        label="Create Password",
        required=True,
        error_messages={"required": "Password is required"},
        widget=forms.PasswordInput(attrs={"placeholder": "Create password"}),
    )
    password2 = forms.CharField(
        label="Confirm Password",
        required=True,
        error_messages={"required": "Please confirm your password"},
        widget=forms.PasswordInput(attrs={"placeholder": "Confirm password"}),
    )

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        confirm_email = cleaned_data.get("confirm_email")

        if email and confirm_email and email != confirm_email:
            self.add_error(
                "confirm_email", ValidationError("Emails do not match")
            )
        return cleaned_data

        return cleaned_data

    def save(self, request):
        user = super().save(request)
        return user


class CustomLoginForm(LoginForm):
    # Function to override the default django allauth login form
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        field = self.fields.get("remember")
        if field:
            field.widget = forms.HiddenInput()
            field.required = False
            self.initial["remember"] = False
