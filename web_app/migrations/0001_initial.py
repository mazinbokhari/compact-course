# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Problem'
        db.create_table(u'web_app_problem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('question', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'web_app', ['Problem'])

        # Adding model 'Choice'
        db.create_table(u'web_app_choice', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('problem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['web_app.Problem'])),
            ('choice_text', self.gf('django.db.models.fields.TextField')()),
            ('correct_choice', self.gf('django.db.models.fields.BooleanField')()),
        ))
        db.send_create_signal(u'web_app', ['Choice'])

        # Adding model 'Quiz'
        db.create_table(u'web_app_quiz', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'web_app', ['Quiz'])

        # Adding M2M table for field problems on 'Quiz'
        m2m_table_name = db.shorten_name(u'web_app_quiz_problems')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('quiz', models.ForeignKey(orm[u'web_app.quiz'], null=False)),
            ('problem', models.ForeignKey(orm[u'web_app.problem'], null=False))
        ))
        db.create_unique(m2m_table_name, ['quiz_id', 'problem_id'])

        # Adding model 'Section'
        db.create_table(u'web_app_section', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'web_app', ['Section'])

        # Adding M2M table for field subsections on 'Section'
        m2m_table_name = db.shorten_name(u'web_app_section_subsections')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_section', models.ForeignKey(orm[u'web_app.section'], null=False)),
            ('to_section', models.ForeignKey(orm[u'web_app.section'], null=False))
        ))
        db.create_unique(m2m_table_name, ['from_section_id', 'to_section_id'])

        # Adding model 'Lesson'
        db.create_table(u'web_app_lesson', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'web_app', ['Lesson'])

        # Adding M2M table for field sections on 'Lesson'
        m2m_table_name = db.shorten_name(u'web_app_lesson_sections')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('lesson', models.ForeignKey(orm[u'web_app.lesson'], null=False)),
            ('section', models.ForeignKey(orm[u'web_app.section'], null=False))
        ))
        db.create_unique(m2m_table_name, ['lesson_id', 'section_id'])

        # Adding model 'CompactReview'
        db.create_table(u'web_app_compactreview', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal(u'web_app', ['CompactReview'])

        # Adding M2M table for field sections on 'CompactReview'
        m2m_table_name = db.shorten_name(u'web_app_compactreview_sections')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('compactreview', models.ForeignKey(orm[u'web_app.compactreview'], null=False)),
            ('section', models.ForeignKey(orm[u'web_app.section'], null=False))
        ))
        db.create_unique(m2m_table_name, ['compactreview_id', 'section_id'])

        # Adding model 'Chapter'
        db.create_table(u'web_app_chapter', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('preview', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='./chapter_images/chapter_image.png', max_length=100, null=True, blank=True)),
            ('compact_review', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web_app.CompactReview'], unique=True, null=True, blank=True)),
            ('lesson', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web_app.Lesson'], unique=True, null=True, blank=True)),
            ('quiz', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['web_app.Quiz'], unique=True, null=True, blank=True)),
        ))
        db.send_create_signal(u'web_app', ['Chapter'])

        # Adding model 'Subject'
        db.create_table(u'web_app_subject', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('preview', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(default='./subject_images/subject_image.png', max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'web_app', ['Subject'])

        # Adding M2M table for field chapters on 'Subject'
        m2m_table_name = db.shorten_name(u'web_app_subject_chapters')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('subject', models.ForeignKey(orm[u'web_app.subject'], null=False)),
            ('chapter', models.ForeignKey(orm[u'web_app.chapter'], null=False))
        ))
        db.create_unique(m2m_table_name, ['subject_id', 'chapter_id'])

        # Adding model 'SubjectType'
        db.create_table(u'web_app_subjecttype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'web_app', ['SubjectType'])

        # Adding M2M table for field subjects on 'SubjectType'
        m2m_table_name = db.shorten_name(u'web_app_subjecttype_subjects')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('subjecttype', models.ForeignKey(orm[u'web_app.subjecttype'], null=False)),
            ('subject', models.ForeignKey(orm[u'web_app.subject'], null=False))
        ))
        db.create_unique(m2m_table_name, ['subjecttype_id', 'subject_id'])

        # Adding model 'CourseType'
        db.create_table(u'web_app_coursetype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.TextField')()),
            ('slug', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'web_app', ['CourseType'])

        # Adding M2M table for field subject_types on 'CourseType'
        m2m_table_name = db.shorten_name(u'web_app_coursetype_subject_types')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('coursetype', models.ForeignKey(orm[u'web_app.coursetype'], null=False)),
            ('subjecttype', models.ForeignKey(orm[u'web_app.subjecttype'], null=False))
        ))
        db.create_unique(m2m_table_name, ['coursetype_id', 'subjecttype_id'])


    def backwards(self, orm):
        # Deleting model 'Problem'
        db.delete_table(u'web_app_problem')

        # Deleting model 'Choice'
        db.delete_table(u'web_app_choice')

        # Deleting model 'Quiz'
        db.delete_table(u'web_app_quiz')

        # Removing M2M table for field problems on 'Quiz'
        db.delete_table(db.shorten_name(u'web_app_quiz_problems'))

        # Deleting model 'Section'
        db.delete_table(u'web_app_section')

        # Removing M2M table for field subsections on 'Section'
        db.delete_table(db.shorten_name(u'web_app_section_subsections'))

        # Deleting model 'Lesson'
        db.delete_table(u'web_app_lesson')

        # Removing M2M table for field sections on 'Lesson'
        db.delete_table(db.shorten_name(u'web_app_lesson_sections'))

        # Deleting model 'CompactReview'
        db.delete_table(u'web_app_compactreview')

        # Removing M2M table for field sections on 'CompactReview'
        db.delete_table(db.shorten_name(u'web_app_compactreview_sections'))

        # Deleting model 'Chapter'
        db.delete_table(u'web_app_chapter')

        # Deleting model 'Subject'
        db.delete_table(u'web_app_subject')

        # Removing M2M table for field chapters on 'Subject'
        db.delete_table(db.shorten_name(u'web_app_subject_chapters'))

        # Deleting model 'SubjectType'
        db.delete_table(u'web_app_subjecttype')

        # Removing M2M table for field subjects on 'SubjectType'
        db.delete_table(db.shorten_name(u'web_app_subjecttype_subjects'))

        # Deleting model 'CourseType'
        db.delete_table(u'web_app_coursetype')

        # Removing M2M table for field subject_types on 'CourseType'
        db.delete_table(db.shorten_name(u'web_app_coursetype_subject_types'))


    models = {
        u'web_app.chapter': {
            'Meta': {'object_name': 'Chapter'},
            'compact_review': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web_app.CompactReview']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'./chapter_images/chapter_image.png'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'lesson': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web_app.Lesson']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'preview': ('django.db.models.fields.TextField', [], {}),
            'quiz': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['web_app.Quiz']", 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'web_app.choice': {
            'Meta': {'object_name': 'Choice'},
            'choice_text': ('django.db.models.fields.TextField', [], {}),
            'correct_choice': ('django.db.models.fields.BooleanField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['web_app.Problem']"})
        },
        u'web_app.compactreview': {
            'Meta': {'object_name': 'CompactReview'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sections': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['web_app.Section']", 'symmetrical': 'False'})
        },
        u'web_app.coursetype': {
            'Meta': {'object_name': 'CourseType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slug': ('django.db.models.fields.TextField', [], {}),
            'subject_types': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['web_app.SubjectType']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'web_app.lesson': {
            'Meta': {'object_name': 'Lesson'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'sections': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['web_app.Section']", 'symmetrical': 'False'})
        },
        u'web_app.problem': {
            'Meta': {'object_name': 'Problem'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'question': ('django.db.models.fields.TextField', [], {})
        },
        u'web_app.quiz': {
            'Meta': {'object_name': 'Quiz'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'problems': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['web_app.Problem']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'web_app.section': {
            'Meta': {'object_name': 'Section'},
            'content': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subsections': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'subsections_rel_+'", 'to': u"orm['web_app.Section']"}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'web_app.subject': {
            'Meta': {'object_name': 'Subject'},
            'chapters': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['web_app.Chapter']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'default': "'./subject_images/subject_image.png'", 'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'preview': ('django.db.models.fields.TextField', [], {}),
            'slug': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.TextField', [], {})
        },
        u'web_app.subjecttype': {
            'Meta': {'object_name': 'SubjectType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'subjects': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['web_app.Subject']", 'symmetrical': 'False'}),
            'title': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['web_app']