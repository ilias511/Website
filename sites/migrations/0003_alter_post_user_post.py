# Generated by Django 4.0.3 on 2022-03-15 17:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_remove_appusername_id_appusername_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='user_post',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]