from django.db import models
from django.utils import timezone


# Create your models here.
class Task(models.Model):
    content = models.TextField()
    complete = models.BooleanField(default=False)
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.content

