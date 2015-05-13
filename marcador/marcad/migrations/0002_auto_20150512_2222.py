# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('marcad', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='date_created',
            field=models.DateTimeField(verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='date_updated',
            field=models.DateTimeField(verbose_name='date updated'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='description',
            field=models.TextField(blank=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='is_public',
            field=models.BooleanField(verbose_name='public', default=True),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='owner',
            field=models.ForeignKey(related_name='bookmarks', verbose_name='owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='title',
            field=models.CharField(verbose_name='title', max_length=255),
        ),
    ]
