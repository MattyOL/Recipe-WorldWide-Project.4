# Generated by Django 3.2.18 on 2023-05-17 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_dish_post_excerpt'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='excerpt',
            new_name='dish',
        ),
    ]
