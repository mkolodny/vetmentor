from __future__ import unicode_literals

from django.views.generic import View
from django.shortcuts import render
from django.contrib import auth
from vetmentor.mentor.models import User
from vetmentor.mentor import forms


class LandingView(View):
    """
    Landing page.
    """
    http_method_names = ['get', 'post']

    def get(self, request, *args, **kwargs):
        """
        Show the landing page.
        """
        return render(request, 'landing.html')

class SignupView(View):
    """
    Sign up pages.
    """
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        """
        Create a user's account.
        """
        form = forms.SignupForm(request.POST)
        user = User(name=form.name.data,
                    email=form.email.data,
                    birthday=form.birthday.data,
                    gender=form.gender.data,
                    category=form.category.data,
                    industry_id=form.industry.data)
        user.set_password(form.password.data)
        user.save()

        # mimic auth.authenticate, then login
        backend = auth.get_backends()[0]
        user.backend = '%s.%s' % (backend.__module__, backend.__class__.__name__)
        auth.login(request, user)

        return render(request, 'create_vet_profile.html')
