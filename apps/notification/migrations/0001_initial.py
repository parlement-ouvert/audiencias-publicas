# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-10-16 16:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0004_auto_20170807_1637'),
    ]

    operations = [
        migrations.CreateModel(
            name='ParticipantNotification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('emails', models.TextField()),
                ('subject', models.CharField(max_length=100, verbose_name='subject')),
                ('content', models.TextField(verbose_name='content')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Room', verbose_name='room')),
            ],
            options={
                'verbose_name': 'participant notification',
                'verbose_name_plural': 'participants notifications',
            },
        ),
    ]