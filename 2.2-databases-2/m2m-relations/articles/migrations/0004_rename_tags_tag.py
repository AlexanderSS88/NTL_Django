# Generated by Django 4.1 on 2022-08-17 21:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_scope_alter_tags_scope_delete_scopes'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
    ]
