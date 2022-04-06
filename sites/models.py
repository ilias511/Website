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
    username = models.CharField(max_length=20, unique=True, validators=[MinLengthValidator(3), ])
    age = models.IntegerField(validators=[MinValueValidator(1)])
    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, primary_key=True)


# POSTS MODEL
class Post(models.Model):
    title = models.CharField(max_length=50, )
    details = models.TextField()
    category = models.CharField(max_length=100, choices=POST_CHOICES)
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)


class Images(models.Model):
    title = models.CharField(max_length=50)
    image = models.URLField()
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
