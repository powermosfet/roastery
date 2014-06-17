from django.db import models
from decimal import Decimal

ACCOUNT_TYPES = (
    (0, 'Master account'),
    (1, 'Master customer credit'),
    (2, 'Customer credit'),
    (3, 'Customer cash'),
)

class Account(models.Model):
    name = models.CharField(max_length = 80, blank = True)
    account_type = models.IntegerField(choices = ACCOUNT_TYPES, default = 2)
    balance = models.DecimalField(max_digits=8, decimal_places=2, default = 0)

    def withdraw(self, amount):
        self.balance -= amount
        self.save()

    def deposit(self, amount):
        self.balance += amount
        self.save()

    def recalculate_balance(self):
        self.balance = Decimal(sum(t.amount for t in Transaction.objects.filter(receiver = self)) - \
                               sum(t.amount for t in Transaction.objects.filter(sender   = self)))
        self.save()

    def __unicode__(self):
        if self.name is None or self.name == '':
            return u'#{0}: [{1}]'.format(self.pk, self.balance)
        else:
            return u'{0}: [{1}]'.format(self.name, self.balance)

class Transaction(models.Model):
    date = models.DateField()
    time = models.TimeField()
    sender = models.ForeignKey(Account, related_name = 'transactions_outbound')
    receiver = models.ForeignKey(Account, related_name = 'transactions_inbound')
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    def save(self):
        if self.pk is None:
            self.sender.withdraw(self.amount)
            self.receiver.deposit(self.amount)
        else:
            self.sender.recalculate_balance()
            self.receiver.recalculate_balance()
        super(Transaction, self).save()

    def __unicode__(self):
        return u"[{0}] {1} NOK".format(self.date, self.amount)
