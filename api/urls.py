from django.conf.urls import patterns, include, url
from piston.resource import Resource
from django.views.generic import *
from api.handlers import *

order_handler = Resource(OrderHandler)
customer_handler = Resource(CustomerHandler)
coffeebag_handler = Resource(CoffeeBagHandler)
roastevent_handler = Resource(EventHandler)
roastpoint_handler = Resource(RoastPointHandler)

urlpatterns = patterns('',
    url(r'^customers/$', customer_handler),
    url(r'^customers/(?P<pk>\d+)/$', customer_handler),
    url(r'^orders/$', order_handler, name='api_order_all'),
    url(r'^orders/(?P<pk>\d+)/$', order_handler),
    url(r'^coffeebags/$', coffeebag_handler),
    url(r'^coffeebags/(?P<pk>\d+)/$', coffeebag_handler),
    url(r'^batch/(?P<batch>\d+)/roastpoints/$', roastpoint_handler),
    url(r'^roastevents/$', roastevent_handler),
    url(r'^roastevents/(?P<pk>\d+)/$', roastevent_handler),
)
