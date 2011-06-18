from haystack import indexes
from models import *

    
class VHCategoryIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    # We add this for autocomplete.
    category_auto = indexes.EdgeNgramField(model_attr='title')
    
    def get_model(self):
        return VHCategory
        
class VHPostIndex(indexes.SearchIndex):
    text = indexes.CharField(document=True, use_template=True)
    post_date = indexes.DateTimeField(model_attr='post_date')
    caption = indexes.CharField(model_attr='caption')
    # We add this for autocomplete.
    post_auto = indexes.EdgeNgramField(model_attr='caption')
    
    def get_model(self):
        return VHPost
