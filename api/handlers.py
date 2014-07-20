from piston.handler import AnonymousBaseHandler, BaseHandler

from sales.models import Order, Customer
from inventory.models import CoffeeBag
from roast.models import RoastPoint, Event

class OrderHandler(BaseHandler):
    model = Order
    fields = [ 'id', 'customer', 'quantity', 'get_status_display', 'date', 'variety' ]

class CustomerHandler(BaseHandler):
    model = Customer

class CoffeeBagHandler(BaseHandler):
    model = CoffeeBag

class EventHandler(BaseHandler):
    model = Event

class RoastPointHandler(BaseHandler):
    model = RoastPoint
    fields = ( 'id', 'temp', 'time', ( 'batch', ( 'id', ) )  )

    def create(self, r, *args, **kwargs):
        import pdb;pdb.set_trace()
        return super(RoastPointHandler, self).create(r, *args, **kwargs)
