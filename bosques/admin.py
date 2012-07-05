# -*- coding: utf-8 -*-

from django.contrib import admin
from bosques.models import *
from django.forms import CheckboxSelectMultiple


class PropietarioBosqueAdmin(admin.ModelAdmin):
	#fields = ['fecha', ('encuestador', 'empresa')]
	formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }

	fieldsets = (
        (None, {
            'fields': ('fecha', ('encuestador', 'empresa'))
        }),
        ('Parte 1', {
            'classes': ('prueba',),
            'fields': ('nombre_propietario', ('sexo_propietario', 'cedula_propietario','propietario_ruc'),
            	       'representante_tecnico', ('sexo_tecnico','cedula_tecnico','tecnico_ruc'),'nombre_propiedad',
            	       'registro_catastral','tipo_propiedad','area_propiedad',('tel_convencional','tel_celular'),
            	       ('email','web'),'direccion')
        }),
        ('', {
            'fields': (('latitud', 'longitud'),
            	       ('departamento','municipio','comunidad'),
            	       )
        }),
        ('', {
            'fields': ('organizado',
            	       ('organizacion','desde'),
            	       )
        }),
        ('Parte 2', {
            'classes': ('prueba2',),
            'fields': ('gobierno_gti','nombre_gti','naturales', 'introducida',('madera','madera_procesada','consumo'),
            	       'producto_no_maderable','tipo_producto','procesos_industriales','secado','buenas_practicas',
            	       'proveedores')
        }),
         ('', {
            'fields': (('nombre_umf','area_umf'),('codigo_umf','periodo_vigencia'),'poas_umf','bosques_umf',
            			'extraccion','secado_horno',('codigo_certificado','area_certificada')
            	       )
        }),
    )
	class Media:
		css = {
            'screen': ('/files/css/admin.css', ),
        }


admin.site.register(Encuestador)
admin.site.register(Empresa)
admin.site.register(TipoPropiedadBosque)
admin.site.register(Organizado)
admin.site.register(Organizacion)
admin.site.register(GobiernoGti)
admin.site.register(EspeciesNaturales)
admin.site.register(EspeciesIntroducidas)
admin.site.register(TipoProducto)
admin.site.register(ProcesoIndustrialBosque)
admin.site.register(TipoSecados)
admin.site.register(BuenasPracticas)
admin.site.register(ProveedoresSuministros)
admin.site.register(TipoBosqueUmf)
admin.site.register(MetodoExtraccion)
admin.site.register(Madera)
admin.site.register(PropietarioBosques, PropietarioBosqueAdmin)