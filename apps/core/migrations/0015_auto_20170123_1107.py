# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-23 13:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20170116_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='max_online_users',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='video',
            name='online_users',
            field=models.IntegerField(default=0),
        ),
    ]
