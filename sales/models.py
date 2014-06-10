from django.db import models

from accounting.models import Account
from roast.models import Batch
from roastery.models import SelflinkMixin

class Customer(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField(blank=True)
    account = models.OneToOneField(Account, blank = True)

    def save(self):
        if not hasattr(self, 'account') or self.account is None:
            a = Account()
            a.name = self.name
            a.save()
            self.account = a
        super(Customer, self).save()

    def __unicode__(self):
        return self.name

class Order(models.Model, SelflinkMixin):
    description = models.CharField(max_length=260, blank = True)
    variety = models.ForeignKey('inventory.Variety')
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer)
    date = models.DateField()

    def delivered_quantity(self):
        return Batch.objects.filter(order = self,\
                                    bag__variety = self.variety,\
                                    state = 1).count()

    def done(self):
        return self.delivered_quantity() >= self.quantity

    def __unicode__(self):
        return u'{0} {1}/{2} pcs {3} for {4}'.format(u'\u2611' if self.done() else u'\u2610', \
                                                     self.delivered_quantity(), \
                                                     self.quantity, \
                                                     self.variety, \
                                                     self.customer )
