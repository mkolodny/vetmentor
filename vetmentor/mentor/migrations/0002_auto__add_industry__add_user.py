# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Industry'
        db.create_table(u'industries', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('code', self.gf('django.db.models.fields.SmallIntegerField')()),
        ))
        db.send_create_signal(u'mentor', ['Industry'])

        # Adding model 'User'
        db.create_table(u'users', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('USERNAME_FIELD', self.gf('django.db.models.fields.TextField')()),
            ('email', self.gf('django.db.models.fields.TextField')(db_index=True)),
            ('birthday', self.gf('django.db.models.fields.DateField')()),
            ('gender', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('category', self.gf('django.db.models.fields.SmallIntegerField')()),
            ('location', self.gf('django.db.models.fields.TextField')()),
            ('industry', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mentor.Industry'], on_delete=models.PROTECT)),
            ('bio', self.gf('django.db.models.fields.TextField')(null=True)),
            ('why_joined', self.gf('django.db.models.fields.TextField')(null=True)),
            ('date_joined', self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 10, 13, 0, 0))),
            ('rank', self.gf('django.db.models.fields.TextField')(null=True)),
            ('service_location', self.gf('django.db.models.fields.TextField')(null=True)),
            ('service_start_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('service_end_date', self.gf('django.db.models.fields.DateField')(null=True)),
            ('education', self.gf('django.db.models.fields.SmallIntegerField')(null=True)),
        ))
        db.send_create_signal(u'mentor', ['User'])


    def backwards(self, orm):
        # Deleting model 'Industry'
        db.delete_table(u'industries')

        # Deleting model 'User'
        db.delete_table(u'users')


    models = {
        u'mentor.industry': {
            'Meta': {'object_name': 'Industry', 'db_table': "u'industries'"},
            'code': ('django.db.models.fields.SmallIntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'mentor.user': {
            'Meta': {'object_name': 'User', 'db_table': "u'users'"},
            'USERNAME_FIELD': ('django.db.models.fields.TextField', [], {}),
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
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'rank': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'service_end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'service_location': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'service_start_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'why_joined': ('django.db.models.fields.TextField', [], {'null': 'True'})
        }
    }

    complete_apps = ['mentor']