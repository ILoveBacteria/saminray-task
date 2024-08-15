from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class Runner(APIView):
    def post(self, request):
        response = [f'task {t} was ran by task_runner2' for t in request.data]
        return Response(response)
