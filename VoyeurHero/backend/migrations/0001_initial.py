# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'VHPost'
        db.create_table('backend_vhpost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('caption', self.gf('django.db.models.fields.CharField')(max_length=10000)),
            ('post_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('backend', ['VHPost'])

        # Adding M2M table for field categories on 'VHPost'
        db.create_table('backend_vhpost_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('vhpost', models.ForeignKey(orm['backend.vhpost'], null=False)),
            ('vhcategory', models.ForeignKey(orm['backend.vhcategory'], null=False))
        ))
        db.create_unique('backend_vhpost_categories', ['vhpost_id', 'vhcategory_id'])

        # Adding model 'VHCategory'
        db.create_table('backend_vhcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('backend', ['VHCategory'])

        # Adding M2M table for field posts on 'VHCategory'
        db.create_table('backend_vhcategory_posts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('vhcategory', models.ForeignKey(orm['backend.vhcategory'], null=False)),
            ('vhpost', models.ForeignKey(orm['backend.vhpost'], null=False))
        ))
        db.create_unique('backend_vhcategory_posts', ['vhcategory_id', 'vhpost_id'])


    def backwards(self, orm):
        
        # Deleting model 'VHPost'
        db.delete_table('backend_vhpost')

        # Removing M2M table for field categories on 'VHPost'
        db.delete_table('backend_vhpost_categories')

        # Deleting model 'VHCategory'
        db.delete_table('backend_vhcategory')

        # Removing M2M table for field posts on 'VHCategory'
        db.delete_table('backend_vhcategory_posts')


    models = {
        'backend.vhcategory': {
            'Meta': {'object_name': 'VHCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'posts': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['backend.VHPost']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'backend.vhpost': {
            'Meta': {'object_name': 'VHPost'},
            'caption': ('django.db.models.fields.CharField', [], {'max_length': '10000'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['backend.VHCategory']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'post_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['backend']
