from rest_framework import serializers

from master.models import NameServer


class NameServerSerializer(serializers.ModelSerializer):
    class Meta:
        model = NameServer
        fields = '__all__'
