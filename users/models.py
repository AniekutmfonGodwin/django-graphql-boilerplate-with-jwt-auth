from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.
# users/models.py

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(_("Email address"),blank=False, max_length=254,unique=True)

    REQUIRED_FIELDS = [ 'username',]

    USERNAME_FIELD = "email"   # e.g: "username", "email"
    EMAIL_FIELD = "email"         # e.g: "email", "primary_email"

    def __str__(self):
        return self.email