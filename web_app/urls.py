from django.conf.urls import patterns, url
from web_app import views

urlpatterns = patterns('',
                       url(r'^$', views.splash, name='splash'),
                       url(r'^ap-courses/submit$', views.submit, name="submit"),
                       url(r'^(?P<course_type_slug>[-\w]+)$', views.courses_page, name='courses'),
                       url(r'^ap-courses/(?P<course_slug>[-\w]+)$', views.chapter_page, name="chapter"),
                       url(r'^ap-courses/(?P<course_slug>[-\w]+)/(?P<chapter_slug>[-\w]+)/lesson$', views.chapter, name="lesson"),
                       url(r'^ap-courses/(?P<course_slug>[-\w]+)/(?P<chapter_slug>[-\w]+)/compact-review$', views.chapter, name="review"),
                       url(r'^ap-courses/(?P<course_slug>[-\w]+)/(?P<chapter_slug>[-\w]+)/problems$', views.chapter, name="problems"),)
