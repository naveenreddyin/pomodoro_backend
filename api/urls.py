from django.conf.urls import include, url
from rest_framework import routers

from api.views import TaskModelView, PomodoroView

task_router = routers.DefaultRouter()
task_router.register(r'task', TaskModelView, base_name='tasks')

pomodoro_router = routers.DefaultRouter()
pomodoro_router.register(r'pomodoro', PomodoroView, base_name='pomodoro')


urlpatterns = [
    url(r'^', include(task_router.urls), name="task"),
    url(r'^', include(pomodoro_router.urls), name="pomodoro"),
]