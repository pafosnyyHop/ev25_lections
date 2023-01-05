from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField(blank=True)
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'


