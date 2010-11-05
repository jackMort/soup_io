# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Author'
        db.create_table('core_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('login', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('core', ['Author'])

        # Adding M2M table for field posts on 'Author'
        db.create_table('core_author_posts', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('author', models.ForeignKey(orm['core.author'], null=False)),
            ('post', models.ForeignKey(orm['core.post'], null=False))
        ))
        db.create_unique('core_author_posts', ['author_id', 'post_id'])

        # Adding model 'Image'
        db.create_table('core_image', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.related.ForeignKey')(related_name='image_author', to=orm['core.Author'])),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('core', ['Image'])

        # Adding model 'Post'
        db.create_table('core_post', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('image', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Image'])),
            ('via', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['core.Author'], null=True, blank=True)),
            ('original_id', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('core', ['Post'])


    def backwards(self, orm):
        
        # Deleting model 'Author'
        db.delete_table('core_author')

        # Removing M2M table for field posts on 'Author'
        db.delete_table('core_author_posts')

        # Deleting model 'Image'
        db.delete_table('core_image')

        # Deleting model 'Post'
        db.delete_table('core_post')


    models = {
        'core.author': {
            'Meta': {'object_name': 'Author'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'login': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'posts': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['core.Post']", 'null': 'True', 'blank': 'True'})
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
