#encoding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from principal import views as principalviews
from django.conf import settings
admin.autodiscover()
urlpatterns = patterns('',
    url(r'^$', principalviews.portada, name='portada'),
)
