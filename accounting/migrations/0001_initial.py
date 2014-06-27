# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Account'
        db.create_table(u'accounting_account', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('balance', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal(u'accounting', ['Account'])

        # Adding model 'DebitAccount'
        db.create_table(u'accounting_debitaccount', (
            (u'account_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounting.Account'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'accounting', ['DebitAccount'])

        # Adding model 'CreditAccount'
        db.create_table(u'accounting_creditaccount', (
            (u'account_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounting.Account'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'accounting', ['CreditAccount'])

        # Adding model 'Transaction'
        db.create_table(u'accounting_transaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('time', self.gf('django.db.models.fields.TimeField')()),
            ('debit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='debit_account', to=orm['accounting.Account'])),
            ('credit', self.gf('django.db.models.fields.related.ForeignKey')(related_name='credit_account', to=orm['accounting.Account'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal(u'accounting', ['Transaction'])


    def backwards(self, orm):
        # Deleting model 'Account'
        db.delete_table(u'accounting_account')

        # Deleting model 'DebitAccount'
        db.delete_table(u'accounting_debitaccount')

        # Deleting model 'CreditAccount'
        db.delete_table(u'accounting_creditaccount')

        # Deleting model 'Transaction'
        db.delete_table(u'accounting_transaction')


    models = {
        u'accounting.account': {
            'Meta': {'object_name': 'Account'},
            'balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'accounting.creditaccount': {
            'Meta': {'object_name': 'CreditAccount', '_ormbases': [u'accounting.Account']},
            u'account_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounting.Account']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'accounting.debitaccount': {
            'Meta': {'object_name': 'DebitAccount', '_ormbases': [u'accounting.Account']},
            u'account_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounting.Account']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'accounting.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'credit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'credit_account'", 'to': u"orm['accounting.Account']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'debit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'debit_account'", 'to': u"orm['accounting.Account']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['accounting']