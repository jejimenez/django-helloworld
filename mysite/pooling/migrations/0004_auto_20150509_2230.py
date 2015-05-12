# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pooling', '0003_auto_20150509_2212'),
    ]

    operations = [
        migrations.CreateModel(
            name='Leg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('driver', models.ForeignKey(related_name='leg', verbose_name=b'driver', to='pooling.Driver')),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_lat', models.DecimalField(max_digits=19, decimal_places=10)),
                ('start_lng', models.DecimalField(max_digits=19, decimal_places=10)),
                ('end_lat', models.DecimalField(max_digits=19, decimal_places=10)),
                ('end_lng', models.DecimalField(max_digits=19, decimal_places=10)),
                ('polyline', models.TextField(verbose_name=b'polyline', blank=True)),
                ('duration', models.CharField(max_length=50, null=True, verbose_name=b'rout_duration')),
                ('html_instruction', models.TextField(verbose_name=b'html_instruction', blank=True)),
                ('distance', models.CharField(max_length=50, null=True, verbose_name=b'rout_duration')),
                ('leg', models.ForeignKey(related_name='step', verbose_name=b'leg', to='pooling.Leg')),
            ],
        ),
        migrations.AlterField(
            model_name='seeker',
            name='user',
            field=models.ForeignKey(related_name='Usuario_Seeker', verbose_name=b'Usuario Seeker', to=settings.AUTH_USER_MODEL),
        ),
    ]
