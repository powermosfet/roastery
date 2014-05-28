# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Batch'
        db.create_table(u'roast_batch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['inventory.CoffeeBag'])),
            ('initial_weight', self.gf('django.db.models.fields.FloatField')()),
            ('date', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('ambient_temp', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('program', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('target_temp', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('target_time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('final_weight', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('order', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sales.Order'])),
        ))
        db.send_create_signal(u'roast', ['Batch'])

        # Adding model 'RoastPoint'
        db.create_table(u'roast_roastpoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.TimeField')()),
            ('temp', self.gf('django.db.models.fields.FloatField')()),
            ('batch', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roast.Batch'])),
        ))
        db.send_create_signal(u'roast', ['RoastPoint'])

        # Adding model 'Event'
        db.create_table(u'roast_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'roast', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Batch'
        db.delete_table(u'roast_batch')

        # Deleting model 'RoastPoint'
        db.delete_table(u'roast_roastpoint')

        # Deleting model 'Event'
        db.delete_table(u'roast_event')


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
        },
        u'roast.batch': {
            'Meta': {'object_name': 'Batch'},
            'ambient_temp': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'bag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.CoffeeBag']"}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'final_weight': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'initial_weight': ('django.db.models.fields.FloatField', [], {}),
            'order': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sales.Order']"}),
            'program': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'target_temp': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'target_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'})
        },
        u'roast.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'roast.roastpoint': {
            'Meta': {'object_name': 'RoastPoint'},
            'batch': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roast.Batch']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'temp': ('django.db.models.fields.FloatField', [], {}),
            'time': ('django.db.models.fields.TimeField', [], {})
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

    complete_apps = ['roast']