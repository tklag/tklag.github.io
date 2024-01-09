from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=64)
    details = models.TextField(max_length=256)
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.name}"