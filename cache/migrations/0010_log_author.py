# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-16 19:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cache', '0009_geocache_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='log',
            name='author',
            field=models.CharField(default=None, max_length=128),
        ),
    ]
