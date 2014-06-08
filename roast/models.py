from django.db import models
from django.core.urlresolvers import reverse_lazy

BATCH_STATES = ((0, 'Unroasted'),
                (1, 'Roasted'),)

class Batch(models.Model):
    bag = models.ForeignKey('inventory.CoffeeBag')
    initial_weight = models.FloatField()
    date = models.DateField(blank=True, null=True)
    ambient_temp = models.FloatField(blank=True, null=True)
    program = models.CharField(max_length = 30, blank=True)
    target_temp = models.FloatField(blank=True, null=True)
    target_time = models.TimeField(blank=True, null=True)
    final_weight = models.FloatField(blank=True, null=True)
    order = models.ForeignKey('sales.Order')
    state = models.IntegerField(choices = BATCH_STATES, default = 0)

    class Meta:
        verbose_name_plural = 'Batches'

    def __unicode__(self):
        if self.date is None:
            return u"\u2610 {0}g of {1}".format(self.initial_weight, self.bag.variety)
        else:
            return u"\u2611 {0}: {1}g of {2}".format(self.date, self.initial_weight, self.bag.variety)

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
