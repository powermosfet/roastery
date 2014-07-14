from piston.handler import AnonymousBaseHandler, BaseHandler

from sales.models import Order

class OrderHandler(BaseHandler):
    model = Order
