# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Vendor'
        db.create_table(u'roast_vendor', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
        ))
        db.send_create_signal(u'roast', ['Vendor'])

        # Adding model 'Variety'
        db.create_table(u'roast_variety', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('area', self.gf('django.db.models.fields.CharField')(max_length=80)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=180)),
        ))
        db.send_create_signal(u'roast', ['Variety'])

        # Adding model 'CoffeeBag'
        db.create_table(u'roast_coffeebag', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('variety', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roast.Variety'])),
            ('vendor', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roast.Vendor'])),
            ('order_date', self.gf('django.db.models.fields.DateField')()),
            ('received_date', self.gf('django.db.models.fields.DateField')()),
            ('weight', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'roast', ['CoffeeBag'])

        # Adding model 'Batch'
        db.create_table(u'roast_batch', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bag', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roast.CoffeeBag'])),
            ('weight', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'roast', ['Batch'])

        # Adding model 'Roast'
        db.create_table(u'roast_roast', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('batch', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['roast.Batch'], unique=True)),
            ('ambient_temp', self.gf('django.db.models.fields.FloatField')()),
            ('program', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('target_temp', self.gf('django.db.models.fields.FloatField')()),
            ('target_time', self.gf('django.db.models.fields.TimeField')()),
            ('final_weight', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal(u'roast', ['Roast'])

        # Adding model 'RoastPoint'
        db.create_table(u'roast_roastpoint', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.TimeField')()),
            ('temp', self.gf('django.db.models.fields.FloatField')()),
            ('roast', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['roast.Roast'])),
        ))
        db.send_create_signal(u'roast', ['RoastPoint'])

        # Adding model 'Event'
        db.create_table(u'roast_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'roast', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Vendor'
        db.delete_table(u'roast_vendor')

        # Deleting model 'Variety'
        db.delete_table(u'roast_variety')

        # Deleting model 'CoffeeBag'
        db.delete_table(u'roast_coffeebag')

        # Deleting model 'Batch'
        db.delete_table(u'roast_batch')

        # Deleting model 'Roast'
        db.delete_table(u'roast_roast')

        # Deleting model 'RoastPoint'
        db.delete_table(u'roast_roastpoint')

        # Deleting model 'Event'
        db.delete_table(u'roast_event')


    models = {
        u'roast.batch': {
            'Meta': {'object_name': 'Batch'},
            'bag': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roast.CoffeeBag']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'weight': ('django.db.models.fields.FloatField', [], {})
        },
        u'roast.coffeebag': {
            'Meta': {'object_name': 'CoffeeBag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'order_date': ('django.db.models.fields.DateField', [], {}),
            'received_date': ('django.db.models.fields.DateField', [], {}),
            'variety': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roast.Variety']"}),
            'vendor': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roast.Vendor']"}),
            'weight': ('django.db.models.fields.FloatField', [], {})
        },
        u'roast.event': {
            'Meta': {'object_name': 'Event'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'roast.roast': {
            'Meta': {'object_name': 'Roast'},
            'ambient_temp': ('django.db.models.fields.FloatField', [], {}),
            'batch': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['roast.Batch']", 'unique': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'final_weight': ('django.db.models.fields.FloatField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'program': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'target_temp': ('django.db.models.fields.FloatField', [], {}),
            'target_time': ('django.db.models.fields.TimeField', [], {})
        },
        u'roast.roastpoint': {
            'Meta': {'object_name': 'RoastPoint'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'roast': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['roast.Roast']"}),
            'temp': ('django.db.models.fields.FloatField', [], {}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
        u'roast.variety': {
            'Meta': {'object_name': 'Variety'},
            'area': ('django.db.models.fields.CharField', [], {'max_length': '80'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'roast.vendor': {
            'Meta': {'object_name': 'Vendor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['roast']