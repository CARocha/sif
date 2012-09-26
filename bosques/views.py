from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.utils import simplejson
from models import *
from forms import *

# Create your views here.
def index(request):
	bosques = PropietarioBosques.objects.all().count()
	empresa_primera = EmpresaPrimeraTransformacion.objects.all().count()
	empresa_segunda = EmpresaSegundaTransformacion.objects.all().count()
	regente = RegenteForestal.objects.all().count()

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
    lista_coordenadas = datos.coordenadas_umf
    
    lista_coordenadas = lista_coordenadas[1:-1].split('&')
    punto = max(lista_coordenadas)

    return render_to_response('bosques/ficha.html', locals(),
							  context_instance=RequestContext(request))

def ficha_propierario_seguimiento(request, id):
    datos = get_object_or_404(PropietarioBosques, id=id)
    seguimiento = Datos.objects.filter(sequimiento__propietario__id=id)

    return render_to_response('bosques/ficha_seguimiento.html', locals(),
							  context_instance=RequestContext(request))

def ficha_propierario_relacion(request, id):
    datos = get_object_or_404(PropietarioBosques, id=id)
    relacion = Datos.objects.filter(sequimiento__propietario__id=id)

    return render_to_response('bosques/relacion_bosque.html', locals(),
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


#######################################################
#	Vistas para empresa de primera trasnformacion     #
#                    ficha 3                          #
#######################################################

def _queryset_filtrado_primera(request):
	params = {}
	params['org_empresarial'] = request.session['org_empresarial']
	params['gobierno_gti'] = request.session['gobierno_gti']
	params['area_trabajo'] = request.session['area_trabajo']
	params['productos_venden'] = request.session['productos_venden']
	unvalid_keys = []
	for key in params:
		if not params[key]:
			unvalid_keys.append(key)
    
	for key in unvalid_keys:
		del params[key]
    
	return EmpresaPrimeraTransformacion.objects.filter(**params)

def consultar_primera(request):    
	if request.method == 'POST':
		form = PrimeraTransformacionForm(request.POST)
		if form.is_valid():
			request.session['org_empresarial'] = form.cleaned_data['org_empresarial']
			request.session['gobierno_gti'] = form.cleaned_data['gobierno_gti']
			request.session['area_trabajo'] = form.cleaned_data['area_trabajo']
			request.session['productos_venden'] = form.cleaned_data['productos_venden']
			centinel = 1
	else:
		form = PrimeraTransformacionForm()
		centinel = 0

	lista = []
	if centinel == 1:
		consulta = _queryset_filtrado_primera(request)
	else:
		request.session['org_empresarial'] = None
		request.session['gobierno_gti'] = None
		request.session['area_trabajo'] = None
		request.session['productos_venden'] = None
		consulta = EmpresaPrimeraTransformacion.objects.all()
	for obj in consulta:
		lista.append([obj.nombre_empresa_forestal,
			          obj.departamento,
			          obj.municipio,
			          obj.org_empresarial,
			          obj.id,
			        ]) 
	return render_to_response('primera_transformacion/consultar_primera.html', locals(),
    	                      context_instance=RequestContext(request))

def obtener_mapa_primera(request):
    if request.is_ajax():
        lista = []
        params = _queryset_filtrado_primera(request)
        for objeto in params.distinct():
            if objeto.latitud and objeto.longitud:
                dicc = dict(nombre=objeto.nombre_empresa_forestal, 
                	        id=objeto.id,
                            lon=float(objeto.longitud) , 
                            lat=float(objeto.latitud),
                            director=objeto.nombre_director,
                            )
            lista.append(dicc)

        serializado = simplejson.dumps(lista)
    	return HttpResponse(serializado, mimetype='application/json')	

def ficha_primera(request, id):
	datos = get_object_or_404(EmpresaPrimeraTransformacion, id=id)

	return render_to_response('primera_transformacion/ficha_primera.html', locals(),
							  context_instance=RequestContext(request))

def ficha_primera_seguimiento(request, id):
    datos = get_object_or_404(EmpresaPrimeraTransformacion, id=id)
    seguimiento = DatosPrimeraTransforma.objects.filter(p_tranformacion__nombre_empresa__id=id)

    return render_to_response('primera_transformacion/primera_seguimiento.html', locals(),
							  context_instance=RequestContext(request))

def ficha_primera_relacion(request, id):
    datos = get_object_or_404(EmpresaPrimeraTransformacion, id=id)
    relacion = DatosPrimeraTransforma.objects.filter(p_tranformacion__nombre_empresa__id=id)

    return render_to_response('primera_transformacion/relacion_primera.html', locals(),
							  context_instance=RequestContext(request))

def obtener_todo_mapa_primera(request):
	if request.is_ajax():
		lista = []
        for objeto in EmpresaPrimeraTransformacion.objects.all():
            if objeto.latitud and objeto.longitud:
                dicc = dict(nombre=objeto.nombre_empresa_forestal, 
                	        id=objeto.id,
                            lon=float(objeto.longitud) , 
                            lat=float(objeto.latitud),
                            director=objeto.nombre_director,
                            )
            lista.append(dicc)

        serializado = simplejson.dumps(lista)
        return HttpResponse(serializado, mimetype='application/json')


#######################################################
#	Vistas para empresa de Segunda trasnformacion     #
#                    ficha 4                          #
#######################################################

def _queryset_filtrado_segunda(request):
	params = {}
	params['org_empresarial'] = request.session['org_empresarial']
	params['gobierno_gti'] = request.session['gobierno_gti']
	params['area_trabajo'] = request.session['area_trabajo']
	params['producto_vende'] = request.session['producto_vende']
	unvalid_keys = []
	for key in params:
		if not params[key]:
			unvalid_keys.append(key)
    
	for key in unvalid_keys:
		del params[key]
    
	return EmpresaSegundaTransformacion.objects.filter(**params)

def consultar_segunda(request):    
	if request.method == 'POST':
		form = SegundaTransformacionForm(request.POST)
		if form.is_valid():
			request.session['org_empresarial'] = form.cleaned_data['org_empresarial']
			request.session['gobierno_gti'] = form.cleaned_data['gobierno_gti']
			request.session['area_trabajo'] = form.cleaned_data['area_trabajo']
			request.session['producto_vende'] = form.cleaned_data['producto_vende']
			centinel = 1
	else:
		form = SegundaTransformacionForm()
		centinel = 0

	lista = []
	if centinel == 1:
		consulta = _queryset_filtrado_segunda(request)
	else:
		request.session['org_empresarial'] = None
		request.session['gobierno_gti'] = None
		request.session['area_trabajo'] = None
		request.session['producto_vende'] = None
		consulta = EmpresaSegundaTransformacion.objects.all()
	for obj in consulta:
		lista.append([obj.nombre_comercial,
			          obj.departamento,
			          obj.municipio,
			          obj.org_empresarial,
			          obj.id,
			        ]) 
	return render_to_response('segunda_transformacion/consultar_segunda.html', locals(),
    	                      context_instance=RequestContext(request))

def obtener_mapa_segunda(request):
    if request.is_ajax():
        lista = []
        params = _queryset_filtrado_segunda(request)
        for objeto in params.distinct():
            if objeto.latitud and objeto.longitud:
                dicc = dict(nombre=objeto.nombre_comercial, 
                	        id=objeto.id,
                            lon=float(objeto.longitud) , 
                            lat=float(objeto.latitud),
                            director=objeto.nombre_director,
                            )
            lista.append(dicc)

        serializado = simplejson.dumps(lista)
    	return HttpResponse(serializado, mimetype='application/json')	

def ficha_segunda(request, id):
	datos = get_object_or_404(EmpresaSegundaTransformacion, id=id)

	return render_to_response('segunda_transformacion/ficha_segunda.html', locals(),
							  context_instance=RequestContext(request))

def obtener_todo_mapa_segunda(request):
	if request.is_ajax():
		lista = []
        for objeto in EmpresaSegundaTransformacion.objects.all():
            if objeto.latitud and objeto.longitud:
                dicc = dict(nombre=objeto.nombre_comercial, 
                	        id=objeto.id,
                            lon=float(objeto.longitud) , 
                            lat=float(objeto.latitud),
                            director=objeto.nombre_director,
                            )
            lista.append(dicc)

        serializado = simplejson.dumps(lista)
        return HttpResponse(serializado, mimetype='application/json')

#######################################################
#	Vistas para Regente forestal                      #
#                    ficha 11                         #
#######################################################

def _queryset_filtrado_regente(request):
	params = {}
	params['organizado'] = request.session['organizado']
	unvalid_keys = []
	for key in params:
		if not params[key]:
			unvalid_keys.append(key)
    
	for key in unvalid_keys:
		del params[key]
    
	return RegenteForestal.objects.filter(**params)

def consultar_regente(request):    
	if request.method == 'POST':
		form = RegenteForestalForm(request.POST)
		if form.is_valid():
			request.session['organizado'] = form.cleaned_data['organizado']
			request.session['area_trabajo'] = form.cleaned_data['area_trabajo']
			centinel = 1
	else:
		form = RegenteForestalForm()
		centinel = 0

	lista = []
	if centinel == 1:
		consulta = _queryset_filtrado_regente(request)
	else:
		request.session['organizado'] = None
		request.session['area_trabajo'] = None
		consulta = RegenteForestal.objects.all()
	for obj in consulta:
		lista.append([obj.nombre_regente,
			          obj.departamento,
			          obj.municipio,
			          obj.area_trabajo,
			          obj.id,
			        ]) 
	return render_to_response('regente_forestal/consultar_regente.html', locals(),
    	                      context_instance=RequestContext(request))
	

def ficha_regente(request, id):
	datos = get_object_or_404(RegenteForestal, id=id)

	return render_to_response('regente_forestal/ficha_regente.html', locals(),
							  context_instance=RequestContext(request))






