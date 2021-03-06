# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-10 14:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import journal.models
import journal.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('journal', '0007_auto_20170708_1417'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('appropriate', models.CharField(blank=True, choices=[('appropriate', 'The topic of this manuscript falls within the scope of the journal.'), ('not_appropriate', 'The topic of this manuscript does not fall within the scope of the journal.')], default=None, max_length=64)),
                ('recommendation', models.CharField(blank=True, choices=[('0', 'Consider after Major Changes.'), ('+2', 'Publish Unaltered.'), ('+1', 'Consider after Minor Changes.'), ('-1', 'Reject. (Paper is not of sufficient quality or novelty to be published in this journal)'), ('-2', 'Reject. (Paper is seriously flawed; Do not encourage resubmission)')], default=None, max_length=64)),
                ('comment', models.TextField(blank=True, help_text='This comment will be shown to the author.', max_length=32768)),
                ('confidential_comment', models.TextField(blank=True, help_text='This comment will not be shown to the author.', max_length=32768)),
                ('additional_file', models.FileField(blank=True, upload_to=journal.models.review_user_id_path, validators=[journal.validators.FileValidator(content_types=('application/pdf', 'text/html', 'application/msword', 'application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'text/plain'), max_size=52428800)])),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.AddField(
            model_name='paper',
            name='reviewers',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='paper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='journal.Paper'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to=settings.AUTH_USER_MODEL),
        ),
    ]
