from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class EventType(models.Model):
    name = models.CharField(max_length=200)
    color = models.CharField(max_length=200)
    createdTime = models.DateTimeField(auto_now_add=True)
    createdByUser = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'EventType'
        verbose_name_plural = 'EventTypes'
        ordering = ["createdTime"]


class Event(models.Model):
    title = models.CharField(max_length=200)
    time = models.DateTimeField()
    description = models.TextField()
    eventType = models.ForeignKey(EventType, on_delete=models.CASCADE)
    createdByUser = models.ForeignKey(User, on_delete=models.CASCADE)
    createdTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Event'
        verbose_name_plural = 'Events'
        ordering = ["createdTime"]
