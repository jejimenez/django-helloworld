# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pooling', '0002_auto_20150508_2348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weight', models.IntegerField()),
                ('start_distance', models.FloatField()),
                ('end_distance', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='seeker',
            name='end_point',
        ),
        migrations.RemoveField(
            model_name='seeker',
            name='start_point',
        ),
        migrations.AddField(
            model_name='driver',
            name='description',
            field=models.TextField(null=True, verbose_name=b'description', blank=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='rout_bound_ne_lat',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='rout_bound_ne_lng',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='rout_bound_sw_lat',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='rout_bound_sw_lng',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='rout_distance',
            field=models.CharField(max_length=50, null=True, verbose_name=b'rout_duration'),
        ),
        migrations.AddField(
            model_name='driver',
            name='rout_duration',
            field=models.CharField(max_length=50, null=True, verbose_name=b'rout_duration'),
        ),
        migrations.AddField(
            model_name='driver',
            name='rout_end_address',
            field=models.TextField(null=True, verbose_name=b'rout_end_address', blank=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='rout_end_lat',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='rout_end_lng',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='rout_overviewpolilyne',
            field=models.TextField(null=True, verbose_name=b'rout_overviewpolilyne', blank=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='rout_start_address',
            field=models.TextField(null=True, verbose_name=b'rout_start_address', blank=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='rout_start_lat',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='rout_start_lng',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='driver',
            name='rout_sumary',
            field=models.TextField(null=True, verbose_name=b'rout_sumary', blank=True),
        ),
        migrations.AddField(
            model_name='seeker',
            name='end_lat',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='seeker',
            name='end_lnt',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='seeker',
            name='start_lat',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='seeker',
            name='start_lng',
            field=models.DecimalField(null=True, max_digits=19, decimal_places=10, blank=True),
        ),
        migrations.AddField(
            model_name='weight',
            name='driver',
            field=models.ForeignKey(related_name='weight_driver', verbose_name=b'driver', to='pooling.Driver'),
        ),
        migrations.AddField(
            model_name='weight',
            name='seeker',
            field=models.ForeignKey(related_name='weight_seeker', verbose_name=b'seeker', to='pooling.Seeker'),
        ),
    ]
