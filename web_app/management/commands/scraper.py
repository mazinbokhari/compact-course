from django.core.management.base import BaseCommand, CommandError
from web_app.models import *

from bs4 import BeautifulSoup, Tag, NavigableString
from itertools import takewhile, chain
from os import listdir, getcwd

class Command(BaseCommand):
    help = 'Funnel lessons into database.'

    def handle(self, *args, **options):
        def get_section_title_and_content(soup, from_tag, until_tag):
            for big in soup(from_tag):
                until = big.findNext(until_tag)

                strings = (node for node in big.nextSiblingGenerator() if node.__repr__())
                selected = takewhile(lambda node: node != until, strings)
                try:
                    yield (big.text, ''.join(node.__repr__() for node in chain([next(selected)], selected)))
                except StopIteration as e:
                    pass


        def strip_tags(html, invalid_tags):
            soup = BeautifulSoup(html)

            for tag in soup.find_all(True):
                if tag.name in invalid_tags:
                    s = ""

                    for c in tag.contents:
                        if not isinstance(c, NavigableString):
                            c = strip_tags(unicode(c), invalid_tags)
                        s += unicode(c)

                    tag.replaceWith(s)

            return soup


        def get_or_create_subject(filename):
            slug = ''.join(filename.split(" - ")[0])
            try:
                subject = Subject.objects.get(slug=slug)
            except:
                subject = Subject(slug=slug, title=slug.replace("-", " ").title(), preview='')
                subject.save()

            return subject


        files = listdir('./web_app/management/lessons/')

        for filename in files:
            subject = get_or_create_subject(filename)

            # Create the chapter that this lesson belongs to
            c = Chapter()
            c.slug = filename.split(" - ")[-1].split(".")[0]
            c.title = filename.split(" - ")[-1].split(".")[0].replace("-", " ").title()
            c.save()

            # Get the file contents as a string
            file = open("./web_app/management/lessons/" + filename)
            text = file.read()
            file.close()

            # Add tags around untagged paragraphs
            text = text.replace("<h2", "</p><h2").replace("</h2>", "</h2><p>") + "</p><h2>DUMMY</h2>"
            text = text[4 + text.index("</p>"):]
            try:
                text = unicode(text.decode('utf-8').encode('ascii', 'xmlcharrefreplace'))
            except UnicodeDecodeError:
                print text

            # Strip spans
            soup = strip_tags(text, ['span'])

            # Strip inline style
            for tag in soup():
                for attribute in ["class", "id", "name", "style"]:
                    del tag[attribute]

            # Create the lesson
            l = Lesson()
            l.save()

            # Form a section
            for pair in get_section_title_and_content(soup, 'h2', 'h2'):
                title = format(pair[0])
                content = pair[1].strip()

                # Set section title
                s = Section(title=title)
                s.save()

                if 'h3' not in content:
                    s.content = content
                    s.save()

                elif 'h3' in content:
                    subsoup = BeautifulSoup(content + "<h3>DEAD</h3>")
                    for subtitle, subcontent in get_section_title_and_content(subsoup, 'h3', 'h3'):
                        subsection = Section(title=subtitle, content=subcontent)
                        subsection.save()

                        s.subsections.add(subsection)
                        s.save()

                l.sections.add(s)
                l.save()

            c.lesson = l
            c.save()

            subject.chapters.add(c)
