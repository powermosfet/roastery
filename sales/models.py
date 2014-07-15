from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from decimal import Decimal
from datetime import datetime as dt

from accounting.models import Account, CreditAccount, DebitAccount, Transaction, ExpenseAccount
from roast.models import Batch
from roastery.models import SelflinkMixin
from inventory.models import InventoryAccount

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

    def __unicode__(self):
        return "{} payable [{}]".format(self.customer, self.pk)

class CustomerReceivable(DebitAccount):
    customer = models.ForeignKey(Customer)

    def __unicode__(self):
        return "{} receivable [{}]".format(self.customer, self.pk)

ORDER_STATUS = (
        (0, 'Initial',            ),
        (1, 'In progress',        ),
        (2, 'Paid and delivered', ),
        )

class Order(models.Model, SelflinkMixin):
    variety = models.ForeignKey('inventory.Variety')
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer)
    date = models.DateField()
    status = models.IntegerField(choices = ORDER_STATUS)

    def delivered_quantity(self):
        return 0

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


@receiver(post_save, sender=Batch)
def batch_saved(sender, instance=None, **kwargs):
    inv = InventoryAccount.objects.first()
    xa = ExpenseAccount.objects.first()
    t = OrderTransaction.objects.filter(order=instance.order, credit=inv).first()
    if not t:
        t = OrderTransaction()
        t.order = instance.order
        t.debit = xa
        t.credit = inv
        t.timestamp = dt.now()
    t.amount = instance.bag.price * Decimal( instance.initial_weight / instance.bag.weight )
    t.save()

