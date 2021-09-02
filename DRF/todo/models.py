from django.db import models
from django.db.models.fields import CharField

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=50)
    completed = models.BooleanField(null=True, blank=True, default=False)

    def __str__(self):
        return self.title
