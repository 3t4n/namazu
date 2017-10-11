from django.conf.urls import url
from  djoser.views import *

urlpatterns = [
    url(r'^login',LoginView.as_view() ),
    url(r'^register',RegistrationView.as_view() ),
    url(r'^password/reset', PasswordResetView.as_view())
        ]
