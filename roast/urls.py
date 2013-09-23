from django.conf.urls import patterns, include, url
from roast.views import *

urlpatterns = patterns('',
    # url(r'^$', BudgetView.as_view(), name='budget_main'),
    url(r'^vendors/$', VendorList.as_view(), name='vendor_list'),
    url(r'^vendors/add/$', VendorCreate.as_view(), name='vendor_add'),
)
