# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'SliderImage'
        db.create_table('cmsplugin_nivoslider_sliderimage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('order', self.gf('django.db.models.fields.PositiveIntegerField')(default=100)),
        ))
        db.send_create_signal('cmsplugin_nivoslider', ['SliderImage'])

        # Adding model 'SliderAlbum'
        db.create_table('cmsplugin_nivoslider_slideralbum', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
        ))
        db.send_create_signal('cmsplugin_nivoslider', ['SliderAlbum'])

        # Adding M2M table for field images on 'SliderAlbum'
        db.create_table('cmsplugin_nivoslider_slideralbum_images', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('slideralbum', models.ForeignKey(orm['cmsplugin_nivoslider.slideralbum'], null=False)),
            ('sliderimage', models.ForeignKey(orm['cmsplugin_nivoslider.sliderimage'], null=False))
        ))
        db.create_unique('cmsplugin_nivoslider_slideralbum_images', ['slideralbum_id', 'sliderimage_id'])

        # Adding model 'SliderPlugin'
        db.create_table('cmsplugin_sliderplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('album', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cmsplugin_nivoslider.SliderAlbum'])),
        ))
        db.send_create_signal('cmsplugin_nivoslider', ['SliderPlugin'])


    def backwards(self, orm):
        
        # Deleting model 'SliderImage'
        db.delete_table('cmsplugin_nivoslider_sliderimage')

        # Deleting model 'SliderAlbum'
        db.delete_table('cmsplugin_nivoslider_slideralbum')

        # Removing M2M table for field images on 'SliderAlbum'
        db.delete_table('cmsplugin_nivoslider_slideralbum_images')

        # Deleting model 'SliderPlugin'
        db.delete_table('cmsplugin_sliderplugin')


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
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['cmsplugin_nivoslider']
