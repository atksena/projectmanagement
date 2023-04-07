from rest_framework.generics import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from .models import Task, IssueType
from .serializers import TaskSerializer, IssueTypeSerializer

class PostBodyViewSet(ModelViewSet):
    def get_object(self):
        """
        Overridden to work with POST body instead of url variable.
        """
        queryset = self.filter_queryset(self.get_queryset())

        filter_kwargs = {self.lookup_field: self.request.data.get(self.lookup_field)}
        obj = get_object_or_404(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj

class TaskViewSet(PostBodyViewSet):
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class IssueTypeViewSet(PostBodyViewSet):
    lookup_field = 'id'
    lookup_url_kwarg = 'id'
    queryset = IssueType.objects.all()
    serializer_class = IssueTypeSerializer

