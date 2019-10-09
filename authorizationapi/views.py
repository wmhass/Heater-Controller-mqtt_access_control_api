# https://wsvincent.com/official-django-rest-framework-tutorial-beginners-guide/
from .models import MqttAcl, MqttAccount
from rest_framework import generics
from .serializers import MqttAccountSerializer, MqttAclSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# https://github.com/jpmens/mosquitto-auth-plug/blob/master/examples/http-auth-be.py
import hashlib
from django.utils.datastructures import MultiValueDictKeyError
from paho.mqtt.matcher import MQTTMatcher


def encode_password(password):
    return hashlib.md5(str(password).encode()).hexdigest()


def dump_request(request):
    f = open("/usr/src/mqtt_access_control_api/file.txt", "a+")
    f.write(str(request) + "\n")
    f.write("GET:" + str(request.GET) + "\n")
    f.write("POST:" + str(request.POST) + "\n")
    f.write("===================\n")
    f.close()


@csrf_exempt
def auth(request):
    status_code = 200
    response_content = {}
    try:
        username = str(request.POST['username'])
        password = str(request.POST['password'])
        account = MqttAccount.objects.get(username=username)

        if account.pw == encode_password(password):
            response_content = {
                "success": 1,
                "account": MqttAccountSerializer(account).data
                }
            status_code = 200
        else:
            status_code = 403
            response_content = {"error": "Wrong password"}
    except MqttAccount.DoesNotExist as does_not_exist:
        status_code = 403
        response_content = {"error": "Account does not exist"}
    except MultiValueDictKeyError as e:
        status_code = 400
        response_content = {"error": "Field " + str(e) + " not sent"}
    except Exception as e:
        status_code = 500
        response_content = {"error": str(e)}

    response = JsonResponse(response_content)
    response.status_code = status_code
    return response


@csrf_exempt
def super_user(request):
    # POST:<QueryDict: {'username': ['admin'], 'password': [''], 'topic': [''], 'acc': ['-1'], 'clientid': ['']}>
    status_code = 200
    response_content = {}
    try:
        username = str(request.POST['username'])
        account = MqttAccount.objects.get(username=username)

        if account.superuser == 1:
            response_content = {
                "success": 1,
                "account": MqttAccountSerializer(account).data
                }
            status_code = 200
        else:
            status_code = 403
            response_content = {"error": "User is not superuser"}
    except MqttAccount.DoesNotExist as does_not_exist:
        status_code = 403
        response_content = {"error": "Account does not exist"}
    except MultiValueDictKeyError as e:
        status_code = 400
        response_content = {"error": "Field " + str(e) + " not sent"}
    except Exception as e:
        status_code = 500
        response_content = {"error": str(e)}

    response = JsonResponse(response_content)
    response.status_code = status_code
    return response


@csrf_exempt
def acl(request):
    status_code = 200
    response_content = {}
    try:
        status_code = 403
        response_content = {"error": "Not authorized"}

        username = str(request.POST['username'])
        topic = str(request.POST['topic'])
        acc = int(request.POST['acc'])

        acls = MqttAcl.objects.filter(username=username)
        for acl in acls:
            matcher = MQTTMatcher()
            matcher[acl.topic] = True
            try:
                next(matcher.iter_match(topic))
                # ACC:
                # 1 = Read
                # 2 = Write
                # 4 - Ask to subscribe
                if acl.rw == acc or acl.rw == 3 or acc == 4:
                    status_code = 200
                    response_content = {"result": MqttAclSerializer(acl).data}
                    break
            except StopIteration:
                continue

    except MqttAccount.DoesNotExist as does_not_exist:
        status_code = 403
        response_content = {"error": "Account does not exist"}
    except MultiValueDictKeyError as e:
        status_code = 400
        response_content = {"error": "Field " + str(e) + " not sent"}
    except Exception as e:
        status_code = 500
        response_content = {"error": str(e)}

    response = JsonResponse(response_content)
    response.status_code = status_code
    return response


class MqttAccountsList(generics.ListCreateAPIView):
    queryset = MqttAccount.objects.all()
    serializer_class = MqttAccountSerializer


class MqttAccountDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MqttAccount.objects.all()
    serializer_class = MqttAccountSerializer


class MqttAclList(generics.ListCreateAPIView):
    queryset = MqttAcl.objects.all()
    serializer_class = MqttAclSerializer


class MqttAclDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MqttAcl.objects.all()
    serializer_class = MqttAclSerializer
