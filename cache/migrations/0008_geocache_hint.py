# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-08 03:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cache', '0007_log_geocache'),
    ]

    operations = [
        migrations.AddField(
            model_name='geocache',
            name='hint',
            field=models.TextField(default='None provided.'),
        ),
    ]