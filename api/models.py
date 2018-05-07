# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    created = models.DateTimeField(auto_now_add=True, blank=True)
    started = models.BooleanField(default=False, blank=True)
    done = models.BooleanField(default=False, blank=True)
    pomodoro_count = models.IntegerField(help_text="Count of finished pomodoros by this task.",
                                         default=0, blank=True)

    def __unicode__(self):
        return u'%s' % self.title


class Pomodoro(models.Model):
    pomodoro_timer = models.IntegerField(help_text="Set pomodoro timer, defaults to 25 minutes",
                                         default=25)
    break_timer = models.IntegerField(help_text="Set break time, defaults to 5 minutes until 4 pomodoros.",
                                      default=5)
    big_break_timer = models.IntegerField(help_text="Set break time after 4 pomodoros are finished, "
                                                    "defaults to 15 minutes",
                                          default=15)