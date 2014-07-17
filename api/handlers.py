from piston.handler import AnonymousBaseHandler, BaseHandler

from sales.models import Order, Customer
from inventory.models import CoffeeBag

class OrderHandler(BaseHandler):
    model = Order
    fields = [ 'id', 'customer', 'quantity', 'get_status_display', 'date', 'variety' ]

class CustomerHandler(BaseHandler):
    model = Customer

class CoffeeBagHandler(BaseHandler):
    model = CoffeeBag