from django.conf.urls import patterns, include, url
from django.views.generic import *
from roast.views import *
from roast.models import *

from tags.functions import *

urlpatterns = patterns('',
    url(r'^$', BatchList.as_view(), name='roast'),
    lr_url(r'^batches/$', BatchList.as_view(), name='batch_all'),
    lr_url(r'^batches/(?P<pk>\d+)/$', BatchEdit.as_view(), name='batch_edit'),
    lr_url(r'^batches/(?P<pk>\d+)/del/$', BatchDelete.as_view(), name='batch_delete'),
    lr_url(r'^batches/add/$', BatchAdd.as_view(), name='batch_add'),
)
