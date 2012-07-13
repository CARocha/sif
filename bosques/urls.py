from django.conf.urls.defaults import *

urlpatterns = patterns('bosques.views',
    #url(r'index/$', 'index', name="index"),
    url(r'^consultar/$', 'consultar', name="consultar"),
    url(r'^ver/$', 'obtener_mapa', name='obtener-mapa'),
    url(r'^ficha/(?P<id>\d+)/$', 'ficha_propierario', name='ficha-propierario'),
    url(r'^ver/todo/$', 'obtener_todo_mapa', name='obtener-todo-mapa'),
    )