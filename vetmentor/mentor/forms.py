from __future__ import unicode_literals

from django import forms
from wtforms import Form, TextField, IntegerField, DateField
from wtforms.validators import Required, Optional, AnyOf
from vetmentor.mentor.models import User


class ContactForm(forms.Form):
    recipient = forms.EmailField(required=False, label='To')
    email = forms.EmailField(required=False, label='From')
    subject = forms.CharField(max_length=100)
    message = forms.CharField(required=False, widget=forms.Textarea)
    """
    def clean_message(self):
        message = self.cleaned_data['message']
        num_words = len(message.split())
        if num_words < 4:
            raise forms.ValidationError("Not enough words!")
        return message
    """
        
class SignupForm(Form):
    """
    A new user is signing up.
    """
    name = TextField('name', [Required()])
    email = TextField('email', [Required()])
    password = TextField('password', [Required()])
    birthday = DateField('birthday', [Required()])
    gender = IntegerField('gender', [Required(), AnyOf([User.MALE, User.FEMALE])])
    category = IntegerField('category', [Required(), AnyOf([User.VETERAN, User.CIVILIAN])])
    industry = IntegerField('industry', [Required()])
