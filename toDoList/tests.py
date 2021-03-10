from django.test import TestCase
from django.urls import reverse
from .models import EventType, Event
from django.contrib.auth.models import User
from .views import typelist
import datetime
from django.utils import timezone
from .form import EventForm
# Create your tests here.


class EventTypeTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.testUser = User.objects.create(
            username='hank', password="1234qwer")

        cls.testEventType = EventType.objects.create(
            name="Home", color="#0002165", createdByUser=cls.testUser)

    def test_string(self):
        self.assertEqual(str(self.testEventType), self.testEventType.name)

    def test_table(self):
        self.assertEqual(str(EventType._meta.db_table), 'EventType')

    def test_view_url_accessible_by_name(self):
        self.client.force_login(self.testUser)

        response = self.client.get(reverse('typelist'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('typesave'))
        self.assertEqual(response.status_code, 200)

    def test_eventtype_form_request_login(self):
        response = self.client.get('/todolist/typesave')
        self.assertRedirects(
            response, '/todolist/login?next=/todolist/typesave')

    def test_eventtype_list_view(self):
        self.client.force_login(self.testUser)
        response = self.client.get('/todolist/typelist')
        self.assertEqual(response.resolver_match.func, typelist)

    def test_resource_form_templates_context(self):
        # login
        self.client.force_login(self.testUser)
        response = self.client.get('/todolist/typelist')
        self.assertIsNone(response.context["msg"])


class EventTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.testUser = User.objects.create(
            username='hank', password="1234qwer")

        cls.testEventType = EventType.objects.create(
            name="Home", color="#0002165", createdByUser=cls.testUser)

        cls.testEvent = Event.objects.create(
            title="test_title",
            time=datetime.datetime.now(tz=timezone.utc),
            description="test_description",
            eventType=cls.testEventType,
            createdByUser=cls.testUser)

    def test_string(self):
        self.assertEqual(str(self.testEvent), self.testEvent.title)

    def test_table(self):
        self.assertEqual(str(Event._meta.db_table), 'Event')

    def test_event_list_templates_used(self):
        # login
        self.client.force_login(self.testUser)
        response = self.client.get('/todolist/index')
        self.assertTemplateUsed("index.html")

    def test_event_form_is_valid(self):
        form = EventForm(
            data={'title': "test_title"})
        self.assertFalse(form.is_valid())
