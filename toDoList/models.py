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
