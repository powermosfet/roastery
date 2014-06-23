from django.views.generic import ListView

from sales.models import Order

class OutstandingOrders(ListView):
    def get_queryset(self, *args, **kwargs):
        return [ x for x in Order.objects.all() ]
