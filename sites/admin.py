from django.contrib import admin

# Register your models here.]
from website.sites.models import  Post




@admin.register(Post)
class TestAdmin2(admin.ModelAdmin):
    pass