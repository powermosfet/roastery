from django.conf.urls import patterns, include, url
from django.views.generic import *
from inventory.views import *
from inventory.models import *

from tags.functions import *

urlpatterns = patterns('',
    lr_url(r'^$', main_view, name='inventory'),
    lr_url(r'^bags/$', BagAll.as_view(), name='coffeebag_all'),
    lr_url(r'^bags/nonempty/$', coffeebag_nonempty, name='coffeebag_nonempty'),
    lr_url(r'^bags/(?P<pk>\d+)/$', BagEdit.as_view(), name='coffeebag_edit'),
    lr_url(r'^bags/(?P<pk>\d+)/del/$', BagDelete.as_view(), name='coffeebag_delete'),
    lr_url(r'^bags/add/$', BagAdd.as_view(), name='coffeebag_add'),
    lr_url(r'^bagtransactions/add/$', BagTransactionAdd.as_view(), name='bagtransaction_add'),
    lr_url(r'^bagtransactions/(?P<pk>\d+)/$', BagTransactionEdit.as_view(), name='bagtransaction_edit'),
    lr_url(r'^bagtransactions/(?P<pk>\d+)/del/$', BagTransactionDelete.as_view(), name='bagtransaction_delete'),
    lr_url(r'^varieties/$', VarietyList.as_view(), name='variety_all'),
    lr_url(r'^varieties/(?P<pk>\d+)/$', VarietyEdit.as_view(), name='variety_edit'),
    lr_url(r'^varieties/(?P<pk>\d+)/del/$', VarietyDelete.as_view(), name='variety_delete'),
    lr_url(r'^varieties/add/$', VarietyAdd.as_view(), name='variety_add'),
    lr_url(r'^vendors/$', VendorList.as_view(), name='vendor_all'),
    lr_url(r'^vendors/(?P<pk>\d+)/$', VendorEdit.as_view(), name='vendor_edit'),
    lr_url(r'^vendors/(?P<pk>\d+)/del/$', VendorDelete.as_view(), name='vendor_delete'),
    lr_url(r'^vendors/add/$', VendorAdd.as_view(), name='vendor_add'),
)
