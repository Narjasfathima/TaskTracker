from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils import timezone


USER_TYPE_CHOICES = (
    ('Admin', 'Admin'),
    ('User', 'User')
)

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=100, choices=USER_TYPE_CHOICES)

    def __str__(self):
        return self.username
    

TASK_STATUS = (
    ('Pending', 'Pending'),
    ('In Progress', 'In Progress'),
    ('Completed', 'Completed')
)


class Task(models.Model):    
    task_id = models.CharField(max_length=100, unique=True, editable=False, default=uuid.uuid4)
    title = models.CharField(max_length=250)
    assigned_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    due_date = models.DateField()
    status = models.CharField(max_length=100, choices=TASK_STATUS)
    completion_report = models.TextField(blank=True, null=True)
    worked_hours = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.task_id