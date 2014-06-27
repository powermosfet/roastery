# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Customer'
        db.create_table(u'sales_customer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('credit_account', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='credit_for', unique=True, null=True, to=orm['accounting.Account'])),
            ('cash_account', self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='cash_from', unique=True, null=True, to=orm['accounting.Account'])),
        ))
        db.send_create_signal(u'sales', ['Customer'])

        # Adding model 'CustomerPayable'
        db.create_table(u'sales_customerpayable', (
            (u'creditaccount_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounting.CreditAccount'], unique=True, primary_key=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sales.Customer'])),
        ))
        db.send_create_signal(u'sales', ['CustomerPayable'])

        # Adding model 'CustomerReceivable'
        db.create_table(u'sales_customerreceivable', (
            (u'debitaccount_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounting.DebitAccount'], unique=True, primary_key=True)),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sales.Customer'])),
        ))
        db.send_create_signal(u'sales', ['CustomerReceivable'])

        # Adding model 'Order'
        db.create_table(u'sales_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('variety', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Variety'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sales.Customer'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('done', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'sales', ['Order'])

        # Adding model 'OrderTransaction'
        db.create_table(u'sales_ordertransaction', (
            (u'transaction_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounting.Transaction'], unique=True, primary_key=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sales.Order'])),
        ))
        db.send_create_signal(u'sales', ['OrderTransaction'])


    def backwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table(u'sales_customer')

        # Deleting model 'CustomerPayable'
        db.delete_table(u'sales_customerpayable')

        # Deleting model 'CustomerReceivable'
        db.delete_table(u'sales_customerreceivable')

        # Deleting model 'Order'
        db.delete_table(u'sales_order')

        # Deleting model 'OrderTransaction'
        db.delete_table(u'sales_ordertransaction')


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
        },
        u'inventory.variety': {
            'Meta': {'object_name': 'Variety'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'crop_year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '180', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'sales.customer': {
            'Meta': {'object_name': 'Customer'},
            'cash_account': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'cash_from'", 'unique': 'True', 'null': 'True', 'to': u"orm['accounting.Account']"}),
            'credit_account': ('django.db.models.fields.related.OneToOneField', [], {'blank': 'True', 'related_name': "'credit_for'", 'unique': 'True', 'null': 'True', 'to': u"orm['accounting.Account']"}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'sales.customerpayable': {
            'Meta': {'object_name': 'CustomerPayable', '_ormbases': [u'accounting.CreditAccount']},
            u'creditaccount_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounting.CreditAccount']", 'unique': 'True', 'primary_key': 'True'}),
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sales.Customer']"})
        },
        u'sales.customerreceivable': {
            'Meta': {'object_name': 'CustomerReceivable', '_ormbases': [u'accounting.DebitAccount']},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sales.Customer']"}),
            u'debitaccount_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounting.DebitAccount']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'sales.order': {
            'Meta': {'object_name': 'Order'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sales.Customer']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'variety': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Variety']"})
        },
        u'sales.ordertransaction': {
            'Meta': {'object_name': 'OrderTransaction', '_ormbases': [u'accounting.Transaction']},
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sales.Order']"}),
            u'transaction_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounting.Transaction']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['sales']