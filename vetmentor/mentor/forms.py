from __future__ import unicode_literals

from wtforms import Form, TextField, IntegerField, DateField
from wtforms.validators import Required, Optional, AnyOf
from vetmentor.mentor.models import User

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
