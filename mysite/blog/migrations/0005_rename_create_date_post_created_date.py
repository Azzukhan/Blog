# Generated by Django 4.1 on 2022-11-08 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_remove_comment_create_date_comment_created_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create_date',
            new_name='created_date',
        ),
    ]
