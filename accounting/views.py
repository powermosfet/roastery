from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.core.urlresolvers import reverse, reverse_lazy 
from utilities.views import FormMixin

from sales.models import *

def navbar_items():
    return [
            ( 'Accounting', [
                        ('Accounts', reverse('account_all')),
                        ] ),
                ]

class AccountList(ListView):
    queryset = Account.objects.select_subclasses()

class AccountDelete(FormMixin, DeleteView):
    model = Account  
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('account_all')

class DebitAccountAdd(FormMixin, CreateView):
    model = DebitAccount
    template_name = 'form.html'
    success_url = reverse_lazy('account_all')

class CreditAccountAdd(FormMixin, CreateView):
    model = CreditAccount
    template_name = 'form.html'
    success_url = reverse_lazy('account_all')

class AccountEdit(FormMixin, UpdateView):
    model = Account
    template_name = 'sales/account_form.html'

    def get_context_data(self, *args, **kwargs):
        c = super(AccountEdit, self).get_context_data(*args, **kwargs)
        c['orders'] = Order.objects.filter(account=self.object)
        return c

