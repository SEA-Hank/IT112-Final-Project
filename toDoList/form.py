from .models import EventType, Event
from django.forms import ModelForm, TextInput, Textarea, Select, SplitDateTimeWidget
from django import forms


class mySplitDateTimeField(forms.SplitDateTimeField):
    widget = forms.SplitDateTimeWidget(date_attrs={
        "type": "date", "class": "form-control"}, time_attrs={"type": "time", "class": "form-control"})


class EventTypeForm(ModelForm):
    class Meta:
        model = EventType
        fields = '__all__'
        exclude = ['createdByUser']
        widgets = {
            'name': TextInput(attrs={"class": "form-control"}),
            'color': TextInput(attrs={"type": "color", "class": "form-control form-control-color"}),
        }


class EventForm(ModelForm):
    field_order = ["eventType", "title", "time", "description"]
    time = mySplitDateTimeField()

    class Meta:
        model = Event
        fields = '__all__'
        exclude = ['createdByUser']
        widgets = {
            'title': TextInput(attrs={"class": "form-control"}),
            'time': SplitDateTimeWidget(date_attrs={"type": "date", "class": "form-control"}, time_attrs={"type": "time", "class": "form-control"}),
            "description": Textarea(attrs={"class": "form-control", "rows": 6}),
            "eventType": Select(attrs={"class": "form-select"})
        }
