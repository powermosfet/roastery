from django.db import models

from accounting.models import Account, CreditAccount, DebitAccount, Transaction
from roast.models import Batch
from roastery.models import SelflinkMixin

class Customer(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(blank=True)

    def save(self):
        super(Customer, self).save()
        if len(CustomerPayable.objects.filter(customer = self)) == 0:
            a = CustomerPayable()
            a.customer = self
            a.save()
        if len(CustomerReceivable.objects.filter(customer = self)) == 0:
            a = CustomerReceivable()
            a.customer = self
            a.save()

    def __unicode__(self):
        return self.name

class CustomerPayable(CreditAccount):
    customer = models.ForeignKey(Customer)

class CustomerReceivable(DebitAccount):
    customer = models.ForeignKey(Customer)

class Order(models.Model, SelflinkMixin):
    variety = models.ForeignKey('inventory.Variety')
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer)
    date = models.DateField()
    done = models.BooleanField(default = False)

    def delivered_quantity(self):
        return Batch.objects.filter(order = self,\
                                    state = Batch.DONE).count()

    def determine_done(self):
        self.done = self.delivered_quantity() >= self.quantity

    def __unicode__(self):
        return u'{} {}/{} pcs {} for {}'.format(u'\u2611' if self.done else u'\u2610', \
                                                self.delivered_quantity(), \
                                                self.quantity, \
                                                self.variety, \
                                                self.customer )

class OrderTransaction(Transaction):
    order = models.ForeignKey(Order)
