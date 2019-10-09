from rest_framework import serializers
from .models import MqttAccount, MqttAcl


class MqttAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = MqttAccount
        fields = ('id', 'username', 'pw', 'superuser')


class MqttAclSerializer(serializers.ModelSerializer):

    class Meta:
        model = MqttAcl
        fields = ('username', 'topic', 'rw')
