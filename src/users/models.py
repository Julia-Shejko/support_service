from django.contrib.auth.models import AbstractBaseUser
from django.db import models

# id
# password
# last_login
# activated (or is_active)

# email
# first_name
# last_name


class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    activated = models.BooleanField(default=True)

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
