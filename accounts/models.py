## Extends the existing AbstractUser
# DOC recomment use AbstractBaseUser not AbstractUser
# But for easy custom same add fields and not change other fields: username, password, email,... let's use AbstractUser for easier
from django.contrib.auth.models import AbstractUser # 3.2
from django.db import models

class CustomUser(AbstractUser): # 3.2
    # We can use both null and blank for age field
    age = models.PositiveIntegerField(null=True, blank=True)

