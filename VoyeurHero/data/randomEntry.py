from backend.models import *
from pickle import load
from random import choice
from os.path import dirname
import random
books = load(open(dirname(__file__) + '/bookpickle.pck','r'))
quotes = load(open(dirname(__file__) + '/quotepickle.pck','r'))
adjs = load(open(dirname(__file__) + '/adjectivepickle.pck','r'))

def classicStart():
    saveN(1000, randomTag)
    Storer.updateTags()
    saveN(500,randomPost)
    Storer.updatePosts()
    saveN(30,randomCategory)


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
    caption = choice(quotes)
    post =  VHPost(title = title, caption = caption)
    post.save()
    post.tags = random.sample(Storer.tags,random.randint(1,5))
    post.save()
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
    

