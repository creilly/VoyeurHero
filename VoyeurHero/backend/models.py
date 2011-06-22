from django import forms
from django.contrib import admin
from django.db import models
from django.contrib.auth.models import User
from voting.managers import VoteManager

class VHProfile(models.Model):
	 # This is the only required field
	 user = models.ForeignKey(User, unique=True)

	 lucky_number = models.IntegerField()

# Create your models here.

class VHTag(models.Model):
	name = models.CharField(max_length=50,verbose_name='Tag Name')
	def __unicode__(self):
		return self.name

class VHPost(models.Model):
<<<<<<< HEAD
	user = User()
	picture = models.ImageField(upload_to='post_images',verbose_name = 'Post Picture', null = True,blank = True,default='post_images/mystery-man.jpg')
=======
	user = models.ForeignKey(User, editable=False, blank=False, null=False)
	picture = models.ImageField(verbose_name = 'Post Picture', null = True,blank = True,default='post_images/mystery-man.jpg',upload_to = 'voyeurshots/%Y/%m/%d')
>>>>>>> 1801d3e6abcd20be130330e4f2bc0fb83e56c6f7
	caption = models.CharField(max_length=10000, verbose_name = 'Caption for Picture')
	post_date = models.DateTimeField(auto_now_add=True,verbose_name = 'Posted Date')
	categories = models.ManyToManyField('VHCategory',verbose_name = 'Categories for Post',null = True, blank = True)
	tags = models.ManyToManyField('VHTag',verbose_name= 'Related Tags',null=True,blank=True)
	title = models.CharField(max_length = 200)
	
	
	def saveAndStoreCategories(self):
		self.save()
		for category in self.categories.all():
			category.posts.add(self)
			category.save()
		return self
		
		

	def __unicode__(self):
		return '%s: Categories - %s' % (self.title, ','.join(cat.title for cat in self.categories.all()))
	
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
	posts = models.ManyToManyField('VHPost',verbose_name = 'Posts Tagged With Category', null = True, blank = True)
	tags = models.ManyToManyField('VHTag',verbose_name= 'Related Tags',null=True,blank=True)
	def __unicode__(self):
		return '%s: %i posts, %i tags' % (self.title, len(self.posts.all()), len(self.tags.all()))

