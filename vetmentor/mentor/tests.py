from __future__ import unicode_literals

from django.test import TestCase, Client
from vetmentor.mentor.models import User, Industry


class LandingTest(TestCase):
    def setUp(self):
        self.c = Client()

    def test_get_landing(self):
        """Show the landing page.
        """
        response = self.c.get('/')
        self.assertTemplateUsed(response, 'landing.html')

class SignupView(TestCase):
    def setUp(self):
        self.c = Client()
        self.uri = '/signup'

        self.industry = Industry(title='aewfioj', code=12)
        self.industry.save()

        self.email = 'awer@aowie.com'
        self.user = {
            'name': 'aeawef',
            'email': self.email,
            'password': 'aowefij',
            'birthday': '1989-02-16',
            'gender': 0,
            'category': 0,
            'industry': industry.id
        }
        self.vet = {
            'rank': 'awef',
            'service_location': 'awoefij',
            'service_start_date': '1234-12-31',
            'education': 0
        }

    def test_create_profile(self):
        response = self.c.post(self.uri, self.user)
        self.assertTemplateUsed(response, 'create_vet_profile.html')

        # the user should be created
        User.objects.get(email=self.email)

