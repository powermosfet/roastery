from django.conf.urls import patterns, include, url
from django.views.generic import *
from sales.views import *
from sales.models import *

urlpatterns = patterns('',
    url(r'^$', OutstandingOrders.as_view(), name='sales'),
)
