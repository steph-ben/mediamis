# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Media.thumbnail'
        db.add_column('friendlib_media', 'thumbnail', self.gf('django.db.models.fields.files.ImageField')(default=None, max_length=100, null=True, blank=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Media.thumbnail'
        db.delete_column('friendlib_media', 'thumbnail')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'friendlib.boardgame': {
            'Meta': {'object_name': 'BoardGame', '_ormbases': ['friendlib.Media']},
            'media_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['friendlib.Media']", 'unique': 'True', 'primary_key': 'True'}),
            'number_players': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'friendlib.book': {
            'Meta': {'object_name': 'Book', '_ormbases': ['friendlib.Media']},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'media_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['friendlib.Media']", 'unique': 'True', 'primary_key': 'True'}),
            'nb_pages': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'friendlib.divx': {
            'Meta': {'object_name': 'Divx', '_ormbases': ['friendlib.Movie']},
            'movie_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['friendlib.Movie']", 'unique': 'True', 'primary_key': 'True'}),
            'quality': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        'friendlib.dvd': {
            'Meta': {'object_name': 'DVD', '_ormbases': ['friendlib.Movie']},
            'movie_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['friendlib.Movie']", 'unique': 'True', 'primary_key': 'True'}),
            'number_of_disc': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'friendlib.media': {
            'Meta': {'object_name': 'Media'},
            'borrowed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'borrower': ('django.db.models.fields.related.ForeignKey', [], {'default': 'None', 'related_name': "'borrowed_medias'", 'null': 'True', 'blank': 'True', 'to': "orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owned_medias'", 'to': "orm['auth.User']"}),
            'specialization_type': ('django.db.models.fields.TextField', [], {'db_index': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'default': 'None', 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'friendlib.mediarequest': {
            'Meta': {'object_name': 'MediaRequest'},
            'borrower': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'requested_medias'", 'to': "orm['auth.User']"}),
            'date_answered': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_media_rented': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_requested': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'date_return_due': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'date_status_updated': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'media': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'requests'", 'to': "orm['friendlib.Media']"}),
            'message': ('django.db.models.fields.TextField', [], {}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'friendlib.movie': {
            'Meta': {'object_name': 'Movie', '_ormbases': ['friendlib.Media']},
            'allocine_id': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'media_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['friendlib.Media']", 'unique': 'True', 'primary_key': 'True'})
        }
    }

    complete_apps = ['friendlib']
