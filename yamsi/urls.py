from django.conf.urls import patterns, include, url
from django.contrib import admin

import get_music.views as views

urlpatterns = [
    url(r'^get_token/$', views.get_token),
    url(r'^index/$', views.index),
    url(r'^get_audiolist/$', views.get_audiolist),
]