# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Media'
        db.create_table('friendlib_media', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('specialization_type', self.gf('django.db.models.fields.TextField')(db_index=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('owner', self.gf('django.db.models.fields.related.ForeignKey')(related_name='owned_medias', to=orm['auth.User'])),
            ('borrower', self.gf('django.db.models.fields.related.ForeignKey')(default=None, related_name='borrowed_medias', null=True, blank=True, to=orm['auth.User'])),
            ('borrowed', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('friendlib', ['Media'])

        # Adding model 'Book'
        db.create_table('friendlib_book', (
            ('media_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['friendlib.Media'], unique=True, primary_key=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('nb_pages', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('friendlib', ['Book'])

        # Adding model 'Movie'
        db.create_table('friendlib_movie', (
            ('media_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['friendlib.Media'], unique=True, primary_key=True)),
            ('allocine_id', self.gf('django.db.models.fields.PositiveIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('friendlib', ['Movie'])

        # Adding model 'DVD'
        db.create_table('friendlib_dvd', (
            ('movie_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['friendlib.Movie'], unique=True, primary_key=True)),
            ('number_of_disc', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('friendlib', ['DVD'])

        # Adding model 'Divx'
        db.create_table('friendlib_divx', (
            ('movie_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['friendlib.Movie'], unique=True, primary_key=True)),
            ('quality', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('friendlib', ['Divx'])

        # Adding model 'BoardGame'
        db.create_table('friendlib_boardgame', (
            ('media_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['friendlib.Media'], unique=True, primary_key=True)),
            ('number_players', self.gf('django.db.models.fields.PositiveSmallIntegerField')(null=True, blank=True)),
        ))
        db.send_create_signal('friendlib', ['BoardGame'])

        # Adding model 'MediaRequest'
        db.create_table('friendlib_mediarequest', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('media', self.gf('django.db.models.fields.related.ForeignKey')(related_name='requests', to=orm['friendlib.Media'])),
            ('borrower', self.gf('django.db.models.fields.related.ForeignKey')(related_name='requested_medias', to=orm['auth.User'])),
            ('message', self.gf('django.db.models.fields.TextField')()),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('date_status_updated', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('date_requested', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('date_answered', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('date_media_rented', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('date_return_due', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('friendlib', ['MediaRequest'])


    def backwards(self, orm):
        
        # Deleting model 'Media'
        db.delete_table('friendlib_media')

        # Deleting model 'Book'
        db.delete_table('friendlib_book')

        # Deleting model 'Movie'
        db.delete_table('friendlib_movie')

        # Deleting model 'DVD'
        db.delete_table('friendlib_dvd')

        # Deleting model 'Divx'
        db.delete_table('friendlib_divx')

        # Deleting model 'BoardGame'
        db.delete_table('friendlib_boardgame')

        # Deleting model 'MediaRequest'
        db.delete_table('friendlib_mediarequest')


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
