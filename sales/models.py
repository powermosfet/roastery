from django.db import models

from accounting.models import Account

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

class Order(models.Model):
    description = models.CharField(max_length=260, blank = True)
    variety = models.ForeignKey('inventory.Variety')
    quantity = models.IntegerField()
    customer = models.ForeignKey(Customer)
    date = models.DateField()

    def __unicode__(self):
        return u'{0} pcs {1} for {2}'.format(self.quantity, \
                                             self.variety, \
                                             self.customer )
