# Generated by Django 4.0.3 on 2022-03-16 21:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0005_rename_user_post_usera'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='usera',
            new_name='user',
        ),
    ]
