from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.core.urlresolvers import reverse, reverse_lazy 
from utilities.views import FormMixin

from sales.models import *

def navbar_items():
    return [
            ( 'Sales', [
                        ('Customers', reverse('customer_all')),
                        ('Orders', reverse('order_all')),
                        ('Outstanding orders', reverse('order_outstanding')),
                        ] ),
                ]

class OrderList(ListView):
    model = Order

class OrderOutstanding(OrderList):
    def get_queryset(self, *args, **kwargs):
        return Order.objects.filter(done=False)


class OrderDelete(FormMixin, DeleteView):
    model = Order  
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('order_all')

class OrderAdd(FormMixin, CreateView):
    model = Order
    template_name = 'form.html'
    
    def get_success_url(self, *args, **kwargs):
        import pdb;pdb.set_trace()
        return reverse('order_edit', self.object.pk)

    def get_initial(self, *args, **kwargs):
        i = super(OrderAdd, self).get_initial(*args, **kwargs)
        if 'customer' in self.request.GET.keys():
            i['customer'] = self.request.GET['customer']
        return i

class OrderEdit(FormMixin, UpdateView):
    model = Order
    template_name = 'sales/order_form.html'
    success_url = reverse_lazy('order_all')

    def get_context_data(self, *args, **kwargs):
        c = super(OrderEdit, self).get_context_data(*args, **kwargs)
        c['ts'] = OrderTransaction.objects.filter(order = self.object)
        c['bs'] = Batch.objects.filter(order = self.object)
        return c


class CustomerList(ListView):
    model = Customer

class CustomerDelete(FormMixin, DeleteView):
    model = Customer  
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('customer_all')

class CustomerAdd(FormMixin, CreateView):
    model = Customer
    template_name = 'form.html'
    success_url = reverse_lazy('customer_all')

class CustomerEdit(FormMixin, UpdateView):
    model = Customer
    template_name = 'sales/customer_form.html'

    def get_context_data(self, *args, **kwargs):
        c = super(CustomerEdit, self).get_context_data(*args, **kwargs)
        c['orders'] = Order.objects.filter(customer=self.object)
        return c


class OrderTransactionAdd(FormMixin, CreateView):
    model = OrderTransaction
    template_name = 'form.html'
    success_url = reverse_lazy('coffeebag_nonempty')

    def get_form(self, *args, **kwargs):
        f = super(OrderTransactionAdd, self).get_form(*args, **kwargs)
        f.fields['debit'].queryset = Account.objects.select_subclasses()
        f.fields['credit'].queryset = Account.objects.select_subclasses()
        return f

    def get_initial(self, *args, **kwargs):
        i = super(OrderTransactionAdd, self).get_initial(*args, **kwargs)
        if 'order' in self.request.GET.keys():
            i['order'] = self.request.GET['order']
        return i

class OrderTransactionEdit(FormMixin, UpdateView):
    model = OrderTransaction
    template_name = 'form.html'
    success_url = reverse_lazy('coffeebag_nonempty')

    def get_form(self, *args, **kwargs):
        f = super(OrderTransactionEdit, self).get_form(*args, **kwargs)
        f.fields['debit'].queryset = Account.objects.select_subclasses()
        f.fields['credit'].queryset = Account.objects.select_subclasses()
        return f

class OrderTransactionDelete(FormMixin, DeleteView):
    model = OrderTransaction
    template_name = 'confirm_delete'
    success_url = reverse_lazy('coffeebag_nonempty')
