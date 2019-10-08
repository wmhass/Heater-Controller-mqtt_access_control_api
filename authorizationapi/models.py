from django.db import models

class MqttAccount(models.Model):
    username = models.CharField(max_length=40, unique=True)
    pw = models.CharField(max_length=100)
    superuser = models.PositiveSmallIntegerField(default=0)

class MqttAcl(models.Model):
    username = models.CharField(max_length=40)
    topic = models.CharField(max_length=100)
    rw = models.PositiveSmallIntegerField(default=1)
