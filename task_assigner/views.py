import random

from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from master.models import NameServer


class Assigner(APIView):
    def post(self, request):
        servers = NameServer.objects.exclude(name='task_assigner').values_list('name', flat=True)
        assigned_tasks = {s: [] for s in servers}
        for task in request.data:
            assigned_tasks[random.choice(servers)].append(task)
        return Response(assigned_tasks)
