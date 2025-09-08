from django.test import TestCase, RequestFactory, override_settings
from django.contrib.auth import get_user_model
from django.urls import reverse
from accounts.forms import CustomSignupForm


# Create your tests here.
User = get_user_model()


# Signup form tests
class CustomSignupFormTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def valid_data(self, **overrides):
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "confirm_email": "testuser@example.com",
            "password1": "testpassword",
            "password2": "testpassword",
        }
        data.update(overrides)
        return data

    def test_required_fields(self):
        # Test that all required fields are enforced
        form = CustomSignupForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn("username", form.errors)
        self.assertIn("email", form.errors)
        self.assertIn("confirm_email", form.errors)
        self.assertIn("password1", form.errors)
        self.assertIn("password2", form.errors)

    def test_email_mismatch_non_field_error(self):
        # Test that email mismatch raises a non-field error
        form = CustomSignupForm(
            data=self.valid_data(confirm_email="different@example.com")
        )
        self.assertFalse(form.is_valid())
        self.assertIn("Email does not match.", form.non_field_errors())

    def test_password_mismatch_error(self):
        # Test that password mismatch raises an error on password2 field
        form = CustomSignupForm(
            data=self.valid_data(password2="Different123!")
        )
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)


# Login tests
@override_settings(
    SITE_ID=1,
    ACCOUNT_EMAIL_VERIFICATION="none",
    ACCOUNT_AUTHENTICATION_METHOD="username",
    ACCOUNT_FORMS={},
    LOGIN_REDIRECT_URL="/",
)
class LoginViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="alice", email="alice@example.com", password="pass12345"
        )

    def test_get_login_renders(self):
        # Test that the login page renders correctly
        url = reverse("account_login")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        html = resp.content.decode()
        self.assertIn('name="login"', html)
        self.assertIn('name="password"', html)


# Logout tests
@override_settings(
    SITE_ID=1,
    ACCOUNT_EMAIL_VERIFICATION="none",
    LOGIN_REDIRECT_URL="/",
    ACCOUNT_LOGOUT_REDIRECT_URL="/goodbye/",
)
class LogoutViewTestsGET(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="bob", email="bob@example.com", password="pass12345"
        )

    @override_settings(ACCOUNT_LOGOUT_ON_GET=True)
    def test_logout_on_get_redirects_and_clears_session(self):
        # Test that logout via GET redirects and clears the session
        self.client.login(username="bob", password="pass12345")
        self.assertIn("_auth_user_id", self.client.session)
        url = reverse("account_logout")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
        self.assertTrue(resp["Location"].endswith("/goodbye/"))
        self.assertNotIn("_auth_user_id", self.client.session)
