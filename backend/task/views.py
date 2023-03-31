from rest_framework import generics
from .models import Task, IssueType
from .serializers import TaskSerializer, IssueTypeSerializer

class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

class IssueTypeListCreateAPIView(generics.ListCreateAPIView):
    queryset = IssueType.objects.all()
    serializer_class = IssueTypeSerializer

# class IssueTypeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = IssueType.objects.all()
#     serializer_class = IssueTypeSerializer