from __future__ import unicode_literals

from django.contrib import auth
from django.core.mail import send_mail      # for contact form
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View

from vetmentor.mentor.models import User
from vetmentor.mentor import forms


def contact(request):
    # contact form view
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            send_mail(
                      cd['subject'],
                      cd['message'],
                      cd.get('email', 'noreply@example.com'),
                      [cd.get('recipient', 'downdigitalco@gmail.com')],
                      )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = forms.ContactForm(
                           initial={'subject': 'Will you be my mentor?'}
                           )
    return render(request, 'contact_form.html', {'form': form})

def thanks(request):
    return HttpResponse('Thanks for contacting us.')

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
