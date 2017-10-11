from django.conf.urls import url,include
from .views import *
from djoser.views import UserView
urlpatterns = [
   url(r'^buildings/', BuildingList.as_view()),
   url(r'^node/(?P<pk>[0-9]+)/', NodeDetail.as_view()),
   url(r'^accelerometer/(?P<pk>[0-9]+)/', AccelerometerDetail.as_view()),
   url(r'^auth/', include('auth.urls')),
   url(r'^login/',UserView.as_view()),
]
