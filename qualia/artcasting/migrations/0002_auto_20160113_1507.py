# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-13 15:07
from __future__ import unicode_literals

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artcasting', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cast',
            name='destination',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='cast',
            name='origin',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AlterField(
            model_name='user',
            name='postcode_geolocation',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
    ]