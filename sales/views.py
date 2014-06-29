from django.views.generic import ListView

from sales.models import Order

class OutstandingOrders(ListView):
    template = 'sales/order_list.html'

    def get_queryset(self, *args, **kwargs):
        return Order.objects.all()
