from rest_framework import serializers

from api.models import Task, Pomodoro


class TaskSerializer(serializers.ModelSerializer):
    count = serializers.IntegerField(source="pomodoro_count", required=False)

    class Meta:
        model = Task
        fields = ('id', 'title', 'created', 'started', 'done', 'count')


class PomodoroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pomodoro
        fields = ('__all__')