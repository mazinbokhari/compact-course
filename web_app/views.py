from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils.text import slugify
from web_app.models import *


def splash(request):
    return render_to_response('web_app/splash.html')


def courses_page(request, course_type_slug):
    course_type = CourseType.objects.filter(slug=course_type_slug)[0]
    subject_types = [course_type.subject_types.get(title="Math"),
                     course_type.subject_types.get(title="Science"),
                     course_type.subject_types.get(title="Social Studies"),
                     course_type.subject_types.get(title="Language")]

    return render_to_response('web_app/base_listing.html',
                              {'course_type': course_type,
                               'subject_types': subject_types},
                              RequestContext(request))


def chapter_page(request, course_slug):
    subject = Subject.objects.get(slug=course_slug)
    subject_types = SubjectType.objects.all()

    subject_type = [_ for _ in subject_types if subject in _.subjects.all()][0]
    course_type = [_ for _ in CourseType.objects.all() if subject_type in _.subject_types.all()][0]

    chapters = subject.chapters.all()

    return render_to_response('web_app/course_page.html',
                              {'subject_types': subject_types,
                               'course_type': course_type,
                               'subject_type': subject_type,
                               'subject': subject,
                               'chapters': chapters},
                              RequestContext(request))


def chapter(request, course_slug, chapter_slug):
    subject = Subject.objects.get(slug=course_slug)
    subject_types = SubjectType.objects.all()

    subject_type = [_ for _ in subject_types if subject in _.subjects.all()][0]
    course_type = [_ for _ in CourseType.objects.all() if subject_type in _.subject_types.all()][0]

    chapters = subject.chapters.all()
    chapter = subject.chapters.get(slug=chapter_slug)

    path = request.get_full_path().split('/')[-1]
    if path == 'lesson':
        sections = chapter.lesson.sections.all()
    elif path == 'compact-review':
        sections = chapter.compact_review.sections.all()
    elif path == 'problems':
        pass
        # sections = chapter.lesson.sections.all()

    return render_to_response('web_app/chapter.html',
                              {'chapter_type': path,
                               'subject_types': subject_types,
                               'course_type': course_type,
                               'subject_type': subject_type,
                               'subject': subject,
                               'chapters': chapters,
                               'chapter': chapter,
                               'sections': sections},
                              RequestContext(request))


def submit(request):
    if request.method == "POST":
        form = ChapterForm(request.POST)

        form.is_valid()

        try:
            subsection = form.cleaned_data['subsection']
            sub_content = form.cleaned_data['sub_content']
            sub = True
        except Exception as e:
            sub = False

        try:
            subject = form.cleaned_data['subject']
            subject_object = Subject.objects.get(slug=slugify(unicode(subject)))

            chapter = form.cleaned_data['chapter']
            chapter_object = subject_object.chapters.get(slug=slugify(unicode(chapter)))

            section = form.cleaned_data['section']
            section_object = chapter_object.lesson.sections.get(title=section)

            content = form.cleaned_data['content']
            section_object.content = content

            if sub:
                try:
                    subsection_object = section_object.subsections.get(title=subsection)
                    subsection_object.content = sub_content
                    subsection_object.save()
                except Exception as e:
                    return render_to_response('web_app/submit.html',
                                              {'success': False,
                                               'error': str(e)},
                                              RequestContext(request))

            section_object.save()
            return render_to_response('web_app/submit.html',
                                      {'success': True,
                                       'error': "POSTED"},
                                      RequestContext(request))

        except Exception as e:
            return render_to_response('web_app/submit.html',
                                      {'success': False,
                                       'error': str(e)},
                                      RequestContext(request))


    elif request.method == "GET":
        return render_to_response('web_app/submit.html',
                                  {'success': True,
                                   'error': None},
                                  RequestContext(request))

# def chapter_quiz(request, course_slug, chapter_slug):
