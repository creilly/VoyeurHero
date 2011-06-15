import os
import sys
 
#path = '/home/al/Archimedes-Lever'
path = '/home/jack/VoyeurHero'
if path not in sys.path:
#    sys.path.insert(0,'/home/al/Archimedes-Lever/StartUp')
    sys.path.insert(0,'/home/jack/VoyeurHero/VoyeurHero')
    sys.path.insert(0,path)
    
 
os.environ['DJANGO_SETTINGS_MODULE'] = 'VoyeurHero.settings'
 
import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()