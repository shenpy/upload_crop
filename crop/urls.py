#coding=utf-8
from django.conf.urls.defaults import *
from crop import views

urlpatterns = patterns('',
    url(r'^$', views.index, name="crop_index"),
	url(r'^cut-(?P<id>\d+)$', views.cut, name="crop_cut"),
	url(r'^show$', views.show, name="crop_show"),
)