from rest_framework.viewsets import ModelViewSet
from .models import Task, IssueType
from .serializers import TaskSerializer, IssueTypeSerializer

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# class TaskRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

class IssueTypeListCreateAPIView(ModelViewSet):
    queryset = IssueType.objects.all()
    serializer_class = IssueTypeSerializer

# class IssueTypeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = IssueType.objects.all()
#     serializer_class = IssueTypeSerializer