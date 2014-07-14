from django.conf.urls import patterns, include, url
from piston.resource import Resource
from django.views.generic import *
from api.handlers import *

from tags.functions import *

order_handler = Resource(OrderHandler)

urlpatterns = patterns('',
    lr_url(r'^orders/$', order_handler),
)
