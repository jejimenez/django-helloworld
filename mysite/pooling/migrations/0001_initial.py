# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('json_way', models.TextField(verbose_name=b'json_way')),
                ('schedule', models.TextField(verbose_name=b'schedule', blank=True)),
                ('user', models.ForeignKey(related_name='Usuario_Driver', verbose_name=b'Usuario_Driver', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Seeker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_point', models.TextField(verbose_name=b'start_point')),
                ('end_point', models.TextField(verbose_name=b'end point')),
                ('schedule', models.TextField(verbose_name=b'schedule')),
                ('user', models.ForeignKey(related_name='Usuario_Seeker', verbose_name=b'Usuario_Seeker', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
