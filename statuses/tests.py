from django.contrib.messages import get_messages
from django.core.exceptions import ObjectDoesNotExist
from django.test import TestCase
from django.urls import reverse
from statuses.models import Status
from task_manager.utils import get_test_data
from tasks.models import Task
from users.models import User


class StatusTest(TestCase):
    fixtures = ['statuses.json', 'users.json', 'tasks.json', 'labels.json']

    @classmethod
    def setUpTestData(cls):
        cls.test_data = get_test_data()
        cls.status = Status.objects.get(pk=1)
        cls.used_status = Status.objects.get(pk=3)
        cls.user = User.objects.get(pk=1)
        cls.task = Task.objects.get(pk=1)
        cls.statuses_url = reverse('statuses')

    def assertStatus(self, status, status_data):
        self.assertEqual(status.__str__(), status_data['name'])
        self.assertEqual(status.name, status_data['name'])

    def test_status_page(self):
        self.client.force_login(self.user)
        response = self.client.get(self.statuses_url)
        self.assertEqual(response.status_code, 200)

        statuses = Status.objects.all()
        self.assertQuerysetEqual(
            response.context['status_list'],
            statuses,
            ordered=False,
        )

    def test_status_create_page(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('create_status'))
        self.assertEqual(response.status_code, 200)

    def test_create_status(self):
        self.client.force_login(self.user)
        new_status_data = self.test_data['statuses']['new']
        response = self.client.post(reverse(
            'create_status'), new_status_data)
        self.assertRedirects(response, self.statuses_url)
        created_status = Status.objects.get(name=new_status_data['name'])
        self.assertStatus(created_status, new_status_data)

    def test_update_status_page(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse('update_status', args=(self.status.pk, ))
        )
        self.assertEqual(response.status_code, 200)

    def test_update_status(self):
        self.client.force_login(self.user)
        new_status_data = self.test_data['statuses']['new']
        response = self.client.post(reverse(
            'update_status', args=[self.status.pk]), new_status_data)
        self.assertRedirects(response, self.statuses_url)
        updated_status = Status.objects.get(name=new_status_data['name'])
        self.assertStatus(updated_status, new_status_data)

    def test_delete_page(self):
        self.client.force_login(self.user)
        response = self.client.get(
            reverse('delete_status', args=(self.user.pk, ))
        )
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse(
            'delete_status', args=(self.status.pk,)))
        self.assertRedirects(response, self.statuses_url)
        with self.assertRaises(ObjectDoesNotExist):
            Status.objects.get(name=self.status.name)

    def test_delete_used_status(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse(
            'delete_status', args=(self.used_status.pk,)))
        self.assertRedirects(response, self.statuses_url)
        assert self.used_status in Status.objects.all()
        self.assertEqual(1, len(list(get_messages(response.wsgi_request))))
