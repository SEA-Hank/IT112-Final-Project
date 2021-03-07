from django.contrib import admin
from .models import EventType, Event

# Register your models here.
admin.site.register(EventType)
admin.site.register(Event)
