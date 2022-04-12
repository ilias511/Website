from django.contrib import admin

# Register your models here.]


from sites.models import AppUser
from django.contrib.auth.admin import UserAdmin


@admin.register(AppUser)
class TestAdmin2(admin.ModelAdmin):
    list_display = ('email',)



