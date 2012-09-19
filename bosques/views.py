from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from models import *
from forms import *

# Create your views here.
def index(request):
	bosques = PropietarioBosques.objects.all().count()

	return render_to_response ('index.html', RequestContext(request, locals()))

def _queryset_filtrado(request):
	params = {}
	if 'fecha' in  request.session:
		params['year'] = request.session['fecha']
	if 'tipo_propiedad' in request.session:
		params['tipo_propiedad'] = request.session['tipo_propiedad']
	# if 'area_total' in request.session:
	# 	params['area_total'] = request.session['area_total']
	if 'organizado' in request.session:
		params['organizado'] = request.session['organizado']
	if 'gti' in request.session:
		params['gobierno_gti'] = request.session['gti']
	if 'tipo_bosque_umf' in request.session:
		params['bosques_umf'] = request.session['tipo_bosque_umf']
	if 'tipo_certificacion' in request.session:
		params['tipo_certificacion'] = request.session['tipo_certificacion']

	unvalid_keys = []
	for key in params:
		if not params[key]:
			unvalid_keys.append(key)
    
	for key in unvalid_keys:
		del params[key]
    
	return PropietarioBosques.objects.filter(**params)

def consultar(request):    
	if request.method == 'POST':
		form = FiltroBosquesForm(request.POST)
		if form.is_valid():
			request.session['fecha'] = form.cleaned_data['fecha']            
			request.session['tipo_propiedad'] = form.cleaned_data['tipo_propiedad']
			#request.session['area_total'] = form.cleaned_data['area_total']
			request.session['organizado'] = form.cleaned_data['organizado']
			request.session['gti'] = form.cleaned_data['gti']
			request.session['tipo_bosque_umf'] = form.cleaned_data['tipo_bosque_umf']
			request.session['tipo_certificacion'] = form.cleaned_data['tipo_certificacion']
			centinel = 1
	else:
		form = FiltroBosquesForm()
		centinel = 0

	lista = []
	if centinel == 1:
		consulta = _queryset_filtrado(request)
	else:
		request.session['fecha'] = None          
		request.session['tipo_propiedad'] = None 
		#request.session['area_total'] = None 
		request.session['organizado'] = None 
		request.session['gti'] = None 
		request.session['tipo_bosque_umf'] = None
		request.session['certificacion'] = None  
		consulta = PropietarioBosques.objects.all()
	for obj in consulta:
		lista.append([obj.nombre_propietario,
			          obj.get_sexo_propietario_display(),
			          obj.area_propiedad,
			          obj.departamento,
			          obj.municipio,
			          obj.bosques_umf,
			          obj.id
			        ]) 
	return render_to_response('bosques/consultar.html', locals(),
    	                      context_instance=RequestContext(request))

def obtener_mapa(request):
    if request.is_ajax():
        lista = []
        params = _queryset_filtrado(request)
        for objeto in params.distinct():
            if objeto.latitud and objeto.longitud:
            	certificado_no=[a.nombre for a in objeto.tipo_certificacion.filter(id=1)]
            	certificado_proceso=[a.nombre for a in objeto.tipo_certificacion.filter(id=2)]
            	certificado_fsc=[a.nombre  for a in objeto.tipo_certificacion.filter(id=3)]
            	certificado_fsc_slimf=[a.nombre for a in objeto.tipo_certificacion.filter(id=4)]
            	certificado_fsc_cw=[a.nombre for a in objeto.tipo_certificacion.filter(id=5)]
            	certificado_comer_justo=[a.nombre for a in objeto.tipo_certificacion.filter(id=6)]
            	certificado_iso=[a.nombre for a in objeto.tipo_certificacion.filter(id=7)]
            	certificado_otro=[a.nombre for a in objeto.tipo_certificacion.filter(id=8)]
            	if certificado_no:
            		color=1
            	if certificado_proceso:
            		color=2
            	if certificado_fsc or certificado_fsc_slimf or certificado_fsc_cw or certificado_comer_justo or certificado_iso or certificado_otro:
                	color=3
                dicc = dict(nombre=objeto.nombre_propietario, 
                	        id=objeto.id,
                            lon=float(objeto.longitud) , 
                            lat=float(objeto.latitud),
                            propiedad=objeto.nombre_propiedad,
                            coloricon=color,
                            fsc=certificado_fsc,
                            fsc_slimf=certificado_fsc_slimf,
                            fsc_cw=certificado_fsc_cw,
                            comer_justo=certificado_comer_justo,
                            iso=certificado_iso,
                            otro=certificado_otro,
                            no=certificado_no,
                            proceso=certificado_proceso,
                            )
            lista.append(dicc)

        serializado = simplejson.dumps(lista)
    	return HttpResponse(serializado, mimetype='application/json')	

def ficha_propierario(request, id):
	datos = get_object_or_404(PropietarioBosques, id=id)

	return render_to_response('bosques/ficha.html', locals(),
							  context_instance=RequestContext(request))

def obtener_todo_mapa(request):
	if request.is_ajax():
		lista = []
        for objeto in PropietarioBosques.objects.all():
            if objeto.latitud and objeto.longitud:
            	certificado_no=[a.nombre for a in objeto.tipo_certificacion.filter(id=1)]
            	certificado_proceso=[a.nombre for a in objeto.tipo_certificacion.filter(id=2)]
            	certificado_fsc=[a.nombre  for a in objeto.tipo_certificacion.filter(id=3)]
            	certificado_fsc_slimf=[a.nombre for a in objeto.tipo_certificacion.filter(id=4)]
            	certificado_fsc_cw=[a.nombre for a in objeto.tipo_certificacion.filter(id=5)]
            	certificado_comer_justo=[a.nombre for a in objeto.tipo_certificacion.filter(id=6)]
            	certificado_iso=[a.nombre for a in objeto.tipo_certificacion.filter(id=7)]
            	certificado_otro=[a.nombre for a in objeto.tipo_certificacion.filter(id=8)]
            	if certificado_no:
            		color=1
            	if certificado_proceso:
            		color=2
            	if certificado_fsc or certificado_fsc_slimf or certificado_fsc_cw or certificado_comer_justo or certificado_iso or certificado_otro:
                	color=3
                dicc = dict(nombre=objeto.nombre_propietario, 
                	        id=objeto.id,
                            lon=float(objeto.longitud) , 
                            lat=float(objeto.latitud),
                            propiedad=objeto.nombre_propiedad,
                            coloricon=color,
                            fsc=certificado_fsc,
                            fsc_slimf=certificado_fsc_slimf,
                            fsc_cw=certificado_fsc_cw,
                            comer_justo=certificado_comer_justo,
                            iso=certificado_iso,
                            otro=certificado_otro,
                            no=certificado_no,
                            proceso=certificado_proceso,
                            )
            lista.append(dicc)

        serializado = simplejson.dumps(lista)
        return HttpResponse(serializado, mimetype='application/json')
