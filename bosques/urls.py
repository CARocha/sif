from django.conf.urls.defaults import *

urlpatterns = patterns('bosques.views',
    #url(r'index/$', 'index', name="index"),
    url(r'^consultar/$', 'consultar', name="consultar"),
    url(r'^ver/$', 'obtener_mapa', name='obtener-mapa'),
    url(r'^ficha/(?P<id>\d+)/$', 'ficha_propierario', name='ficha-propierario'),
    url(r'^ver/todo/$', 'obtener_todo_mapa', name='obtener-todo-mapa'),

    # Empresas de primera transformacion
    url(r'^primera/consultar/$', 'consultar_primera', name="consultar-primera"),
    url(r'^primera/ficha/(?P<id>\d+)/$', 'ficha_primera', name='ficha-propierario'),
    url(r'^primera/ver/$', 'obtener_mapa_primera', name='obtener-mapa'),
    url(r'^primera/todo/$', 'obtener_todo_mapa_primera', name='obtener-todo-mapa'),
    )