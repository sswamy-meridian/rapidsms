#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.conf.urls.defaults import *
from . import views


urlpatterns = patterns('',
    url(r'^$', views.registration, name="registration"),
    url(r'^/contact/add$', views.contact_add, name="contact_add"),
    url(r'^contact/bulk_add$', views.contact_bulk_add, name="contact_bulk_add"),
    url(r'^(?P<pk>\d+)/edit/$', views.contact_edit, name="contact_edit"),
)