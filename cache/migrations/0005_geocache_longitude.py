# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-02 20:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cache', '0004_geocache_latitude'),
    ]

    operations = [
        migrations.AddField(
            model_name='geocache',
            name='longitude',
            field=models.FloatField(default=0.0),
        ),
    ]