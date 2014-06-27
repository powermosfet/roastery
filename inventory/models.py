from django.db import models

from accounting.models import Account

class Vendor(models.Model):
    name = models.CharField(max_length = 30)
    website = models.URLField()
    credit = models.OneToOneField('accounting.CreditAccount')

    def save(self):
        if not hasattr(self, 'account') or self.account is None:
            a = Account()
            a.name = self.name
            a.save()
            self.account = a
        super(Vendor, self).save()

    def __unicode__(self):
        return u"{0}".format(self.name)

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
