# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 11:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artcasting', '0003_user_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='encounters',
            field=models.IntegerField(default=0),
        ),
    ]