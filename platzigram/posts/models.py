""" Posts Models """

#Django
from django.db import models


class User(models.Model):
    """ User Model """

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    is_admin = models.BooleanField(default=False)

    bio = models.TextField(blank=True)

    birthdate = models.DateField(blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    country = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)

    def __str__(self):
        """ Return Email """
        return self.email