from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$',
        'qa.views.base_pagin'),
    url(r'^popular\/$',
        'qa.views.base_popular'),
    url(r'^question\/(?P<slug>\d+)\/$',
        'qa.views.post_details')
)
