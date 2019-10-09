from django.urls import path

from . import views

urlpatterns = [
    path('mosquitto_auth', views.auth, name='auth'),
    path('mosquitto_superuser', views.super_user, name='superuser'),
    path('mosquitto_acl', views.acl, name='acl'),
    path('accounts/', views.MqttAccountsList.as_view()),
    path('accounts/<int:pk>/', views.MqttAccountDetail.as_view()),
    path('acl/', views.MqttAclList.as_view()),
    path('acl/<int:pk>/', views.MqttAclDetail.as_view())
]
