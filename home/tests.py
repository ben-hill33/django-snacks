from django.test import SimpleTestCase, client
from django.http import response
from django.urls import reverse


class SnacksTest(SimpleTestCase):
    def test_home_page_status(self):
        url = reverse("home_index")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_about_page_status(self):
        url = reverse("about")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_home_template(self):
        url = reverse("home_index")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "home_index.html")

    def test_about_template(self):
        url = reverse("about")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "about.html")

    def test_base_template(self):
        url = reverse("home_index")
        response = self.client.get(url)
        self.assertTemplateUsed(response, "base.html")
