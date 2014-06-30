from django.views.generic import ListView
from django.core.urlresolvers import reverse

from sales.models import Order

def navbar_items():
    return [
            ( 'Sales', [
                        ('Subfeature', '#'),
                        ('Another Subfeature', '#'),
                        ('Third Subfeature', '#'),
                        ] ),
                ]

class OutstandingOrders(ListView):
    template = 'sales/order_list.html'

    def get_queryset(self, *args, **kwargs):
        return Order.objects.all()
