# Create your views here.
from ImageOps import flip
from VoyeurHero.backend.models import VHPost
from VoyeurHero.backend.vhforms import VHPostForm
from django import forms
from django.forms.models import ModelForm
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from django.template.context import Context, RequestContext
from django.utils.simplejson import dumps
from django.views.decorators.csrf import csrf_protect
from haystack.query import SearchQuerySet
from models import VHCategory
from random import choice, sample, randint, shuffle
from voting.models import Vote
from django.contrib.auth.decorators import login_required
from profiles.views import profile_detail

N_CATEGORIES_PULL = 1
N_CATEGORIES_SELECT = 1

def topPosts(request):
    return render_to_response('backend/top_posts.html', dict(posts =map(lambda x: x[0],list(Vote.objects.get_top(VHPost, 10)))), RequestContext(request))

def userProfile(request,username):
    return profile_detail(request,username, extra_context=dict(userPosts = VHPost.objects.filter(user=request.user)))

def categoryPage(request):
    category_id = request.GET['category_id']
    return render_to_response('backend/category_page.html',dict(category=VHCategory.objects.get(id=category_id)), RequestContext(request))

def loggedIn(request):
    if request.user.vhprofile_set.exists():
        return redirect('/profiles/%s' % request.user)
    return redirect('/profiles/create')

def createPost(request):
    return image_viewer(request)
    #return render_to_response('backend/newpost.html',dict(form = VHPostForm()),RequestContext(request))
    
def index(request):
    categories = sample(VHCategory.objects.order_by('title')[:N_CATEGORIES_PULL], N_CATEGORIES_SELECT)
    shuffle(categories)
    return render_to_response('backend/index.html',dict(categories=categories), RequestContext(request))


def search(request):
    return render_to_response('backend/search.html',dict(), RequestContext(request))

def contact(request):
    return render_to_response('backend/contact.html',dict())

def autocomplete(request):
    return HttpResponse(dumps([result.object.name for result in SearchQuerySet().autocomplete(tag_auto=request.GET['term'])]))

def post_page(request, post):
    return render_to_response('backend/post_page.html',dict(post=post),RequestContext(request))

@login_required
def image_viewer(request):
    '''
    form to upload an image.
    shows you the image upside-down on POST.
    does not save the image.
    '''
    if request.method != 'POST':
        # for GET, just show the empty form
        form = VHPostForm()
    else:
        form = VHPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            form.save_m2m()
            post.saveAndStoreCategories()
            return post_page(request, post)
    return render_to_response('test/image_viewer.html',dict(form = form), RequestContext(request) )
