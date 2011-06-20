'''
Created on Jun 19, 2011

@author: jackdreilly
'''

from django.forms import ModelForm
from VoyeurHero.backend.models import VHPost

class VHPostForm(ModelForm):
    class Meta:
        model = VHPost