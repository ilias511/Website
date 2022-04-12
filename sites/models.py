import math

from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import models as auth_models, get_user_model
from django.db import models
from sites.managers import AppUsersManager
from django.core.validators import MinLengthValidator, MinValueValidator

POST_CHOICES = [
    ("Sport", "Sport"),
    ("Politics", "Politics"),
    ("Article", "Article"),
    ("Fun Fact", "Fun Fact"),
    ("International News", "International News"),
    ("Joke", "Joke"),
    ("Crypto", "Crypto"),
    ("Gaming", "Gaming"),
    ("Movies", "Movies"),
    ("Other", "Other")]

USERNAME_MAX_LENGTH = 30
USERNAME_MIN_LENGTH = 3
AGE_MIN_VALUE = 1

POST_TITLE_MAX_LENGTH = 50
POST_CATEGORY_MAX_LENGTH = 100

IMAGE_TITLE_MAX_LENGTH = 50




# AUTH USER MODEL
class AppUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False,
    )

    is_staff = models.BooleanField(
        default=False,
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
    )
    USERNAME_FIELD = 'email'

    objects = AppUsersManager()


# PROFILE MODEL
class AppUsername(models.Model):
    username = models.CharField(max_length=USERNAME_MAX_LENGTH, unique=True,
                                validators=[MinLengthValidator(USERNAME_MIN_LENGTH), ])
    age = models.IntegerField(validators=[MinValueValidator(AGE_MIN_VALUE)])
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, primary_key=True)


# POSTS MODEL
class Post(models.Model):
    title = models.CharField(max_length=POST_TITLE_MAX_LENGTH, )
    details = models.TextField()
    category = models.CharField(max_length=POST_CATEGORY_MAX_LENGTH, choices=POST_CHOICES)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)


class Images(models.Model):
    title = models.CharField(max_length=IMAGE_TITLE_MAX_LENGTH)
    image = models.URLField()
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)

#admin
class AdminUser(models.Model):
    username = models.CharField(max_length=USERNAME_MAX_LENGTH)