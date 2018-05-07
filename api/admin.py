# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from api.models import Pomodoro, Task


admin.site.register(Pomodoro)
admin.site.register(Task)