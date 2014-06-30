# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BagTransaction'
        db.create_table(u'inventory_bagtransaction', (
            (u'transaction_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounting.Transaction'], unique=True, primary_key=True)),
            ('bag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.CoffeeBag'])),
        ))
        db.send_create_signal(u'inventory', ['BagTransaction'])

        # Deleting field 'CoffeeBag.cost'
        db.delete_column(u'inventory_coffeebag', 'cost_id')

        # Adding field 'CoffeeBag.price'
        db.add_column(u'inventory_coffeebag', 'price',
                      self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=6, decimal_places=2),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'BagTransaction'
        db.delete_table(u'inventory_bagtransaction')

        # Adding field 'CoffeeBag.cost'
        db.add_column(u'inventory_coffeebag', 'cost',
                      self.gf('django.db.models.fields.related.OneToOneField')(default=0, to=orm['accounting.Transaction'], unique=True),
                      keep_default=False)

        # Deleting field 'CoffeeBag.price'
        db.delete_column(u'inventory_coffeebag', 'price')


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
            'date': ('django.db.models.fields.DateField', [], {}),
            'debit': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'debit_account'", 'to': u"orm['accounting.Account']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
        u'inventory.bagtransaction': {
            'Meta': {'object_name': 'BagTransaction', '_ormbases': [u'accounting.Transaction']},
            'bag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.CoffeeBag']"}),
            u'transaction_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounting.Transaction']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'inventory.coffeebag': {
            'Meta': {'object_name': 'CoffeeBag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_date': ('django.db.models.fields.DateField', [], {}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'received_date': ('django.db.models.fields.DateField', [], {}),
            'variety': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Variety']"}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Vendor']"}),
            'weight': ('django.db.models.fields.FloatField', [], {})
        },
        u'inventory.inventoryaccount': {
            'Meta': {'object_name': 'InventoryAccount', '_ormbases': [u'accounting.DebitAccount']},
            u'debitaccount_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounting.DebitAccount']", 'unique': 'True', 'primary_key': 'True'})
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