# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-29 03:46
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='userWebsite',
            field=models.CharField(default=datetime.datetime(2016, 9, 29, 3, 46, 57, 868537, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
    ]
