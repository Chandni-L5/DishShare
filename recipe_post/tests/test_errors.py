from django.test import TestCase, override_settings
from django.core.exceptions import PermissionDenied, SuspiciousOperation
from django.http import Http404
from django.urls import include, path


def trigger_400(request): raise SuspiciousOperation("bad request")
def trigger_403(request): raise PermissionDenied("forbidden")
def trigger_404(request): raise Http404("not found")
def trigger_500(request): 1 / 0


urlpatterns = [
    path("", include("dishshare.urls")),
    path("trigger-400/", trigger_400),
    path("trigger-403/", trigger_403),
    path("trigger-404/", trigger_404),
    path("trigger-500/", trigger_500),
]


@override_settings(
    DEBUG=False,
    ROOT_URLCONF=__name__,
    ALLOWED_HOSTS=["testserver"],
)
class ErrorPageTemplateTests(TestCase):
    def setUp(self):
        self.client.raise_request_exception = False

    def test_400_template_used(self):
        resp = self.client.get("/trigger-400/")
        self.assertEqual(resp.status_code, 400)
        self.assertTemplateUsed(resp, "400.html")

    def test_403_template_used(self):
        resp = self.client.get("/trigger-403/")
        self.assertEqual(resp.status_code, 403)
        self.assertTemplateUsed(resp, "403.html")

    def test_404_template_used(self):
        resp = self.client.get("/trigger-404/")
        self.assertEqual(resp.status_code, 404)
        self.assertTemplateUsed(resp, "404.html")

    def test_500_template_used(self):
        resp = self.client.get("/trigger-500/")
        self.assertEqual(resp.status_code, 500)
        self.assertTemplateUsed(resp, "500.html")
