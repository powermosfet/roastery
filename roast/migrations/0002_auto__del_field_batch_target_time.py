# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Batch.target_time'
        db.delete_column(u'roast_batch', 'target_time')


    def backwards(self, orm):
        # Adding field 'Batch.target_time'
        db.add_column(u'roast_batch', 'target_time',
                      self.gf('django.db.models.fields.TimeField')(null=True, blank=True),
                      keep_default=False)


    models = {
        u'inventory.coffeebag': {
            'Meta': {'object_name': 'CoffeeBag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_date': ('django.db.models.fields.DateField', [], {}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
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
            'state': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'target_temp': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
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
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80'})
        },
        u'sales.order': {
            'Meta': {'object_name': 'Order'},
            'customer': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sales.Customer']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'done': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'quantity': ('django.db.models.fields.IntegerField', [], {}),
            'variety': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['inventory.Variety']"})
        }
    }

    complete_apps = ['roast']