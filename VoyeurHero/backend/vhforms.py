'''
Created on Jun 19, 2011

@author: jackdreilly
'''

from VoyeurHero.backend.models import VHPost, VHProfile
from django.forms import ModelForm

class VHPostForm(ModelForm):
    class Meta:
        model = VHPost