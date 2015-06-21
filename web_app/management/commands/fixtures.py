from web_app.models import *
from django.utils.text import slugify

ss = [Section(title='asdf', content='test'),
Section(title='Motiondfs F', content='SHIT'),
Section(title='Motiodfsn A', content='??'),
Section(title='Motiosdfn D', content='HM'),
Section(title='Motidsfon G', content='B')]

for sub in ss:
    sub.save()

sections = [Section(title='Motion Definitions', content='test'),
Section(title='Motion F', content='SHIT'),
Section(title='Motion A', content='??'),
Section(title='Motion D', content='HM'),
Section(title='Motion G', content='B')]

for s in sections:
    s.save()
    for sub in ss:
        s.subsections.add(sub)
        s.save()

l = Lesson()
l.save()

for s in sections:
    l.sections.add(s)
    l.save()

cccc = Section(title='CR1', content='does this work?')
cccc.save()

cr = CompactReview()
cr.save()
cr.sections.add(cccc)
cr.save()

ch = Chapter(title='Vectors', preview='preview', lesson=l, compact_review=cr, slug=slugify(u'Vectors'))
ch.save()

co = Subject(title='Physics B', preview='ap phys b preview', slug=slugify(u'Physics B'))
co.save()
co.chapters.add(ch)
co.save()

t = SubjectType(title='Science')
t.save()
t.subjects.add(co)
t.save()

ct = CourseType(title='AP Courses', slug=slugify(u'AP Courses'))
ct.save()
ct.subject_types.add(t)
ct.save()


