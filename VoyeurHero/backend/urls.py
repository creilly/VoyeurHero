'''
Created on Jun 14, 2011

@author: jackdreilly
'''
from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns( 'backend.views',
                       url( r'^$', 'index' ),
                       url( r'^picview$', 'image_viewer' ),
                       url( r'^contact$', 'contact' ),
                       url( r'^search$', 'search' ),
                       url( r'^autocomplete$', 'autocomplete' ),
                       url( r'^newpost', 'createPost' ),
                       url( r'^category/(?P<category_id>\d+)/$', 'categoryPage', name = "category_page" ),
                       url( r'^top_posts', 'topPosts', name = 'top_posts' ),
 )




