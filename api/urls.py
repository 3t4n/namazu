from django.conf.urls import url
from .views import *
urlpatterns = [
   url(r'^buildings/', BuildingList.as_view()),
   url(r'^node/(?P<pk>[0-9]+)/', NodeDetail.as_view()),
   url(r'^accelerometer/(?P<pk>[0-9]+)/', AccelerometerDetail.as_view()),
]
