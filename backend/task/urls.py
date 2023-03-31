"""task_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import TaskListCreateAPIView, IssueTypeListCreateAPIView

urlpatterns = [
    path('', TaskListCreateAPIView.as_view(), name='task_list_create'),
    path('tasks/', TaskListCreateAPIView.as_view(), name='task_list_create'),
    # path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyAPIView.as_view(), name='task_retrieve_update_destroy'),
    path('issue-types/', IssueTypeListCreateAPIView.as_view(), name='issue_type_list_create'),
    # path('issue-types/<int:pk>/', IssueTypeRetrieveUpdateDestroyAPIView.as_view(), name='issue_type_retrieve_update_destroy'),
]
