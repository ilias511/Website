from django.contrib import admin

# Register your models here.]
from website.sites.models import User, Post


@admin.register(User)
class TestAdmin(admin.ModelAdmin):
    pass

@admin.register(Post)
class TestAdmin2(admin.ModelAdmin):
    pass