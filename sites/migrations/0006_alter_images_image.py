# Generated by Django 4.0.3 on 2022-04-04 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0005_alter_images_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='image',
            field=models.URLField(),
        ),
    ]
