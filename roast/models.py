from django.db import models

class Vendor(models.Model):
    name = models.CharField(max_length = 30)
    website = models.URLField()

    def __unicode__(self):
        return "{0}".format(self.name)

class CoffeeBag(models.Model):
    country = models.CharField(max_length = 30)
    variety = models.CharField(max_length = 30)
    vendor = models.ForeignKey(Vendor)
    order_date = models.DateField()
    received_date = models.DateField()
    weight = models.FloatField()

    def __unicode__(self):
        return "{0} ({1}) from {2} [{3}]".format(self.country, self.variety, self.vendor, self.received_date)

class Batch(models.Model):
    bag = models.ForeignKey(CoffeeBag)
    weight = models.FloatField()

    def __unicode__(self):
        return "{0}g from {1}".format(self.weight, self.bag)

class Roast(models.Model):
    date = models.DateField()
    batch = models.ForeignKey(Batch)
    ambient_temp = models.FloatField()
    program = models.CharField(max_length = 30)
    target_temp = models.FloatField()
    target_time = models.TimeField()
    final_weight = models.FloatField()

    def __unicode__(self):
        return "Roast: {0}".format(self.date)

class RoastPoint(models.Model):
    time = models.TimeField()
    temp = models.FloatField()
    roast = models.ForeignKey(Roast)

    def __unicode__(self):
        return "{0}: {1}deg K".format(self.time, self.temp)

class Event(models.Model):
    description = models.CharField(max_length = 30)

    def __unicode__(self):
        return self.description
