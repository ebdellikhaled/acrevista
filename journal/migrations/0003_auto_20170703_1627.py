# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-03 16:27
from __future__ import unicode_literals

from django.contrib.auth.management import create_permissions
from django.contrib.auth.models import Permission
from django.db import migrations, models
import journal.validators


# This will create the reviwers group.
def create_reviewers_group(apps, schema):
    groups = apps.get_model("auth", "Group")
    group, created = groups.objects.get_or_create(name='Reviewer')


class Migration(migrations.Migration):

    dependencies = [
        ('journal', '0002_auto_20170628_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='file',
            field=models.FileField(upload_to='papers', validators=[journal.validators.FileValidator(content_types=('application/pdf', 'text/html', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'application/vnd.ms-powerpoint', 'application/vnd.openxmlformats-officedocument.presentationml.presentation', 'text/plain'), max_size=52428800)]),
        ),
        migrations.RunPython(create_reviewers_group),
    ]
