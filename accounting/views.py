from django.views.generic import ListView, DeleteView, UpdateView, CreateView
from django.core.urlresolvers import reverse, reverse_lazy 
from utilities.views import FormMixin
from django.db.models import Sum

from sales.models import *
from inventory.models import *

def navbar_items():
    return [
            ( 'Accounting', [
                        ('Accounts', reverse('account_all')),
                        ('Transactions', reverse('transaction_all')),
                        ] ),
                ]

class AccountList(ListView):
    queryset = Account.objects.select_subclasses()

    def get_context_data(self, *args, **kwargs):
        c = super(AccountList, self).get_context_data(*args, **kwargs)
        c['cr'] = CustomerReceivable.objects.all()
        c['cr_sum'] = c['cr'].aggregate(Sum('balance'))
        c['vr'] = VendorReceivable.objects.all()
        c['vr_sum'] = c['vr'].aggregate(Sum('balance'))
        c['da'] = DebitAccount.objects.select_subclasses().filter(customerreceivable__isnull = True,
                                                                  vendorreceivable__isnull = True)
        c['da_sum'] = c['da'].aggregate(Sum('balance'))
        c['dr_subtotal'] = sum(x['balance__sum'] for x in [ c['cr_sum'], c['da_sum'], c['vr_sum'] ])

        c['cp'] = CustomerPayable.objects.all()
        c['cp_sum'] = c['cp'].aggregate(Sum('balance'))
        c['vp'] = VendorPayable.objects.all()
        c['vp_sum'] = c['vp'].aggregate(Sum('balance'))
        c['ca'] = CreditAccount.objects.select_subclasses().filter(customerpayable__isnull = True,
                                                                   vendorpayable__isnull = True)
        c['ca_sum'] = c['ca'].aggregate(Sum('balance'))
        c['cr_subtotal'] = sum(x['balance__sum'] for x in [ c['cp_sum'], c['ca_sum'], c['vp_sum'] ])
        return c

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
    template_name = 'form.html'

class TransactionList(ListView):
    queryset = Transaction.objects.order_by('timestamp')
    template_name = 'accounting/transaction_list.html'

class TransactionDelete(FormMixin, DeleteView):
    model = Transaction  
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('transaction_all')

class TransactionAdd(FormMixin, CreateView):
    model = Transaction
    template_name = 'form.html'
    success_url = reverse_lazy('transaction_all')

class TransactionEdit(FormMixin, UpdateView):
    model = Transaction
    template_name = 'form.html'

