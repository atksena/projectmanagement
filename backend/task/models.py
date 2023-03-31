from django.db import models

class IssueType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    
    def __str__(self):
        return self.name

class Task(models.Model):
    PriorityChoices = [
        (0, 'Low'),
        (1, 'Medium'),
        (2, 'High'),
    ]
    summary = models.CharField(max_length=100)
    description = models.TextField(null=True)
    priority = models.SmallIntegerField(choices=PriorityChoices, default=0)
    issue_type = models.BigIntegerField(null=True)
