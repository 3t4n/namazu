from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from frontend import views as frontend
urlpatterns = [
    url(r'^$', frontend.index), 
    url(r'^dashboard/$', frontend.dashboard), 
    url(r'^admin/', admin.site.urls),
    url(r'^api/',include('api.urls')),
] + static(settings.STATIC_URL, document_root='/static/')
