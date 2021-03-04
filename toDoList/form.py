from .models import EventType
from django.forms import ModelForm, TextInput


class EventTypeForm(ModelForm):
    class Meta:
        model = EventType
        fields = '__all__'
        exclude = ['createdByUser']
        widgets = {
            'name': TextInput(attrs={"class": "form-control"}),
            'color': TextInput(attrs={"type": "color"}),
        }
