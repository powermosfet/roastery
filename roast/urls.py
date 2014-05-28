from django.conf.urls import patterns, include, url
from django.views.generic import *
from roast.views import *
from roast.models import *

urlpatterns = patterns('',
    # url(r'^$', BudgetView.as_view(), name='budget_main'),
    # url(r'^$', main_view, name='main'),
    # url(r'^customers/$', ListView.as_view(model=Customer), name='customer_list'),
    # url(r'^customer/(?P<pk>\d+)/$', UpdateView.as_view(model=Customer, template_name='roast/detail_form.html'), name='customer_update'),
    # url(r'^customer/(?P<pk>\d+)/del/$', DeleteView.as_view(model=Customer), name='customer_del'),
    # url(r'^vendors/$', ListView.as_view(model=Vendor), name='vendor_list'),
    # url(r'^vendors/(?P<pk>\d+)/$', UpdateView.as_view(model=Vendor, template_name='roast/detail_form.html'), name='vendor_update'),
    # url(r'^vendors/(?P<pk>\d+)/del/$', DeleteView.as_view(model=Vendor), name='vendor_del'),
    # url(r'^vendors/add/$', CreateView.as_view(model=Vendor), name='vendor_add'),
    # url(r'^batches/$', ListView.as_view(queryset=Batch.objects.order_by('-date')), name='batch_list'),
    # url(r'^batches/unfinished/$', ListView.as_view(queryset=Batch.objects.filter(date__isnull=True)), name='unfinished_batch_list'),
    # url(r'^batches/orderless/$', ListView.as_view(queryset=Batch.objects.filter(order__isnull=True)), name='orderless_batch_list'),
    # url(r'^batch/(?P<pk>\d+)/$', UpdateView.as_view(model=Batch, success_url=reverse_lazy('batch_list'), template_name='roast/detail_form.html'), name='batch_update'),
    # url(r'^batch/(?P<pk>\d+)/del/$', DeleteView.as_view(model=Batch, success_url=reverse_lazy('batch_list')), name='batch_del'),
    # url(r'^batch/add/$', BatchCreate.as_view(), name='batch_add'),
    # url(r'^batch/add/(?P<order_pk>\d+)/$', OrderBatchCreate.as_view(), name='order_batch_add'),
    # url(r'^orders/$', ListView.as_view(model=Order), name='order_list'),
    # url(r'^order/(?P<pk>\d+)/$', DetailView.as_view(model=Order, template_name='roast/order_detail.html'), name='order_detail'),
    # url(r'^bags/$', ListView.as_view(model=CoffeeBag), name='bag_list'),
    # url(r'^bags/non_empty/$', ListView.as_view(queryset=CoffeeBag.objects.annotate(used=Sum('batch__initial_weight')).filter(Q(used__lt=F('weight')) | Q(used__isnull=True))), name='bag_list'),
    # url(r'^bag/(?P<pk>\d+)/$', DetailView.as_view(model=CoffeeBag, template_name='roast/coffeebag_detail.html'), name='bag_detail'),
)
