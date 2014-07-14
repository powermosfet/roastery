from django.conf.urls import patterns, include, url
from django.views.generic import *
from utilities.views import direct
from sales.views import *
from sales.models import *

from tags.functions import *

orders = direct('sales/order_list_ajax.html')

urlpatterns = patterns('',
    url(r'^$', OrderOutstanding.as_view(), name='sales'),
    lr_url(r'^customers/$', CustomerList.as_view(), name='customer_all'),
    lr_url(r'^customers/(?P<pk>\d+)/$', CustomerEdit.as_view(), name='customer_edit'),
    lr_url(r'^customers/(?P<pk>\d+)/del/$', CustomerDelete.as_view(), name='customer_delete'),
    lr_url(r'^customers/add/$', CustomerAdd.as_view(), name='customer_add'),
    lr_url(r'^orders/$', orders, name='order_all'),
    lr_url(r'^orders/(?P<pk>\d+)/$', OrderEdit.as_view(), name='order_edit'),
    lr_url(r'^orders/(?P<pk>\d+)/del/$', OrderDelete.as_view(), name='order_delete'),
    lr_url(r'^orders/add/$', OrderAdd.as_view(), name='order_add'),
    lr_url(r'^ordertransactions/add/$', OrderTransactionAdd.as_view(), name='ordertransaction_add'),
    lr_url(r'^ordertransactions/(?P<pk>\d+)/$', OrderTransactionEdit.as_view(), name='ordertransaction_edit'),
    lr_url(r'^ordertransactions/(?P<pk>\d+)/del/$', OrderTransactionDelete.as_view(), name='ordertransaction_delete'),
)
