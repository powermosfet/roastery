from django.db import models
from django.core.urlresolvers import reverse_lazy

class Vendor(models.Model):
    name = models.CharField(max_length = 30)
    website = models.URLField()

    def __unicode__(self):
        return u"{0}".format(self.name)

class Variety(models.Model):
    country = models.CharField(max_length = 30)
    area = models.CharField(max_length = 80)
    description = models.CharField(max_length = 180, blank = True)

    def __unicode__(self):
        if self.description is None or self.description == '':
            return u"{0} {1}".format(self.country, self.area)
        else:
            return u"{0} {1} ({2})".format(self.country, self.area, self.description)

CASHFLOW_TYPES = (
    ( 1, 'Income'),
    (-1, 'Expense')
)

class CashFlow(models.Model):
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    type = models.IntegerField(choices=CASHFLOW_TYPES, default=1)
    date = models.DateField()

    def __unicode__(self):
        return u"[{0}] {1} NOK".format(self.date, self.amount * self.type)

class CoffeeBag(models.Model):
    variety = models.ForeignKey(Variety)
    vendor = models.ForeignKey(Vendor)
    order_date = models.DateField()
    cost = models.OneToOneField(CashFlow)
    received_date = models.DateField()
    weight = models.FloatField()
    
    def remaining(self):
        return self.weight - sum(b.initial_weight for b in self.batch_set.all())

    def __unicode__(self):
        return u"bag #{0}: {1}g of {2} from {3} [{4}] - {5}g left".format(self.pk, self.weight, self.variety, self.vendor, self.received_date, self.remaining())

class Customer(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(blank=True)
    
    def __unicode__(self):
        return self.name

class Order(models.Model):
    description = models.CharField(max_length=260)
    customer = models.ForeignKey(Customer)
    date = models.DateField()
    payment = models.OneToOneField(CashFlow, blank=True)

    def paid(self):
        if (hasattr(self, 'payment') == False) or self.payment is None: return 'Unpaid'
        else: return 'Paid'
    
    def __unicode__(self):
        return u"[{0}][{2}] {1}: {3}".format(self.date, self.customer, self.paid(), self.description)
    
class Batch(models.Model):
    bag = models.ForeignKey(CoffeeBag)
    initial_weight = models.FloatField()
    date = models.DateField(blank=True)
    ambient_temp = models.FloatField(blank=True)
    program = models.CharField(max_length = 30, blank=True)
    target_temp = models.FloatField(blank=True)
    target_time = models.TimeField(blank=True)
    final_weight = models.FloatField(blank=True)
    order = models.ForeignKey(Order, null=True, blank=True)

    def __unicode__(self):
        if self.date is None:
            return u"Unroasted: {0}g of {1}".format(self.initial_weight, self.bag.variety)
        else:
            return u"{0}: {1}g of {2}".format(self.date, self.initial_weight, self.bag.variety)

class RoastPoint(models.Model):
    time = models.TimeField()
    temp = models.FloatField()
    batch = models.ForeignKey(Batch)

    def __unicode__(self):
        return u"{0}: {1}deg K".format(self.time, self.temp)

class Event(models.Model):
    description = models.CharField(max_length = 30)

    def __unicode__(self):
        return self.description

