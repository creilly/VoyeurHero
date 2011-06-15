# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'VHPost.picture'
        db.alter_column('backend_vhpost', 'picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True))


    def backwards(self, orm):
        
        # Changing field 'VHPost.picture'
        db.alter_column('backend_vhpost', 'picture', self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100))


    models = {
        'backend.vhcategory': {
            'Meta': {'object_name': 'VHCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['backend.VHPost']", 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'backend.vhpost': {
            'Meta': {'object_name': 'VHPost'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['backend.VHCategory']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['backend']
