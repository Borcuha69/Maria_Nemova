from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^landing/$', views.landing, name='landing'),
    url(r'^landing2/$', views.landing2, name='landing2'),
]