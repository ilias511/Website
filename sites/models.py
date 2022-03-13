from django.contrib.auth import models as auth_models
from django.db import models

# Create your models here.
from website.sites.managers import AppUsersManager

POST_CHOICES = [
    ("Sport", "Sport"),
    ("Politics", "Politics"),
    ("Crypto", "Crypto"),
    ("Gaming", "Gaming"),
    ("Movies", "Movies"),
    ("Other", "Other")]


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


class AppUsername(models.Model):
    username = models.CharField(max_length=20)
    age = models.CharField(max_length=2)

    user = models.OneToOneField(AppUser, on_delete=models.CASCADE, primary_key=True)


# class User(models.Model):
#     password = models.CharField(max_length=29)


class Post(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    category = models.CharField(max_length=100, choices=POST_CHOICES)

    def __str__(self):
        return self.title
