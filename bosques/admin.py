# -*- coding: utf-8 -*-

from django.contrib import admin
from bosques.models import *
from django.forms import CheckboxSelectMultiple
from django import forms
from bosques.forms import *
from autocomplete.widgets import *

class PropietarioBosqueAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    #     models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    # }
#    field_formfield_overrides = { 
#        'tipo_propiedad': { 'widget':CheckboxSelectMultiple}, 
#    }
#    def formfield_for_dbfield(self, db_field, **kwargs):
#        if db_field.name == 'tipo_propiedad':
#            kwargs['widget'] = CheckboxSelectMultiple
#        return super(PropietarioBosqueAdmin, self).formfield_for_dbfield(db_field, **kwargs) 
    form = PropietarioBosquesForm
    filter_horizontal = ('organizacion','naturales','introducida')
    fieldsets = (
        (None, {
            'fields': ('fecha', ('encuestador', 'empresa'))
        }),
        ('Datos generales del bosque', {
            'classes': ('pruebabosque',),
            'fields': ('nombre_propietario', ('sexo_propietario', 'cedula_propietario','propietario_ruc'),
            	       'representante_tecnico', ('sexo_tecnico','cedula_tecnico','tecnico_ruc'),'nombre_propiedad',
            	       'registro_catastral','tipo_propiedad','area_propiedad',('tel_convencional','tel_celular'),
            	       ('email','web'),'direccion')
        }),
        ('Ubicación geografica', {
            'classes': ('pruebaubicacion',),
            'fields': (('latitud', 'longitud'),
            	       ('departamento','municipio','comunidad'),
            	       )
        }),
        ('', {
            'fields': ('organizado',
            	       ('organizacion','desde'),
            	       )
        }),
        ('Datos varios y GTI', {
            'classes': ('pruebagti',),
            'fields': ('gobierno_gti','nombre_gti',('naturales', 'introducida'),('madera','madera_procesada','consumo'),
            	       'producto_no_maderable','tipo_producto','procesos_industriales','secado','buenas_practicas',
            	       'proveedores')
        }),
         ('Datos de unidad de manejo', {
            'classes': ('pruebaumf',),
            'fields': (('nombre_umf','area_umf'),('codigo_umf','periodo_vigencia'),'poas_umf','bosques_umf',
            			'extraccion','secado_horno',('codigo_certificado','area_certificada')
            	       )
        }),
    )
    class Media:
        css = {
            'all': ('/files/css/admin.css',),
        }
        js = ('/files/js/adminficha1.js',)


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

#---------------- seguimiento -------------------------------

class DatosAdminInline(admin.StackedInline):
    model = Datos

    fields = ['fecha_seguimiento',('hombre','mujeres'),('uso_agricola','uso_pecuario','uso_foretal'),
             ('bosque_bajo_manejo','uso_agroforestal','otros_usos'),('poa_ejecucion','area_poa','permiso_poa'),
             ('volumen_cosecha','segui_plantaciones','registro_orfn'),('certificado','tipo_certificacion',
             'estado_certificado')]
    #filter_horizontal = ('tipo_certificacion',)
    extra = 1


class SeguimientoAdmin(AutocompleteModelAdmin):
    related_search_fields = { 

                'propietario': ('nombre_propietario',),
        }
    inlines = [DatosAdminInline]

admin.site.register(Seguimiento, SeguimientoAdmin)
admin.site.register(TipoCertificacion)

