from django.db import models

# Create your models here.

POST_CHOICES = [
    # ("------------", "------------"),
    ("Sport", "Sport"),
    ("Politics", "Politics"),
    ("Crypto", "Crypto"),
    ("Gaming", "Gaming"),
    ("Movies", "Movies"),
    ("Other", "Other")]


class User(models.Model):
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=29)

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    category = models.CharField(max_length=100, choices=POST_CHOICES)

    def __str__(self):
        return self.title
