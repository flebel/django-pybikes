# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 22:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bikeshares', '0006_remove_bikesharesystem_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='bikesharesystem',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
