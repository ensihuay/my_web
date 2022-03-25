from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _

from useradmin.managers import UserManager


class User(AbstractUser):
    # User's username
    username = None

    # User's email
    email = models.EmailField(
        _('email address'),
        unique=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

class Login(models.Model):

    email = models.EmailField()
    date_login = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email