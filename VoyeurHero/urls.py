from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.conf.urls.defaults import *
from voting.views import xmlhttprequest_vote_on_object
from backend.models import VHPost

vhpost_dict = {
    'model': VHPost,
}

urlpatterns = patterns('',
    # Examples:
    (r'^post_vote/(?P<object_id>\d+)/(?P<direction>up|down|clear)vote/?$', xmlhttprequest_vote_on_object, vhpost_dict),
    (r'^accounts/', include('registration.urls')),
    (r'^profiles/', include('profiles.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^search/', include('haystack.urls')),
    url(r'^loggedin/', 'backend.views.loggedIn',name='logged in page'),
    url(r'^backend/', include('backend.urls')),
    url(r'^$', 'backend.views.index', name='index'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
