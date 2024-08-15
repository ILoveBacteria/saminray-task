import requests
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from master.models import Server
from master.serializers import ServerSerializer


class SendAllView(APIView): 
    def post(self, request):
        task_assigner_url = Server.objects.filter(name='task_assigner').get().url
        response = requests.post(task_assigner_url, json=request.data)
        assigned_task = response.json()
        tasks_result = []
        for server_name in assigned_task:
            result = run_task(assigned_task[server_name], server_name)
            tasks_result.extend(result)
        return Response(tasks_result)
    

class SendSpecificView(APIView):
    def post(self, request, server_name):
        result = run_task(request.data, server_name)
        return Response(result)
    

class ServerList(generics.ListCreateAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer


class ServerDetail(generics.RetrieveUpdateAPIView):
    queryset = Server.objects.all()
    serializer_class = ServerSerializer
    lookup_field = 'name'


def run_task(tasks: list, server_name: str) -> list:
    task_runner_url = Server.objects.filter(name=server_name).get().url
    response = requests.post(task_runner_url, json=tasks)
    return response.json()
