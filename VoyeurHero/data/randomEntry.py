from backend.models import *
from pickle import load
from random import choice
from os.path import dirname
from django.contrib.auth.models import *
import random
books = load(open(dirname(__file__) + '/bookpickle.pck','r'))
quotes = load(open(dirname(__file__) + '/quotepickle.pck','r'))
adjs = load(open(dirname(__file__) + '/adjectivepickle.pck','r'))

adminuser = User.objects.get(id=1)

def classicStart():
    saveN(1000, randomTag)
    print 'tags done'
    Storer.updateTags()
    print 'update done'
    saveN(10,randomPost)
    Storer.updatePosts()
    saveN(10,randomCategory)


def randomTag():
    return VHTag(name=choice(adjs))

class Storer:    
    cats = VHCategory.objects.all()
    posts = VHPost.objects.all()
    tags = VHTag.objects.all()

    ncats = len(cats)
    nposts = len(posts)
    ntags = len(tags)

    @classmethod
    def updateCats(cls):
        cls.cats = VHCategory.objects.all()
        cls.ncats = len(cls.cats)

    @classmethod
    def updatePosts(cls):
        cls.posts = VHPost.objects.all()
        cls.nposts = len(cls.posts)

    @classmethod
    def updateTags(cls):
        cls.tags = VHTag.objects.all()
        cls.ntags = len(cls.tags)


def randomPost():
    title = choice(books)
    print 'get title'
    caption = choice(quotes)
    print 'get caption'
    post =  VHPost(title = title, caption = caption)
    print 'get post'
    post.user = adminuser
    post.save()
    post.tags = random.sample(Storer.tags,random.randint(1,5))
    post.save()
    print 'post saved'
    return post


def saveN(n,fn):
    counter = 0
    while counter < n:
        try:
            fn().save()
            counter+=1
        except:
            pass


def randomCategory():
    cat =  VHCategory(title=choice(books))
    cat.save()
    cat.posts = random.sample(Storer.posts, random.randint(1,12))
    cat.save()
    cat.tags = random.sample(Storer.tags,random.randint(1,5))
    cat.save()
    return cat
    

