from django.db import models


class IssueType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    class Priority(models.TextChoices):
        LOW = 'low', 'Low'
        MEDIUM = 'medium', 'Medium'
        HIGH = 'high', 'High'
        HIGHEST = 'highest', 'Highest'

    summary = models.CharField(max_length=100)
    description = models.TextField(null=True)
    priority = models.CharField(choices=Priority.choices, max_length=7, default=0)
    issue_type = models.ForeignKey(IssueType, on_delete=models.CASCADE)
