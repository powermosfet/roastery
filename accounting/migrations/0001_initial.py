# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Account'
        db.create_table(u'accounting_account', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('account_type', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('balance', self.gf('django.db.models.fields.DecimalField')(default=0, max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal(u'accounting', ['Account'])

        # Adding model 'Transaction'
        db.create_table(u'accounting_transaction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('time', self.gf('django.db.models.fields.TimeField')()),
            ('sender', self.gf('django.db.models.fields.related.ForeignKey')(related_name='transactions_outbound', to=orm['accounting.Account'])),
            ('receiver', self.gf('django.db.models.fields.related.ForeignKey')(related_name='transactions_inbound', to=orm['accounting.Account'])),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=8, decimal_places=2)),
        ))
        db.send_create_signal(u'accounting', ['Transaction'])


    def backwards(self, orm):
        # Deleting model 'Account'
        db.delete_table(u'accounting_account')

        # Deleting model 'Transaction'
        db.delete_table(u'accounting_transaction')


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
        }
    }

    complete_apps = ['accounting']