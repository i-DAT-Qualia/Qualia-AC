# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-06 15:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('artcasting', '0006_auto_20160406_1557'),
    ]

    operations = [
        migrations.AddField(
            model_name='cast',
            name='sender',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='artcasting.User'),
        ),
    ]
