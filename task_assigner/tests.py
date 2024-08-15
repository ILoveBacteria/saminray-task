from django.test import TestCase, Client

from master.models import Server


class AnimalTestCase(TestCase):
    def setUp(self):
        Server.objects.create(name='server1', url='http://test.test')
        Server.objects.create(name='server2', url='http://test.test')
        Server.objects.create(name='server3', url='http://test.test')
        Server.objects.create(name='server4', url='http://test.test')

    def test_assign_tasks(self):
        tasks = [
            'task1',
            'task2',
            'task3',
            'task4',
            'task5',
            'task6',
        ]
        client = Client()
        response = client.post('/task_assigner/', data=tasks, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        content = response.json()
        self.assertEqual(len(content), Server.objects.count())
        actual_tasks = []
        for key in content:
            actual_tasks.extend(content[key])
        self.assertEqual(set(actual_tasks), set(tasks))
