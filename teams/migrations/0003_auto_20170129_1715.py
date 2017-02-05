# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-29 16:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0002_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='flag',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='team',
            name='flag',
            field=models.URLField(blank=True),
        ),
    ]
