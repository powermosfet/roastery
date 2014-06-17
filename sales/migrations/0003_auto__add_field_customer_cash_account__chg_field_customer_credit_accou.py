# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Customer.cash_account'
        db.add_column(u'sales_customer', 'cash_account',
                      self.gf('django.db.models.fields.related.OneToOneField')(blank=True, related_name='cash_from', unique=True, null=True, to=orm['accounting.Account']),
                      keep_default=False)


        # Changing field 'Customer.credit_account'
        db.alter_column(u'sales_customer', 'credit_account_id', self.gf('django.db.models.fields.related.OneToOneField')(unique=True, null=True, to=orm['accounting.Account']))

    def backwards(self, orm):
        # Deleting field 'Customer.cash_account'
        db.delete_column(u'sales_customer', 'cash_account_id')


        # User chose to not deal with backwards NULL issues for 'Customer.credit_account'
        raise RuntimeError("Cannot reverse this migration. 'Customer.credit_account' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration
        # Changing field 'Customer.credit_account'
        db.alter_column(u'sales_customer', 'credit_account_id', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounting.Account'], unique=True))

    models = {
        u'accounting.account': {
            'Meta': {'object_name': 'Account'},
            'account_type': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'})
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
        u'sales.order': {
            'Meta': {'object_name': 'Order'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sales.Customer']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '260', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'variety': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Variety']"})
        }
    }

    complete_apps = ['sales']