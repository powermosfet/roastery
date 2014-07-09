from model_utils.managers import InheritanceManager
from django.db import models
from decimal import Decimal

class Account(models.Model):
    balance = models.DecimalField(max_digits=8, decimal_places=2, default = 0.0)
    description = models.CharField(max_length=80, blank=True, null=True)

    objects = InheritanceManager()

    def recalculate_balance(self):
        self.balance = 0
        for t in Transaction.objects.filter(debit = self):
            self.debit(t.amount)
        for t in Transaction.objects.filter(credit = self):
            self.credit(t.amount)

    def __unicode__(self):
        if self.description is None:
            drcr = '-'
            if hasattr(self, 'debitaccount')  and self.debitaccount is not None: drcr = 'Dr'
            if hasattr(self, 'creditaccount') and self.creditaccount is not None: drcr = 'Cr'
            return u'{} [{}]'.format(drcr, self.pk)
        else:
            return u'{} [{}]'.format(self.description, self.pk)

class DebitAccount(Account):
    objects = InheritanceManager()
    def debit(self, amount):
        self.balance += amount

    def credit(self, amount):
        self.balance -= amount

class CreditAccount(Account):
    objects = InheritanceManager()
    def debit(self, amount):
        self.balance -= amount

    def credit(self, amount):
        self.balance += amount

class ExpenseAccount(DebitAccount):
    objects = InheritanceManager()

    def save(self):
        self.description = 'Expenses'
        super(ExpenseAccount, self).save()

class Transaction(models.Model):
    timestamp = models.DateTimeField()
    debit = models.ForeignKey(Account, related_name = 'debit_account')
    credit = models.ForeignKey(Account, related_name = 'credit_account')
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    def __init__(self, *args, **kwargs):
        super(Transaction, self).__init__(*args, **kwargs)
        if hasattr(self, 'debit') and self.debit is not None:
            self.debit = Account.objects.get_subclass(pk=self.debit.pk)
        if hasattr(self, 'credit') and self.credit is not None:
            self.credit = Account.objects.get_subclass(pk=self.credit.pk)

    def save(self):
        if self.pk is None:
            self.debit.debit(self.amount)
            self.credit.credit(self.amount)
        else:
            self.debit.recalculate_balance()
            self.credit.recalculate_balance()
        self.credit.save()
        self.debit.save()
        super(Transaction, self).save()

    def __unicode__(self):
        return u"{:%Y-%m-%d} {} Dr {} Cr {}".format(self.timestamp,
                                                              self.amount,
                                                              self.debit,
                                                              self.credit,
                                                              )
