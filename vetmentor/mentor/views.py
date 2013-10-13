from __future__ import unicode_literals

from django.views.generic import View
from django.shortcuts import render


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
