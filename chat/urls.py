from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'chat'

urlpatterns = [
    path('',views.chathome, name='chat'),
    url(r'^(?P<room_name>[^/]+)/$', views.room, name='room'),
]