# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Transaction.time'
        db.delete_column(u'accounting_transaction', 'time')

        # Deleting field 'Transaction.date'
        db.delete_column(u'accounting_transaction', 'date')

        # Adding field 'Transaction.timestamp'
        db.add_column(u'accounting_transaction', 'timestamp',
                      self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2014, 7, 3, 0, 0)),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Transaction.time'
        raise RuntimeError("Cannot reverse this migration. 'Transaction.time' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Transaction.time'
        db.add_column(u'accounting_transaction', 'time',
                      self.gf('django.db.models.fields.TimeField')(),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Transaction.date'
        raise RuntimeError("Cannot reverse this migration. 'Transaction.date' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Transaction.date'
        db.add_column(u'accounting_transaction', 'date',
                      self.gf('django.db.models.fields.DateField')(),
                      keep_default=False)

        # Deleting field 'Transaction.timestamp'
        db.delete_column(u'accounting_transaction', 'timestamp')


    models = {
        u'accounting.account': {
            'Meta': {'object_name': 'Account'},
            'balance': ('django.db.models.fields.DecimalField', [], {'default': '0.0', 'max_digits': '8', 'decimal_places': '2'}),
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
            'debit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'debit_account'", 'to': u"orm['accounting.Account']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {})
        }
    }

    complete_apps = ['accounting']