from __future__ import unicode_literals

from django.test import TestCase, Client


class LandingTest(TestCase):
    def setUp(self):
        self.c = Client()

    def test_get_landing(self):
        """Show the landing page.
        """
        response = self.c.get('/')
        self.assertTemplateUsed(response, 'landing.html')
