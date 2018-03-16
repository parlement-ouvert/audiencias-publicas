# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-10 10:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20170807_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='RoomAttachment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='title')),
                ('url', models.URLField(verbose_name='link')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attachments', to='core.Room', verbose_name='room')),
            ],
            options={
                'verbose_name': 'attachment',
                'verbose_name_plural': 'attachments',
            },
        ),
    ]