from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from master.models import NameServer
from master.serializers import NameServerSerializer


class SendAllView(APIView): 
    def post(self, request):
        print(request.data, type(request.data))
        return Response('posted')
    

class SendSpecificView(APIView):
    def post(self, request, server_name):
        return Response(server_name)
    

class NameServerList(generics.ListCreateAPIView):
    queryset = NameServer.objects.all()
    serializer_class = NameServerSerializer


class NameServerDetail(generics.RetrieveUpdateAPIView):
    queryset = NameServer.objects.all()
    serializer_class = NameServerSerializer
    lookup_field = 'name'
