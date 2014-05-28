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
            ('account', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounting.Account'], unique=True, blank=True)),
        ))
        db.send_create_signal(u'sales', ['Customer'])

        # Adding model 'Order'
        db.create_table(u'sales_order', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=260, blank=True)),
            ('variety', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Variety'])),
            ('quantity', self.gf('django.db.models.fields.IntegerField')()),
            ('customer', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sales.Customer'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal(u'sales', ['Order'])


    def backwards(self, orm):
        # Deleting model 'Customer'
        db.delete_table(u'sales_customer')

        # Deleting model 'Order'
        db.delete_table(u'sales_order')


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
            'account': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounting.Account']", 'unique': 'True', 'blank': 'True'}),
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