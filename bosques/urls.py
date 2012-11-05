from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
urlpatterns = patterns('bosques.views',
    #url(r'index/$', 'index', name="index"),
    url(r'^acerca/$',direct_to_template,{'template': 'acerca.html'}),
    # Empresa de manejo de bosque
    url(r'^consultar/$', 'consultar', name="consultar"),
    url(r'^ver/$', 'obtener_mapa', name='obtener-mapa'),
    url(r'^ficha/(?P<id>\d+)/$', 'ficha_propierario', name='ficha-propierario'),
    url(r'^ficha/seguimiento/(?P<id>\d+)/$', 'ficha_propierario_seguimiento', name='ficha-propierario-seguimiento'),
    url(r'^ver/todo/$', 'obtener_todo_mapa', name='obtener-todo-mapa'),
    url(r'^ficha/relacion/(?P<id>\d+)/$', 'ficha_propierario_relacion', name='ficha-propierario-relacion'),

    # Empresas de primera transformacion
    url(r'^primera/consultar/$', 'consultar_primera', name="consultar-primera"),
    url(r'^primera/ficha/(?P<id>\d+)/$', 'ficha_primera', name='ficha-primera'),
    url(r'^primera/ver/$', 'obtener_mapa_primera', name='obtener-mapa-primera'),
    url(r'^primera/todo/$', 'obtener_todo_mapa_primera', name='obtener-todo-mapa-primera'),
    url(r'^primera/relacion/(?P<id>\d+)/$', 'ficha_primera_relacion', name='ficha-primera-relacion'),
    url(r'^primera/seguimiento/(?P<id>\d+)/$', 'ficha_primera_seguimiento', name='ficha-primera-seguimiento'),

    # Empresas de segunda transformacion
    url(r'^segunda/consultar/$', 'consultar_segunda', name="consultar-segunda"),
    url(r'^segunda/ficha/(?P<id>\d+)/$', 'ficha_segunda', name='ficha-segunda'),
    url(r'^segunda/ver/$', 'obtener_mapa_segunda', name='obtener-mapa-segunda'),
    url(r'^segunda/todo/$', 'obtener_todo_mapa_segunda', name='obtener-todo-mapa-segunda'),
    url(r'^segunda/relacion/(?P<id>\d+)/$', 'ficha_segunda_relacion', name='ficha-segunda-relacion'),
    url(r'^segunda/seguimiento/(?P<id>\d+)/$', 'ficha_segunda_seguimiento', name='ficha-segunda-seguimiento'),

    # Regente Forestal
    url(r'^regente/consultar/$', 'consultar_regente', name="consultar-regente"),
    url(r'^regente/ficha/(?P<id>\d+)/$', 'ficha_regente', name='ficha-regente'),
    url(r'^regente/relacion/(?P<id>\d+)/$', 'ficha_regente_relacion', name='ficha-regente-relacion'),
    url(r'^regente/seguimiento/(?P<id>\d+)/$', 'ficha_regente_seguimiento', name='ficha-regente-seguimiento'),
    )