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
	#if 'certificacion' in request.session:
		#params['certificacion'] = request.session['certificacion']

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
			#request.session['certificacion'] = form.cleaned_data['certificacion']
			centinel = 1
			print centinel
			return HttpResponseRedirect('/consultar/')
	else:
		form = FiltroBosquesForm()
		lista = []
		centinel = 0
		consulta = _queryset_filtrado(request)
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

def indicadores(request):
	prueba = _queryset_filtrado(request).count()
	return render_to_response('bosques/indicadores.html', locals(),
    	                      context_instance=RequestContext(request))

def obtener_mapa(request):
    if request.is_ajax():
        lista = []
        params = _queryset_filtrado(request)
        for objeto in params.distinct():
            if objeto.latitud and objeto.longitud:
                dicc = dict(nombre=objeto.nombre_propietario, id=objeto.id,
                            lon=float(objeto.longitud) , lat=float(objeto.latitud),
                            propiedad=objeto.nombre_propiedad)
            lista.append(dicc)

        serializado = simplejson.dumps(lista)
    	return HttpResponse(serializado, mimetype='application/json')	

def obtener_lista(request):
	lista = []
	consulta = _queryset_filtrado(request)
	for obj in consulta:
		lista.append([obj.nombre_propietario,
			          obj.get_sexo_propietario_display(),
			          obj.area_propiedad,
			          obj.departamento,
			          obj.municipio,
			          obj.bosques_umf,
			          obj.id
			        ])
	return render_to_response('bosques/lista_actores.html', locals(),
		                      context_instance=RequestContext(request))

def ficha_propierario(request, id):
	datos = get_object_or_404(PropietarioBosques, id=id)

	return render_to_response('bosques/ficha.html', locals(),
							  context_instance=RequestContext(request))

def obtener_todo_mapa(request):
	if request.is_ajax():
		lista = []
        for objeto in PropietarioBosques.objects.all():
            if objeto.latitud and objeto.longitud:
                dicc = dict(nombre=objeto.nombre_propietario, id=objeto.id,
                            lon=float(objeto.longitud) , lat=float(objeto.latitud),
                            propiedad=objeto.nombre_propiedad)
            lista.append(dicc)

        serializado = simplejson.dumps(lista)
        return HttpResponse(serializado, mimetype='application/json')