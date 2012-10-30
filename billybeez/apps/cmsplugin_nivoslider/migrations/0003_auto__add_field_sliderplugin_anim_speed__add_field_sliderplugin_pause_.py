# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'SliderPlugin.anim_speed'
        db.add_column('cmsplugin_sliderplugin', 'anim_speed', self.gf('django.db.models.fields.PositiveIntegerField')(default=500), keep_default=False)

        # Adding field 'SliderPlugin.pause_time'
        db.add_column('cmsplugin_sliderplugin', 'pause_time', self.gf('django.db.models.fields.PositiveIntegerField')(default=3000), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'SliderPlugin.anim_speed'
        db.delete_column('cmsplugin_sliderplugin', 'anim_speed')

        # Deleting field 'SliderPlugin.pause_time'
        db.delete_column('cmsplugin_sliderplugin', 'pause_time')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'cmsplugin_nivoslider.slideralbum': {
            'Meta': {'object_name': 'SliderAlbum'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'images': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['cmsplugin_nivoslider.SliderImage']", 'symmetrical': 'False', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'cmsplugin_nivoslider.sliderimage': {
            'Meta': {'ordering': "('order', 'name')", 'object_name': 'SliderImage'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveIntegerField', [], {'default': '100'})
        },
        'cmsplugin_nivoslider.sliderplugin': {
            'Meta': {'object_name': 'SliderPlugin', 'db_table': "'cmsplugin_sliderplugin'", '_ormbases': ['cms.CMSPlugin']},
            'album': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cmsplugin_nivoslider.SliderAlbum']"}),
            'anim_speed': ('django.db.models.fields.PositiveIntegerField', [], {'default': '500'}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'effect': ('django.db.models.fields.CharField', [], {'default': "'random'", 'max_length': '50'}),
            'pause_time': ('django.db.models.fields.PositiveIntegerField', [], {'default': '3000'}),
            'theme': ('django.db.models.fields.CharField', [], {'default': "'default'", 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cmsplugin_nivoslider']
