from django.conf.urls import patterns, include, url
from django.contrib import admin


    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
urlpatterns = patterns('',
                       #url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', 'qa.views.test'),
                       url(r'^login/$', 'qa.views.test'),
                       url(r'^singup/$', 'qa.views.test'),
                       url(r'^question/[0-9]*/$', 'qa.views.test'),
                       url(r'^ask/$', 'qa.views.test'),
                       url(r'^popular/$', 'qa.views.test'),
                       url(r'^new/$', 'qa.views.test')
                       )
