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
    filter_horizontal = ('organizacion','naturales','tipo_certificacion',)
    date_hierarchy = 'fecha'
    search_fields = ['nombre_propietario']
    fieldsets = (
        (None, {
            'fields': ('fecha', ('encuestador', 'empresa'))
        }),
        ('Datos generales del bosque', {
            'classes': ('pruebabosque',),
            'fields': ('nombre_propietario', ('sexo_propietario', 'cedula_propietario'),
                       'representante_tecnico', ('sexo_tecnico','cedula_tecnico','tecnico_ruc'),'nombre_propiedad',
                       'tipo_propiedad','area_propiedad',('tel_convencional','tel_celular'),
                       ('email','web'),'direccion')
        }),
        ('Ubicación geográfica (coordenadas de punto de referencia) de la propiedad', {
            'classes': ('pruebaubicacion',),
            'fields': (('latitud', 'longitud'),
            	       ('departamento','municipio','comunidad'),
            	       'gobierno_gti','nombre_gti',
                       )
        }),
        ('Datos de unidad de manejo (UMF)', {
            'classes': ('pruebaumf',),
            'fields': (('coordenadas_umf','nombre_umf','area_umf'),
                       ('codigo_umf','periodo_vigencia'),'poas_umf',
                        ('codigo_certificado','area_certificada'),'bosques_umf'
                       )
        }),
        ('', {
            'fields': ('organizado',
                       ('organizacion','desde'),
                       )
        }),
        ('Datos varios', {
            'classes': ('pruebagti',),
            'fields': (('naturales',),('madera','madera_procesada','consumo'),'extraccion',
            	       'producto_no_maderable','tipo_producto','procesos_industriales',
                       'buenas_practicas','otro_social', 'otro_ambiental','tipo_certificacion'
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
admin.site.register(ProVendenBosque)
admin.site.register(PropietarioBosques, PropietarioBosqueAdmin)

#---------------- seguimiento -------------------------------

class DatosAdminInline(admin.StackedInline):
    model = Datos
    #filter_horizontal = ('tipo_certificacion',)

    fieldsets = (
        (None, {
            'fields': ('fecha_seguimiento',)
        }),
        ('Número de empleados en la UMF (colocar cantidades)', {
            'classes': ('datoseguimiento',),
            'fields': (('hombre', 'mujeres',),)
        }),
        ('Uso de la tierra (cantidades)', {
            'classes': ('datoseguimiento',),
            'fields': (('uso_agricola','uso_pecuario','uso_foretal'),
                        ('bosque_bajo_manejo','uso_agroforestal','otros_usos'),)
        }),
        ('Datos de la unidad de manejo', {
            'classes': ('datoseguimiento',),
            'fields': (('poa_ejecucion','area_poa','permiso_poa'),
                       ('volumen_cosecha','segui_plantaciones','registro_orfn'),
                       ('visita_auditoria','auditor'),
                       ('tipo_certificacion',),
                       ('estado_certificado','entidad_certificadora')
                       )
        }),
        ('Relaciones con actores', {
            'classes': ('actoresRela',),
            'fields': (('primera_transformacion','producto_venden'),
                       ('primera_transformacion2','producto_venden2'),
                       ('primera_transformacion3','producto_venden3'), 'regente'
                     )
        }),
    )

    extra = 1

    class Media:
        css = {
            'all': ('/files/css/admin.css',),
        }


class SeguimientoAdmin(AutocompleteModelAdmin):
    search_fields = ['__unicode__']
    related_search_fields = {

                'propietario': ('nombre_propietario',),
        }
    inlines = [DatosAdminInline]

admin.site.register(Seguimiento, SeguimientoAdmin)
admin.site.register(TipoCertificacion)
admin.site.register(Auditor)
admin.site.register(EntidadCertificadora)
admin.site.register(SocialesEconomico)
admin.site.register(Ambientales)

#------------------------  Regente foresal  -------------------------------

class RegenteAdmin(admin.ModelAdmin):
    form = RegenteForm
    filter_horizontal = ('organizado','organizacion','area_trabajo')
    date_hierarchy = 'llenado'
    search_fields = ['nombre_regente']

    fieldsets = (
        (None, {
            'fields': ('llenado', ('encuestador'))
        }),
        ('Datos generales regente forestal', {
            'classes': ('pruebabosque',),
            'fields': ('nombre_regente', ('codigo_regente','no_cedula'),
                       'org_publica', ('tel_convencional','tel_celular'),('correo','pagina_web'),
                       'direccion', ('departamento','municipio','comunidad'),
                       ('fecha_acreditacion', 'experiencia'), 'organizado','organizacion','desde',
                       'area_trabajo','perfil')
        }),

    )

admin.site.register(RegenteForestal, RegenteAdmin)
admin.site.register(OrganizacionPublica)
admin.site.register(AreaTrabajo)

#------------------------ admin seguimiento regente -------------------------------

class SeguimientoRegenteAdminInline(admin.StackedInline):
    model = DatosSeguimientoRegente
    fieldsets = (
        (None, {
            'fields': ('fecha_seguimiento',)
        }),
        ('Datos de seguimiento para monitoreo', {
            'fields': (('hombre', 'mujeres',),('no_pgmf_regencia','area_pgmf'),
                       ('codigo_pgmf','fecha_ingreso'),('no_poa_regencia','area_total_poa'),
                       ('codigo_poa','volumenes_totales'))
        }),
    )
    extra = 1

class RegenteSeguimientoAdmin(AutocompleteModelAdmin):
    search_fields = ['__unicode__']
    related_search_fields = {

                'regente': ('nombre_regente',),
        }
    inlines = [SeguimientoRegenteAdminInline]

admin.site.register(SeguimientoRegente, RegenteSeguimientoAdmin)

#---------------------------admin primera tranformacion --------------------------------
class PrimeraTransformacionAdmin(admin.ModelAdmin):
    form = PrimeraTForm
    #filter_horizontal = ('organizado','organizacion','area_trabajo')
    date_hierarchy = 'fecha_llenado'
    search_fields = ['nombre_empresa_forestal']
    fieldsets = (
        (None, {
            'fields': ('fecha_llenado', ('encuestador','empresa'))
        }),
        ('Datos generales de primera transformación', {
            'classes': ('pruebabosque',),
            'fields': ('nombre_empresa_forestal', ('nombre_corto','fecha_creacion'),
                       'org_empresarial', ('nombre_director','cedula'),'alianza',
                       ('organizado','desde'),('tel_convencional','tel_celular'),
                       ('correo','pagina_web'),'direccion',
                       ('departamento','municipio','comunidad'),
                       ('latitud', 'longitud'), 'gobierno_gti','nombre_gti',
                       'area_trabajo','servicio_secado','capasidad_horno',
                       'productos_venden','otro_social','otro_ambiental')
        }),

    )

admin.site.register(OrganizacionEmpresarial)
admin.site.register(AlianzaNegocio)
admin.site.register(TrabajoTranformacion)
admin.site.register(ServicioSecado)
admin.site.register(ProductosVenden)
admin.site.register(EmpresaPrimeraTransformacion,PrimeraTransformacionAdmin)

#-------------------------- Seguimiento primera transformacion ---------------------

class DatosPrimeroTransformacionInline(admin.StackedInline):
    model = DatosPrimeraTransforma
    fieldsets = (
        (None, {
            'fields': ('fecha',)
        }),
        ('Datos de seguimiento para primera transformación', {
            'fields': (('hombres', 'mujeres',),'tipo_certificacion','codigo_certificacion',
                       ('estado_certificado','entidad_certificadora'),
                       ('status','regente'),('asistencia','servicio_extraccion'),
                       ('empresa','relacion'),('producto_vende','desde'),
                       ('volumen_madera_rollo','volumen_madera_aserrada'),
                       ('volumen_carbon','volumen_lena'))
        }),
    )
    extra = 1

class SeguimientoPrimeraTransformacionAdmin(AutocompleteModelAdmin):
    search_fields = ['__unicode__']
    related_search_fields = {

                'nombre_empresa': ('nombre_empresa_forestal',),
        }
    inlines = [DatosPrimeroTransformacionInline]

admin.site.register(AsistenciaTecnica)
admin.site.register(ServicioExtraccion)
admin.site.register(EmpresaComercializadora)
admin.site.register(RelacionComercial)
admin.site.register(ProductoVenden)
admin.site.register(SeguimientoPrimeraTransformacion,SeguimientoPrimeraTransformacionAdmin)

#-------------------------- Admin segunda tranformación ------------------------------

class SegundaTranformacionAdmin(admin.ModelAdmin):
    form = SegundaTForm
    #filter_horizontal = ('organizado','organizacion','area_trabajo')
    date_hierarchy = 'fecha'
    search_fields = ['nombre_comercial']
    fieldsets = (
        (None, {
            'fields': ('fecha', ('encuestador','empresa'))
        }),
        ('Datos generales de segunda transformación', {
            'classes': ('pruebabosque',),
            'fields': ('nombre_comercial', ('nombre_corto','creacion','funcionando'),
                       'org_empresarial', ('nombre_director','cedula'),
                       ('organizado','desde'),('tel_convencional','tel_celular'),
                       ('correo','pagina_web'),'direccion',
                       ('departamento','municipio','comunidad'),
                       ('latitud', 'longitud'), 'gobierno_gti','nombre_gti',
                       'area_trabajo','apoyo_produccion','madera',
                       'producto_vende','no_maderable','nivel_tecnologico',
                       'propia_secado','volumen_anual','promedio','otro_social',
                       'otro_ambiental','vision_empresarial')
        }),

    )

admin.site.register(AreaTrabajoSegunda)
admin.site.register(ApoyoProduccion)
admin.site.register(ProductosVendenSegunda)
admin.site.register(NoMaderable)
admin.site.register(NivelTecnologico)
admin.site.register(VisionEmpresarial)
admin.site.register(EmpresaSegundaTransformacion, SegundaTranformacionAdmin)
#------------------------ seguimiento segunda tranformacion ------------------------------

class DatosSegundaTransformacionInline(admin.StackedInline):
    model = DatosSegundaTranformacion
    fieldsets = (
        (None, {
            'fields': ('fecha',)
        }),
        ('Datos de seguimiento para segunda transformación', {
            'fields': (('alianza','hombres', 'mujeres',),'tipo_certificacion',
                        'codigo',
                       ('estado_certificado','entidad_certificadora'),
                       ('fecha_status','proveedores'),('servicio_operacionales'),
                       ('relacion','t_producto'),('desde_cuando','volumen_promedio')
                      )
        }),
    )
    extra = 1

class SeguimientoSegundaTransformacionAdmin(AutocompleteModelAdmin):
    search_fields = ['__unicode__']
    related_search_fields = {
                'nombre': ('nombre_comercial',),
        }
    inlines = [DatosSegundaTransformacionInline]

admin.site.register(AlianzaNegocion)
admin.site.register(PrestadoresServicioOperacionales)
admin.site.register(SeguimientoSegundaTranformacion, SeguimientoSegundaTransformacionAdmin)
admin.site.register(TipoProductoSegundaTransformacion)
