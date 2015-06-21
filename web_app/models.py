from django.db import models
from django import forms


class Problem(models.Model):
    question = models.TextField()


class Choice(models.Model):
    problem = models.ForeignKey(Problem)
    choice_text = models.TextField()
    correct_choice = models.BooleanField()


class Quiz(models.Model):
    title = models.TextField()
    problems = models.ManyToManyField(Problem)


class Section(models.Model):
    '''
    e.g. Motion Definitions, Graphic Relationships, etc.
    '''

    title = models.TextField()
    content = models.TextField()
    subsections = models.ManyToManyField('self')

    def __unicode__(self):
        return "{0}, {1}".format(self.title, self.content)


class Lesson(models.Model):
    sections = models.ManyToManyField(Section)

    def __unicode__(self):
        return "{0}".format(self.sections.all())


class CompactReview(models.Model):
    sections = models.ManyToManyField(Section)

    def __unicode__(self):
        return "{0}".format(self.sections.all())


class Chapter(models.Model):
    '''
    e.g. Vectors, Kinematics, etc.
    '''

    title = models.TextField()
    preview = models.TextField()
    slug = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='./chapter_images/', default='./chapter_images/chapter_image.png')

    compact_review = models.OneToOneField(CompactReview, null=True, blank=True)
    lesson = models.OneToOneField(Lesson, null=True, blank=True)
    quiz = models.OneToOneField(Quiz, null=True, blank=True)

    def __unicode__(self):
        return "{0}, {1}".format(self.title, self.preview)


class Subject(models.Model):
    '''
    e.g. AP Physics B, etc.
    '''

    title = models.TextField()
    preview = models.TextField()
    slug = models.TextField()
    image = models.ImageField(blank=True, null=True, upload_to='./subject_images/', default='./subject_images/subject_image.png')

    chapters = models.ManyToManyField(Chapter)

    def __unicode__(self):
        return "{0}, {1}".format(self.title, self.preview)


class SubjectType(models.Model):
    '''
    e.g. Math, science, etc.
    '''

    title = models.TextField()
    subjects = models.ManyToManyField(Subject)


    def get_all_subjects(self):
        return sorted(self.subjects.all(), key=lambda subject: subject.title)

    def __unicode__(self):
        return "{0}, {1}".format(self.title, self.subjects.all())


class CourseType(models.Model):
    '''
    e.g. AP Courses, College Courses, etc.
    '''

    title = models.TextField()
    slug = models.TextField()
    subject_types = models.ManyToManyField(SubjectType)

    def __unicode__(self):
        return "{0}, {1}".format(self.title, self.subject_types.all())


class ChapterForm(forms.Form):
    subject = forms.CharField()
    chapter = forms.CharField()
    section = forms.CharField()
    content = forms.CharField()
    subsection = forms.CharField()
    sub_content = forms.CharField()
