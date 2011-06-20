'''
Created on Jun 19, 2011

@author: jackdreilly
'''
from VoyeurHero.backend.models import VHCategory, VHTag, VHPost, VHProfile
from django.contrib import admin


admin.site.register(VHPost)
admin.site.register(VHCategory)
admin.site.register(VHTag)
admin.site.register(VHProfile)

