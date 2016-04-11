from django.conf.urls import patterns, include, url
from . import views

urlpatterns = [
     url(r'^$', 'registration.views.registrate', name='registration'),
]
