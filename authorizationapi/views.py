# https://wsvincent.com/official-django-rest-framework-tutorial-beginners-guide/
from rest_framework import generics
from .models import MqttAcl, MqttAccount
from .serializers import MqttAccountSerializer


class AccountsList(generics.ListCreateAPIView):
    queryset = MqttAccount.objects.all()
    serializer_class = MqttAccountSerializer


class AccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MqttAccount.objects.all()
    serializer_class = MqttAccountSerializer
