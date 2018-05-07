# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-06 12:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20180506_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='pomodoro_count',
            field=models.IntegerField(blank=True, default=0, help_text='Count of finished pomodoros by this task.'),
        ),
    ]
