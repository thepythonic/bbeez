# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'BillybeezGame'
        db.create_table('cmsplugin_billybeezgame', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('gallery_plugin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsplugin_gallery.GalleryPlugin'])),
            ('titiled_plugin', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsplugin_titledplugin.TitledPlugin'])),
        ))
        db.send_create_signal('cmsplugin_billybeezgames', ['BillybeezGame'])


    def backwards(self, orm):
        # Deleting model 'BillybeezGame'
        db.delete_table('cmsplugin_billybeezgame')


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
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
        'cmsplugin_billybeezgames.billybeezgame': {
            'Meta': {'object_name': 'BillybeezGame', 'db_table': "'cmsplugin_billybeezgame'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'gallery_plugin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cmsplugin_gallery.GalleryPlugin']"}),
            'titiled_plugin': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cmsplugin_titledplugin.TitledPlugin']"})
        },
        'cmsplugin_gallery.galleryplugin': {
            'Meta': {'object_name': 'GalleryPlugin', 'db_table': "'cmsplugin_galleryplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'template': ('django.db.models.fields.CharField', [], {'default': "'cmsplugin_gallery/gallery.html'", 'max_length': '255'})
        },
        'cmsplugin_titledplugin.titledplugin': {
            'Meta': {'object_name': 'TitledPlugin', 'db_table': "'cmsplugin_titledplugin'"},
            'body': ('django.db.models.fields.TextField', [], {}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'font': ('django.db.models.fields.CharField', [], {'default': "'Title Font'", 'max_length': '50'}),
            'span': ('django.db.models.fields.CharField', [], {'default': "'Width'", 'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "'Title'", 'max_length': '50'})
        }
    }

    complete_apps = ['cmsplugin_billybeezgames']