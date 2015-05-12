# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pooling', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='seeker',
            name='description',
            field=models.TextField(verbose_name=b'description', blank=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='schedule',
            field=models.CharField(max_length=7, verbose_name=b'schedule'),
        ),
        migrations.AlterField(
            model_name='seeker',
            name='end_point',
            field=models.CharField(max_length=255, verbose_name=b'end point'),
        ),
        migrations.AlterField(
            model_name='seeker',
            name='schedule',
            field=models.CharField(max_length=7, verbose_name=b'schedule'),
        ),
        migrations.AlterField(
            model_name='seeker',
            name='start_point',
            field=models.CharField(max_length=255, verbose_name=b'start_point'),
        ),
    ]
