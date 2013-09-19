from django.views.generic import *
from roast.models import *

class VendorList(ListView):
    model = Vendor

class VendorCreate(CreateView):
    model = Vendor
