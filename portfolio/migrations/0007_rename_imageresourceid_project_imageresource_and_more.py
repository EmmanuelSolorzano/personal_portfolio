# Generated by Django 4.1.7 on 2023-02-23 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_rename_imageresource_project_imageresourceid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='imageResourceID',
            new_name='imageResource',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='youtubeResource',
            new_name='youtubeResourceID',
        ),
    ]
