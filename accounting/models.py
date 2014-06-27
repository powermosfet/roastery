from django.db import models
from decimal import Decimal

ACCOUNT_TYPES = (
    (0, 'Assets'),
    (1, 'Liabilities'),
    (2, 'Equity'),
)

class Account(models.Model):
    balance = models.DecimalField(max_digits=8, decimal_places=2, default = 0)

    def recalculate_balance(self):
        self.balance = 0
        for t in Transaction.objects.filter(debit = self):
            self.debit(t.amount)
        for t in Transaction.objects.filter(credit = self):
            self.credit(t.amount)

    def __unicode__(self):
        drcr = '-'
        if hasattr(self, 'debitaccount')  and self.debitaccount is not None: drcr = 'Dr'
        if hasattr(self, 'creditaccount') and self.creditaccount is not None: drcr = 'Cr'
        return u'{:0>10} [{}]: {:.2}'.format(self.pk, drcr, self.balance)

class DebitAccount(Account):
    def debit(self, amount):
        self.balance += amount

    def credit(self, amount):
        self.balance -= amount

class CreditAccount(Account):
    def debit(self, amount):
        self.balance -= amount

    def credit(self, amount):
        self.balance += amount

class Transaction(models.Model):
    date = models.DateField()
    time = models.TimeField()
    debit = models.ForeignKey(Account, related_name = 'debit_account')
    credit = models.ForeignKey(Account, related_name = 'credit_account')
    amount = models.DecimalField(max_digits=8, decimal_places=2)

    def save(self):
        if self.pk is None:
            self.debit.debit(self.amount)
            self.credit.credit(self.amount)
        else:
            self.debit.recalculate_balance()
            self.credit.recalculate_balance()
        super(Transaction, self).save()

    def __unicode__(self):
        return u"{} {:.2} Dr {:0>10} Cr {:0>10}".format(self.date, self.amount, self.debit.pk, self.credit.pk)
