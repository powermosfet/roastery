from django.conf.urls import patterns, include, url
from django.views.generic import *
from roast.views import *
from roast.models import *

urlpatterns = patterns('',
    url(r'^$', main_view, name='roast'),
    url(r'^batch$', BatchList.as_view(), name='batch_list'),
)
