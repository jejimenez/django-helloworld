# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('world', '0002_zipcode'),
    ]

    operations = [
        migrations.CreateModel(
            name='SouthTexasCity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('point', django.contrib.gis.db.models.fields.PointField(srid=32140)),
            ],
        ),
        migrations.AlterField(
            model_name='worldborder',
            name='fips',
            field=models.CharField(verbose_name='FIPS Code', max_length=2),
        ),
        migrations.AlterField(
            model_name='worldborder',
            name='iso2',
            field=models.CharField(verbose_name='2 Digit ISO', max_length=2),
        ),
        migrations.AlterField(
            model_name='worldborder',
            name='iso3',
            field=models.CharField(verbose_name='3 Digit ISO', max_length=3),
        ),
        migrations.AlterField(
            model_name='worldborder',
            name='pop2005',
            field=models.IntegerField(verbose_name='Population 2005'),
        ),
        migrations.AlterField(
            model_name='worldborder',
            name='region',
            field=models.IntegerField(verbose_name='Region Code'),
        ),
        migrations.AlterField(
            model_name='worldborder',
            name='subregion',
            field=models.IntegerField(verbose_name='Sub-Region Code'),
        ),
        migrations.AlterField(
            model_name='worldborder',
            name='un',
            field=models.IntegerField(verbose_name='United Nations Code'),
        ),
    ]
