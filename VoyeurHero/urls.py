from backend.models import VHPost
from django.conf import settings
from django.conf.urls.defaults import *
from django.contrib import admin
from voting.views import xmlhttprequest_vote_on_object
from profiles import views
from VoyeurHero.backend.views import userProfile
# Uncomment the next two lines to enable the admin:
admin.autodiscover()

vhpost_dict = {
    'model': VHPost,
}

profile_patterns =  patterns('',
                       url(r'^profiles/create/$',
                           views.create_profile,
                           name='profiles_create_profile'),
                       url(r'^profiles/edit/$',
                           views.edit_profile,
                           name='profiles_edit_profile'),
                       url(r'^profiles/(?P<username>\w+)/$',
                           userProfile,
                           name='profiles_profile_detail'),
                       url(r'^profiles/$',
                           views.profile_list,
                           name='profiles_profile_list'),
                       )

urlpatterns = patterns('',
    # Examples:
    (r'^post_vote/(?P<object_id>\d+)/(?P<direction>up|down|clear)vote/?$', xmlhttprequest_vote_on_object, vhpost_dict),
    (r'^accounts/', include('registration.urls')),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='auth_logout'),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^search/', include('haystack.urls')),
    url(r'^loggedin/', 'backend.views.loggedIn',name='logged in page'),
    url(r'^backend/', include('backend.urls',namespace='backend',app_name='backend')),
    url(r'^$', 'backend.views.index', name='index'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += profile_patterns


if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
