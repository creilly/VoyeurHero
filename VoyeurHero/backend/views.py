# Create your views here.
from ImageOps import flip
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import Context
from models import VHCategory
from django import forms

def index(request):
    return render_to_response('backend/index.html',dict(categories=VHCategory.objects.order_by('title').all()))



class ImageViewerForm(forms.Form):
    image = forms.ImageField()


def image_viewer(request):
    '''
    form to upload an image.
    shows you the image upside-down on POST.
    does not save the image.
    '''
    if request.method != 'POST':
        # for GET, just show the empty form
        form = ImageViewerForm()
    else:
        form = ImageViewerForm(request.POST, request.FILES)
        if form.is_valid():
            uploadedImage = form.cleaned_data['image']

            # the cleaned_data of a FileField is an 
            # UploadedFile object. It's a small data container
            # with no methods and just two properties:
            filename = uploadedImage.filename
            imageData = uploadedImage.content

            #just for fun, let's use PIL to flip the image 
            # upside-down and change to PNG format.
            imageData = flip(imageData)

            # note the mimetype; we're returning the image directly.
            return HttpResponse(imageData, mimetype="image/png")

    return render_to_response('test/image_viewer.html',
                              Context(dict(form=form) ) )