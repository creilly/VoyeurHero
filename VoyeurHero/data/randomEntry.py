from backend.models import *
from pickle import load
from random import choice
from os.path import dirname
import random
books = load(open(dirname(__file__) + '/bookpickle.pck','r'))
quotes = load(open(dirname(__file__) + '/quotepickle.pck','r'))


def classicStart():
    saveN(500,randomPost)
    saveN(30,randomCategory)

class Storer:
    
    cats = VHCategory.objects.all()
    posts = VHPost.objects.all()

    ncats = len(cats)
    nposts = len(posts)


    @classmethod
    def updateCats(cls):
        cls.cats = VHCategory.objects.all()
        cls.ncats = len(cls.cats)

    @classmethod
    def updatePosts(cls):
        cls.posts = VHPost.objects.all()
        cls.nposts = len(cls.posts)





def randomPost():
    title = choice(books)
    caption = choice(quotes)
    return VHPost(title = title, caption = caption)


def saveN(n,fn):
    counter = 0
    while counter < n:
        try:
            fn().save()
            counter+=1
        except:
            pass


def randomCategory():
    Storer.updatePosts()
    cat =  VHCategory(title=choice(books))
    cat.save()
    cat.posts = random.sample(Storer.posts, random.randint(1,12))
    cat.save()
    return cat
    

