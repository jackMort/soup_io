# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Author.virtual'
        db.add_column('core_author', 'virtual', self.gf('django.db.models.fields.BooleanField')(default=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Author.virtual'
        db.delete_column('core_author', 'virtual')


    models = {
        'core.author': {
            'Meta': {'object_name': 'Author'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'posts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['core.Post']", 'null': 'True', 'blank': 'True'}),
            'virtual': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'})
        },
        'core.image': {
            'Meta': {'object_name': 'Image'},
            'author': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'image_author'", 'to': "orm['core.Author']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'core.post': {
            'Meta': {'object_name': 'Post'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Image']"}),
            'original_id': ('django.db.models.fields.IntegerField', [], {}),
            'via': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['core.Author']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['core']
