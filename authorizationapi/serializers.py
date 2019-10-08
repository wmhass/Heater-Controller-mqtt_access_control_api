from rest_framework import serializers
from .models import MqttAccount


class MqttAccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = MqttAccount
        fields = ('username', 'pw', 'superuser')
