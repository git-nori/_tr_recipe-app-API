# Generated by Django 2.1.15 on 2020-04-05 02:58

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200404_1413'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='images',
            field=models.ImageField(null=True, upload_to=core.models.recipe_image_file_path),
        ),
    ]
