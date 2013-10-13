# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'User.USERNAME_FIELD'
        db.delete_column(u'users', 'USERNAME_FIELD')

        # Adding field 'User.name'
        db.add_column(u'users', 'name',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'User.USERNAME_FIELD'
        db.add_column(u'users', 'USERNAME_FIELD',
                      self.gf('django.db.models.fields.TextField')(default=''),
                      keep_default=False)

        # Deleting field 'User.name'
        db.delete_column(u'users', 'name')


    models = {
        u'mentor.industry': {
            'Meta': {'object_name': 'Industry', 'db_table': "u'industries'"},
            'code': ('django.db.models.fields.SmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'mentor.user': {
            'Meta': {'object_name': 'User', 'db_table': "u'users'"},
            'bio': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'birthday': ('django.db.models.fields.DateField', [], {}),
            'category': ('django.db.models.fields.SmallIntegerField', [], {}),
            'date_joined': ('django.db.models.fields.DateField', [], {'default': 'datetime.datetime(2013, 10, 13, 0, 0)'}),
            'education': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True'}),
            'email': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'gender': ('django.db.models.fields.SmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'industry': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['mentor.Industry']", 'on_delete': 'models.PROTECT'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'location': ('django.db.models.fields.TextField', [], {}),
            'name': ('django.db.models.fields.TextField', [], {}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'rank': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'service_end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'service_location': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'service_start_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'why_joined': ('django.db.models.fields.TextField', [], {'null': 'True'})
        }
    }

    complete_apps = ['mentor']