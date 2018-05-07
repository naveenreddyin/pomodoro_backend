# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase

from api.models import Task, Pomodoro


class ApiTests(APITestCase):

    def test_index_view(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_tasks_model(self):
        tasks = Task.objects.create(title="First task")
        self.assertIsNotNone(tasks.created)
        self.assertFalse(tasks.started)
        self.assertFalse(tasks.done)
        self.assertEqual(tasks.pomodoro_count, 0)

    def test_task_model_view(self):
        response = self.client.get("/api/task/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        response = self.client.post("/api/task/", data={"title": "second task"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_task(self):
        task = Task.objects.create(title="First task")
        response = self.client.put("/api/task/%s/" % task.id, data={"title": "second task"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task = get_object_or_404(Task, pk=task.id)
        self.assertEqual(task.title, "second task")
        self.assertFalse(task.started)

    def test_update_task_started(self):
        task = Task.objects.create(title="First task")
        response = self.client.patch("/api/task/%s/" % task.id, data={"started": "true"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task = get_object_or_404(Task, pk=task.id)
        self.assertTrue(task.started)

    def test_patch_task_done(self):
        task = Task.objects.create(title="First task")
        response = self.client.patch("/api/task/%s/" % task.id, data={"done": "true"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task = get_object_or_404(Task, pk=task.id)
        self.assertTrue(task.done)

    # test pomodoro timer and break timer settings
    def test_pomodoro_model(self):
        pomodoro = Pomodoro.objects.create(pomodoro_timer=25, break_timer=5, big_break_timer=15)
        self.assertEqual(pomodoro.pomodoro_timer,25)

    # test pomodoro api
    def test_pomodoro_api(self):
        response = self.client.get("/api/pomodoro/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # test count update
    def test_task_count_update(self):
        task = Task.objects.create(title="First task")
        self.assertEqual(task.pomodoro_count, 0)
        response = self.client.patch("/api/task/%s/" % task.id, data={"count": 4}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # it should now be 4
        task = get_object_or_404(Task, pk=task.id)
        self.assertEqual(task.pomodoro_count, 4)


