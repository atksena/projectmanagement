from rest_framework import serializers
from .models import Task, IssueType

class TaskSerializer(serializers.ModelSerializer):
    issue_type__name = serializers.CharField(read_only=True, source="issue_type.name")

    class Meta:
        model = Task
        fields = '__all__'

class IssueTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = IssueType
        fields = '__all__'
