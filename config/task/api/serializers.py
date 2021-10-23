from django.utils import timezone
from rest_framework import serializers

from task.models import Comment, Project, Reminder, Task


# class ProjectSerializer(serializers.ModelSerializer):
#   class Meta: 
#     model = Project
#     fields = ['id', 'name', 'description']



class ProjectSerializer(serializers.ModelSerializer):
  manager = serializers.ReadOnlyField(source='manager.username')

  class Meta:
    model = Project
    fields = ['id', 'name','manager', 'description', 'tasks_ids']
    read_only_fields = ['id', 'tasks_ids']


class TaskSerializer(serializers.ModelSerializer):
  # user = serializers.ReadOnlyField(source='user.username')
  # project = serializers.ReadOnlyField(source='project.name')
  # if not commenting above then not getting user and project fields in front if i don't then getting 
  # ID of user and project instead of name of project

  class Meta:
    # lookup_field = 'id'
    model = Task
    fields = ('id', 'project', 'user', 'title', 'description',
              'deadline', 'priority', 'status', 'created_at', 'updated_at', 'reminders_ids', 'comments_ids')

    read_only_fields = ('id', 'reminders_ids', 'comments_ids')

    def validate_deadline(self, value):
        if (timezone.now() > value):
            raise serializers.ValidationError('deadline must be in the future.')
        return value


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        lookup_field = 'id'
        model = Comment
        fields = ['id',  'task', 'user', 'created_at', 'updated_at', 'comment']
        read_only_fields = ('id',)


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        lookup_field = 'id'
        model = Reminder
        fields = ('id','task', 'date')
        read_only_fields = ('id',)

    def validate_date(self, value):
        if (timezone.now() > value):
            raise serializers.ValidationError('date must be in the future.')
        return value
