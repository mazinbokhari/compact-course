from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'compact_course.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('web_app.urls')),
    url(r'^ap-courses/submit$', include('web_app.urls')),
    url(r'^(?P<course_type_slug>[-\w]+)$', include('web_app.urls')),
    url(r'^ap-courses/(?P<course_slug>[-\w]+)/(?P<chapter_slug>[-\w]+)/lesson$', include('web_app.urls')),
    url(r'^ap-courses/(?P<course_slug>[-\w]+)/(?P<chapter_slug>[-\w]+)/compact-review$', include('web_app.urls')),
    url(r'^ap-courses/(?P<course_slug>[-\w]+)/(?P<chapter_slug>[-\w]+)/problems$', include('web_app.urls')),)
