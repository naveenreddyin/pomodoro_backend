# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics

from api.models import Task, Pomodoro
from api.serializers import TaskSerializer, PomodoroSerializer


def home(request):
    return render(request, "api/index.html")


# This class is to for tasks and its related operations
class TaskModelView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


# This class is to get Pomodoro timer settings
class PomodoroView(viewsets.ModelViewSet):
    serializer_class = PomodoroSerializer

    def get_queryset(self):
        queryset = Pomodoro.objects.all()
        return queryset