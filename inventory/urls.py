from django.conf.urls import patterns, include, url
from django.views.generic import *
from inventory.views import *
from inventory.models import *

urlpatterns = patterns('',
    url(r'^$', main_view, name='inventory'),
    url(r'^bags$', BagList.as_view(), name='bag_list'),
    url(r'^bag/(?P<pk>\d+)$', BagEdit.as_view(), name='bag_edit'),
    url(r'^bag/add$', BagAdd.as_view(), name='bag_add'),
)
