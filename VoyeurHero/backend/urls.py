'''
Created on Jun 14, 2011

@author: jackdreilly
'''
from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('backend.views',
                       url(r'^$', 'index'),                                                                                                                          
                       url(r'^picview$', 'image_viewer'),
                       url(r'^search$', 'search'),                                                                                                                 
                       url(r'^autocomplete$', 'autocomplete'),                                                                                                                 
)





