from django.views.generic import ListView , UpdateView, CreateView
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy

from inventory.models import *

def navbar_items():
    return [ 
            ('Inventory', [
                ('Coffee bags', reverse('bag_list')),
                ('Ffffh', reverse('bag_list')),
                ]),
            ]

def main_view(req):
    return HttpResponseRedirect(reverse('bag_list'))

class BagList(ListView):
    model = CoffeeBag
    template = 'inventory/coffeebag_list.html'

class BagEdit(UpdateView):
    model = CoffeeBag  

class BagAdd(CreateView):
    model = CoffeeBag
    sucess_url = reverse_lazy('bag_list')
