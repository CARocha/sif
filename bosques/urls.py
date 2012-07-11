from django.conf.urls.defaults import *

urlpatterns = patterns('bosques.views',
    #url(r'index/$', 'index', name="index"),
    url(r'^consultar/$', 'consultar', name="consultar"),
    url(r'^indicadores/$', 'indicadores', name="indicadores"),
    url(r'^ver/$', 'obtener_mapa', name='obtener-mapa'),
    url(r'^lista/$', 'obtener_lista', name='obtener-lista'),
    url(r'^ficha/(?P<id>\d+)/$', 'ficha_propierario', name='ficha-propierario'),

    )