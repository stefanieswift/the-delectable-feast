# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-18 15:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_userbios'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserBios',
            new_name='Bios',
        ),
    ]
