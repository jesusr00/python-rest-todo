from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.


class Todo(models.Model):

    TODO_STATE = (
        ('T', 'To Do'),
        ('P', 'In Progress'),
        ('D', 'Done')
    )

    title = models.CharField(max_length=200)
    description = models.TextField()
    end_date = models.DateField()
    state = models.CharField(max_length=1, choices=TODO_STATE)
    created_at = models.DateTimeField(auto_now_add=True)
