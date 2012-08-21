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
		params['sequimiento__propietario__year'] = request.session['fecha']
	if 'tipo_propiedad' in request.session:
		params['sequimiento__propietario__tipo_propiedad'] = request.session['tipo_propiedad']
	# if 'area_total' in request.session:
	# 	params['area_total'] = request.session['area_total']
	if 'organizado' in request.session:
		params['sequimiento__propietario__organizado'] = request.session['organizado']
	if 'gti' in request.session:
		params['sequimiento__propietario__gobierno_gti'] = request.session['gti']
	if 'tipo_bosque_umf' in request.session:
		params['sequimiento__propietario__bosques_umf'] = request.session['tipo_bosque_umf']
	if 'certificacion' in request.session:
		params['tipo_certificacion'] = request.session['certificacion']

	unvalid_keys = []
	for key in params:
		if not params[key]:
			unvalid_keys.append(key)
    
	for key in unvalid_keys:
		del params[key]
    
	return Datos.objects.filter(**params)

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
			request.session['certificacion'] = form.cleaned_data['certificacion']
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
        print params
        for objeto in params.distinct():
            if objeto.sequimiento.propietario.latitud and objeto.sequimiento.propietario.longitud:
                dicc = dict(nombre=objeto.sequimiento.propietario.nombre_propietario, 
                	        id=objeto.sequimiento.propietario.id,
                            lon=float(objeto.sequimiento.propietario.longitud) , 
                            lat=float(objeto.sequimiento.propietario.latitud),
                            propiedad=objeto.sequimiento.propietario.nombre_propiedad,
                            cert=objeto.certificado,
                            tipo=[a.nombre for a in objeto.tipo_certificacion.all()],
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
        for objeto in Datos.objects.all():
            if objeto.sequimiento.propietario.latitud and objeto.sequimiento.propietario.longitud:
                dicc = dict(nombre=objeto.sequimiento.propietario.nombre_propietario, 
                	        id=objeto.sequimiento.propietario.id,
                            lon=float(objeto.sequimiento.propietario.longitud) , 
                            lat=float(objeto.sequimiento.propietario.latitud),
                            propiedad=objeto.sequimiento.propietario.nombre_propiedad,
                            cert=objeto.certificado,
                            tipo=[a.nombre for a in objeto.tipo_certificacion.all()],
                            )
            lista.append(dicc)

        serializado = simplejson.dumps(lista)
        return HttpResponse(serializado, mimetype='application/json')
