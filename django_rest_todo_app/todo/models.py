from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title
