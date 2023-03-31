from rest_framework import serializers
from .models import Task, IssueType

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

class IssueTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueType
        fields = '__all__'
