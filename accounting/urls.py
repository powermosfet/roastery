from django.conf.urls import patterns, include, url
from django.views.generic import *
from accounting.views import *
from accounting.models import *

from tags.functions import *

urlpatterns = patterns('',
    url(r'^$', AccountList.as_view(), name='account_all'),
    lr_url(r'^accounts/$', AccountList.as_view(), name='account_all'),
    lr_url(r'^accounts/(?P<pk>\d+)/$', AccountEdit.as_view(), name='account_edit'),
    lr_url(r'^accounts/(?P<pk>\d+)/del/$', AccountDelete.as_view(), name='account_delete'),
    lr_url(r'^accounts/debitadd/$', DebitAccountAdd.as_view(), name='debitaccount_add'),
    lr_url(r'^accounts/creditadd/$', CreditAccountAdd.as_view(), name='creditaccount_add'),
)
