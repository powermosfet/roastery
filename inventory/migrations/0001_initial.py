# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Vendor'
        db.create_table(u'inventory_vendor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('account', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounting.Account'], unique=True, blank=True)),
        ))
        db.send_create_signal(u'inventory', ['Vendor'])

        # Adding model 'Variety'
        db.create_table(u'inventory_variety', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('crop_year', self.gf('django.db.models.fields.CharField')(max_length=4, blank=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=180, blank=True)),
        ))
        db.send_create_signal(u'inventory', ['Variety'])

        # Adding model 'CoffeeBag'
        db.create_table(u'inventory_coffeebag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('variety', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Variety'])),
            ('vendor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.Vendor'])),
            ('order_date', self.gf('django.db.models.fields.DateField')()),
            ('cost', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounting.Transaction'], unique=True)),
            ('received_date', self.gf('django.db.models.fields.DateField')()),
            ('weight', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'inventory', ['CoffeeBag'])


    def backwards(self, orm):
        # Deleting model 'Vendor'
        db.delete_table(u'inventory_vendor')

        # Deleting model 'Variety'
        db.delete_table(u'inventory_variety')

        # Deleting model 'CoffeeBag'
        db.delete_table(u'inventory_coffeebag')


    models = {
        u'accounting.account': {
            'Meta': {'object_name': 'Account'},
            'account_type': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'balance': ('django.db.models.fields.DecimalField', [], {'default': '0', 'max_digits': '8', 'decimal_places': '2'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'})
        },
        u'accounting.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '8', 'decimal_places': '2'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'receiver': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transactions_inbound'", 'to': u"orm['accounting.Account']"}),
            'sender': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transactions_outbound'", 'to': u"orm['accounting.Account']"}),
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
            'account': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounting.Account']", 'unique': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['inventory']