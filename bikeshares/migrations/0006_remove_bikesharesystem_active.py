# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 22:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bikeshares', '0005_auto_20160726_2211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bikesharesystem',
            name='active',
        ),
    ]
