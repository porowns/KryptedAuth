# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-19 18:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_game_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='date_created',
            field=models.DateField(auto_now=True),
        ),
    ]