from django import forms
from django.contrib import admin
from django.db import models
# Create your models here.

class VHPost(models.Model):
	picture = models.ImageField(upload_to='post_images',verbose_name = 'Post Picture', null = True,blank = True,default='http://mormonsoprano.files.wordpress.com/2010/01/mystery-man.jpg')
	caption = models.CharField(max_length=10000, verbose_name = 'Caption for Picture')
	post_date = models.DateTimeField(auto_now_add=True,verbose_name = 'Posted Date')
	categories = models.ManyToManyField('VHCategory',verbose_name = 'Categories for Post',null = True, blank = True)
	title = models.CharField(max_length = 200)

	def __unicode__(self):
		return '%s: Categories - %s' % (self.title, str(self.categories.all()))
	
	class PictureUploadForm(forms.Form):
		image = forms.ImageField()
		caption = forms.CharField(max_length=100)

		def clean_image(self):
			' reject large images. '
			max_size = 10**5
			if len(self.cleaned_data['image'].content) > max_size:
			   raise forms.ValidationError(
				   'Image must be less then %d bytes.' % max_size
			   )
			else:
			   return self.cleaned_data['image']

	
class VHCategory(models.Model):
	title = models.CharField(max_length=200,verbose_name = 'Category Title')
	posts = models.ManyToManyField(VHPost,verbose_name = 'Posts Tagged With Category', null = True, blank = True)
	
	def __unicode__(self):
		return '%s: %i posts' % (self.title, len(self.posts.all()))
	
admin.site.register(VHPost)
admin.site.register(VHCategory)
