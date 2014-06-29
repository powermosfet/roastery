# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'VendorReceivable'
        db.create_table(u'inventory_vendorreceivable', (
            (u'debitaccount_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounting.DebitAccount'], unique=True, primary_key=True)),
            ('vendor', self.gf('annoying.fields.AutoOneToOneField')(to=orm['inventory.Vendor'], unique=True)),
        ))
        db.send_create_signal(u'inventory', ['VendorReceivable'])

        # Adding model 'VendorPayable'
        db.create_table(u'inventory_vendorpayable', (
            (u'creditaccount_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounting.CreditAccount'], unique=True, primary_key=True)),
            ('vendor', self.gf('annoying.fields.AutoOneToOneField')(to=orm['inventory.Vendor'], unique=True)),
        ))
        db.send_create_signal(u'inventory', ['VendorPayable'])

        # Deleting field 'Vendor.credit'
        db.delete_column(u'inventory_vendor', 'credit_id')


    def backwards(self, orm):
        # Deleting model 'VendorReceivable'
        db.delete_table(u'inventory_vendorreceivable')

        # Deleting model 'VendorPayable'
        db.delete_table(u'inventory_vendorpayable')

        # Adding field 'Vendor.credit'
        db.add_column(u'inventory_vendor', 'credit',
                      self.gf('annoying.fields.AutoOneToOneField')(to=orm['accounting.CreditAccount'], unique=True, null=True, blank=True),
                      keep_default=False)


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
        u'inventory.coffeebag': {
            'Meta': {'object_name': 'CoffeeBag'},
            'cost': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounting.Transaction']", 'unique': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_date': ('django.db.models.fields.DateField', [], {}),
            'received_date': ('django.db.models.fields.DateField', [], {}),
            'variety': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Variety']"}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Vendor']"}),
            'weight': ('django.db.models.fields.FloatField', [], {})
        },
        u'inventory.variety': {
            'Meta': {'object_name': 'Variety'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'crop_year': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '180', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'inventory.vendor': {
            'Meta': {'object_name': 'Vendor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'inventory.vendorpayable': {
            'Meta': {'object_name': 'VendorPayable', '_ormbases': [u'accounting.CreditAccount']},
            u'creditaccount_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounting.CreditAccount']", 'unique': 'True', 'primary_key': 'True'}),
            'vendor': ('annoying.fields.AutoOneToOneField', [], {'to': u"orm['inventory.Vendor']", 'unique': 'True'})
        },
        u'inventory.vendorreceivable': {
            'Meta': {'object_name': 'VendorReceivable', '_ormbases': [u'accounting.DebitAccount']},
            u'debitaccount_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounting.DebitAccount']", 'unique': 'True', 'primary_key': 'True'}),
            'vendor': ('annoying.fields.AutoOneToOneField', [], {'to': u"orm['inventory.Vendor']", 'unique': 'True'})
        }
    }

    complete_apps = ['inventory']