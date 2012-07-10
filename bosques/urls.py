from django.conf.urls.defaults import *

urlpatterns = patterns('bosques.views',
    #url(r'index/$', 'index', name="index"),
    url(r'^consultar/$', 'consultar', name="consultar"),
    url(r'^indicadores/$', 'indicadores', name="indicadores"),
    url(r'^ver/$', 'obtener_mapa', name='obtener-mapa'),
   
    )