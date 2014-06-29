from django.db import models
from annoying.fields import AutoOneToOneField
from roastery.models import SelflinkMixin

from accounting.models import CreditAccount, DebitAccount

class Vendor(models.Model):
    name = models.CharField(max_length = 30)
    website = models.URLField()

    def __unicode__(self):
        return u"{0}".format(self.name)

class VendorPayable(CreditAccount, SelflinkMixin):
    vendor = AutoOneToOneField(Vendor)

    def __unicode__(self):
        return u'{} Payable {}'.format(self.vendor, super(VendorPayable, self).__unicode__())

class VendorReceivable(DebitAccount, SelflinkMixin):
    vendor = AutoOneToOneField(Vendor)

    def __unicode__(self):
        return u'{} Receivable {}'.format(self.vendor, super(VendorReceivable, self).__unicode__())

class Variety(models.Model):
    country = models.CharField(max_length = 30)
    area = models.CharField(max_length = 80, blank = True)
    crop_year = models.CharField(max_length = 4, blank = True)
    description = models.CharField(max_length = 180, blank = True)

    class Meta:
        verbose_name_plural = 'Varieties'

    def __unicode__(self):
        if self.description is None or self.description == '':
            return u"{0} {1}".format(self.country, self.area)
        else:
            return u"{0} {1} ({2})".format(self.country, self.area, self.description)

class InventoryAccount(DebitAccount):
    def __unicode__(self):
        return u'inventory [{}]: {:.2}'.format(self.pk, self.balance)

class CoffeeBag(models.Model):
    variety = models.ForeignKey(Variety)
    vendor = models.ForeignKey(Vendor)
    order_date = models.DateField()
    cost = models.OneToOneField('accounting.Transaction')
    received_date = models.DateField()
    weight = models.FloatField()

    def remaining(self):
        return self.weight - sum(b.initial_weight for b in self.batch_set.all())

    def __unicode__(self):
        return u"{0} {1}/{2}g of {3} from {4}".format( u'\u2610' if self.remaining() <= 0 else u'\u2611',\
                                                      self.remaining(),\
                                                      self.weight,\
                                                      self.variety,\
                                                      self.vendor)
