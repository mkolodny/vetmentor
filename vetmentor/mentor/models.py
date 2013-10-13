from __future__ import unicode_literals

from datetime import datetime
from django.utils.timezone import utc
from django.contrib.auth.models import AbstractBaseUser
from django.db import models


class User(AbstractBaseUser):
    name = models.TextField()
    email = models.TextField(db_index=True) # unique
    birthday = models.DateField()
    MALE = 0
    FEMALE = 1
    GENDER_TYPES = (
        (MALE, 'male'),
        (FEMALE, 'female'),
    )
    gender = models.SmallIntegerField(choices=GENDER_TYPES)
    VETERAN = 0
    CIVILIAN = 1
    CATEGORY_TYPES = (
        (VETERAN, 'veteran'),
        (CIVILIAN, 'civilian'),
    )
    category = models.SmallIntegerField(choices=CATEGORY_TYPES)
    location = models.TextField()
    bio = models.TextField(null=True)
    why_joined = models.TextField(null=True)
    industry = models.ForeignKey('Industry', to_field='id', on_delete=models.PROTECT)
    date_joined = models.DateField(default=datetime.utcnow().replace(tzinfo=utc))

    # vet-only fields
    rank = models.TextField(null=True)
    service_location = models.TextField(null=True)
    service_start_date = models.DateField(null=True)
    service_end_date = models.DateField(null=True)
    HS = 0
    COLLEGE = 1
    GRAD = 2
    EDUCATION_TYPES = (
        (HS, 'high school'),
        (COLLEGE, 'college'),
        (GRAD, 'grad school'),
    )
    education = models.SmallIntegerField(null=True, choices=EDUCATION_TYPES)

    class Meta:
        db_table = 'users'


class Industry(models.Model):
    title = models.TextField()
    code = models.SmallIntegerField()

    class Meta:
        db_table = 'industries'
