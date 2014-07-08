from django.views.generic import ListView , UpdateView, CreateView, DeleteView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render_to_response
from utilities.views import FormMixin

from inventory.models import *
from accounting.models import Account

def navbar_items():
    return [ 
            ('Inventory', [
                ('Non-empty coffee bags', reverse('coffeebag_nonempty')),
                ('All coffee bags', reverse('coffeebag_all')),
                ('Varieties', reverse('variety_all')),
                ('Vendors', reverse('vendor_all')),
                ]),
            ]

def main_view(req):
    return HttpResponseRedirect(reverse('coffeebag_all'))

class BagAll(ListView):
    model = CoffeeBag

class BagEdit(FormMixin, UpdateView):
    model = CoffeeBag  

    def get_context_data(self, *args, **kwargs):
        kwargs['ts'] = BagTransaction.objects.filter(bag = self.object)
        return super(BagEdit, self).get_context_data(*args, **kwargs)

class BagDelete(FormMixin, DeleteView):
    model = CoffeeBag  
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('coffeebag_nonempty')

class BagAdd(FormMixin, CreateView):
    model = CoffeeBag
    template_name = 'form.html'
    sucess_url = reverse_lazy('coffeebag_all')

def coffeebag_nonempty(r):
    bags = [ b for b in CoffeeBag.objects.all() if b.remaining() > 0 ]
    c = { 'object_list': bags }
    return render_to_response('inventory/coffeebag_list.html', c)

class BagTransactionAdd(FormMixin, CreateView):
    model = BagTransaction
    template_name = 'form.html'
    success_url = reverse_lazy('coffeebag_nonempty')

    def get_form(self, *args, **kwargs):
        f = super(BagTransactionAdd, self).get_form(*args, **kwargs)
        f.fields['debit'].queryset = Account.objects.select_subclasses()
        f.fields['credit'].queryset = Account.objects.select_subclasses()
        return f

    def get_initial(self, *args, **kwargs):
        i = super(BagTransactionAdd, self).get_initial(*args, **kwargs)
        if 'bag' in self.request.GET.keys():
            i['bag'] = self.request.GET['bag']
        return i

class BagTransactionEdit(FormMixin, UpdateView):
    model = BagTransaction
    template_name = 'form.html'
    success_url = reverse_lazy('coffeebag_nonempty')

    def get_form(self, *args, **kwargs):
        f = super(BagTransactionEdit, self).get_form(*args, **kwargs)
        f.fields['debit'].queryset = Account.objects.select_subclasses()
        f.fields['credit'].queryset = Account.objects.select_subclasses()
        return f

class BagTransactionDelete(FormMixin, DeleteView):
    model = BagTransaction
    template_name = 'confirm_delete'
    success_url = reverse_lazy('coffeebag_nonempty')

class VarietyList(ListView):
    model = Variety

class VarietyDelete(FormMixin, DeleteView):
    model = Variety  
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('variety_all')

class VarietyAdd(FormMixin, CreateView):
    model = Variety
    template_name = 'form.html'
    success_url = reverse_lazy('variety_all')

class VarietyEdit(FormMixin, UpdateView):
    model = Variety
    template_name = 'form.html'


class VendorList(ListView):
    model = Vendor

class VendorDelete(FormMixin, DeleteView):
    model = Vendor  
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('vendor_all')

class VendorAdd(FormMixin, CreateView):
    model = Vendor
    template_name = 'form.html'
    success_url = reverse_lazy('vendor_all')

class VendorEdit(FormMixin, UpdateView):
    model = Vendor
    template_name = 'form.html'

