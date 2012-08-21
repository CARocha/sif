# -*- coding: utf-8 -*-

from django.db import models
from lugar.models import *
import datetime
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

class Encuestador(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Nombres de encuestadores"
        
class Empresa(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Nombres de empresas"
        
SEXO_CHOICE = (
    (1, 'Masculino'),
    (2, 'Femenino')
)

SINO_CHOICE = (
    (1, 'Si'),
    (2, 'No')
)

class TipoPropiedadBosque(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Tipo de propiedad del bosque"
        
class Organizado(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Organizado"

class Organizacion(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Organizacion"
        
class GobiernoGti(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Gobiernos territoriales indigenas"

class EspeciesNaturales(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Especies forestales naturales"

class EspeciesIntroducidas(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Especies plantaciones introducidas"
        
class Madera(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Madera"

MADERA_PROCESADAS_CHOICE = (
    (1, 'Con moto sierras'),
    (2, 'Aserradero')
)

CONSUMO_CHOICE = (
    (1, 'Nacional'),
    (2, 'Exportacion'),
    (3, 'Ambos')
)

class TipoProducto(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Tipo de productos"
        
class ProcesoIndustrialBosque(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Otros procesos industriales integrados al bosque"
        
class TipoSecados(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Tipos de secados"

class BuenasPracticas(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Buenas prácticas que implementan"

class ProveedoresSuministros(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Principales proveedores de suministros y materiales"
        
class TipoBosqueUmf(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Tipo de Bosque de la UMF"
        
class MetodoExtraccion(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Método de extracción de la madera"
        
#--------------- Ficha principal -----------------------------------------------                
class PropietarioBosques(models.Model):
    fecha = models.DateField()
    encuestador = models.ForeignKey(Encuestador)
    empresa = models.ForeignKey(Empresa)
    nombre_propietario = models.CharField('Nombre del propietario', 
                                           max_length=200, 
                                           help_text='Nombre del propietario o representante legal')
    sexo_propietario = models.IntegerField(choices=SEXO_CHOICE)
    cedula_propietario = models.CharField('Cédula', max_length=200, 
                                           help_text='Cédula del propietario ó representante legal')
    propietario_ruc = models.CharField('RUC', max_length=200, help_text='Registro RUC del propietario')
    representante_tecnico = models.CharField('Nombre del técnico', 
                                           max_length=200, 
                                           help_text='Nombre del representante técnico')
    sexo_tecnico = models.IntegerField(choices=SEXO_CHOICE)
    cedula_tecnico = models.CharField('Cédula', max_length=200, help_text='Cédula del representante técnico')
    tecnico_ruc = models.CharField('RUC', max_length=200, help_text='Registro RUC del técnico')
    nombre_propiedad = models.CharField('Nombre de la propiedad', 
                                           max_length=200, 
                                           help_text='Nombre de la propiedad')
    registro_catastral = models.CharField(max_length=200, help_text='No. registro catrastal')
    tipo_propiedad = models.ManyToManyField(TipoPropiedadBosque)
    area_propiedad = models.FloatField('Área total de la propiedad en ha', help_text='área total en ha')
    tel_convencional = models.CharField('Teléfono convencional', max_length=15, null=True, blank=True)
    tel_celular = models.CharField('Teléfono celular', max_length=15, null=True, blank=True)
    email = models.EmailField('Correo electrónico', null=True, blank=True)
    web = models.URLField('Página web', null=True, blank=True)
    direccion = models.CharField('Dirección', max_length=200, null=True, blank=True)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    
    departamento = models.ForeignKey(Departamento)
    #municipio = models.ForeignKey(Municipio)
    municipio = ChainedForeignKey(
        Municipio,
        chained_field="departamento",
        chained_model_field="departamento",
        show_all=False,
        auto_choose=True
    )
    #comunidad = models.ForeignKey(Comunidad)
    comunidad = ChainedForeignKey(
        Comunidad,
        chained_field="municipio",
        chained_model_field="municipio",
        show_all=False,
        auto_choose=True
    )
    
    organizado = models.ManyToManyField(Organizado)
    organizacion = models.ManyToManyField(Organizacion, verbose_name="Nombre organizacion", null=True, blank=True)
    desde = models.DateField('Desde cuando', null=True, blank=True)
    gobierno_gti = models.IntegerField('Gobierno territorial indigena (GTI)', choices=SINO_CHOICE)
    nombre_gti = models.ForeignKey(GobiernoGti, null=True, blank=True)
    naturales = models.ManyToManyField(EspeciesNaturales, verbose_name='Especies naturales')
    introducida = models.ManyToManyField(EspeciesIntroducidas, verbose_name='Especies introducidas')
    madera = models.ForeignKey(Madera, null=True, blank=True)
    madera_procesada = models.IntegerField(choices=MADERA_PROCESADAS_CHOICE, null=True, blank=True)
    consumo = models.IntegerField(choices=CONSUMO_CHOICE, null=True, blank=True)
    producto_no_maderable = models.IntegerField(choices=SINO_CHOICE)
    tipo_producto = models.ManyToManyField(TipoProducto, null=True, blank=True)
    procesos_industriales = models.ManyToManyField(ProcesoIndustrialBosque)
    secado = models.ManyToManyField(TipoSecados)
    buenas_practicas = models.ManyToManyField(BuenasPracticas)
    proveedores = models.ManyToManyField(ProveedoresSuministros)
    nombre_umf = models.CharField('Nombre de la UMF', max_length=200)
    area_umf = models.FloatField('Área de la UMF (ha)')
    codigo_umf = models.CharField('Código de la UMF (INAFOR)', max_length=200)
    periodo_vigencia = models.IntegerField('Periodo de vigencia (años)')
    poas_umf = models.IntegerField('POAS en la UMF')
    bosques_umf = models.ManyToManyField(TipoBosqueUmf)
    extraccion = models.ManyToManyField(MetodoExtraccion)
    secado_horno = models.FloatField('Capacidad de secado del horno')
    codigo_certificado = models.CharField(max_length=200, null=True, blank=True)
    area_certificada = models.FloatField(null=True, blank=True)

    year = models.IntegerField(editable=False)

    def clean(self):
        from django.core.exceptions import ValidationError
    # Don't allow draft entries to have a pub_date.
        if self.area_umf > self.area_propiedad:
            raise ValidationError('El area de la UMF no puede ser Mayor al Area total de la propiedad')
    
    def save(self):
        self.year = self.fecha.year
        super(PropietarioBosques, self).save()

    def __unicode__(self):
        return self.nombre_propietario

    #esto ta malo aun le falta 
    #def certificacion_actual(self):
    #     cert = Datos.objects.filter(sequimiento__propietario__pk=self.id)[:1]
    #     if cert:
    #         lista=()
    #         for c in cert[0].tipo_certificacion
    #         return lista
    #     else:
    #         return ""
    def cert(self):
        cert = Datos.objects.filter(sequimiento__propietario__pk=self.id).order_by('-fecha_seguimiento')[:1]
        if cert:
            return cert[0].certificado
        else:
            return ""

    class Meta:
        verbose_name_plural = "Ficha 1 Dueños de bosques"
        unique_together = ('nombre_propietario',)


#--------------------- modelo de seguimiento -----------------------------------

class Seguimiento(models.Model):
    propietario = models.ForeignKey(PropietarioBosques)
    
    def __unicode__(self):
        return self.propietario.nombre_propietario
        
    class Meta:
        verbose_name_plural = "Datos para seguimiento"
        unique_together = ('propietario',)

CERTIFICADO_CHOICE = (
    (1, 'Si'),
    (2, 'No'),
    (3, 'En proceso')
)

class TipoCertificacion(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Tipos de certificación"


ESTADO_CERTIFICADO_CHOICE = (
    (1, 'Vigente'),
    (2, 'Suspendido'),
    (3, 'Renovado'),
    (4, 'Cancelado')
)
                
class Datos(models.Model):
    fecha_seguimiento = models.DateField()
    hombre = models.IntegerField('Número de hombres')
    mujeres = models.IntegerField('Número de mujeres')
    uso_agricola = models.FloatField('Uso agrícola (ha)')
    uso_pecuario = models.FloatField('Uso pecuario (ha)')
    uso_foretal = models.FloatField('Uso forestal total (ha)')
    bosque_bajo_manejo = models.FloatField('Bosques bajo manejo (ha)')
    uso_agroforestal = models.FloatField('Uso agroforestal (ha)')
    otros_usos = models.FloatField('Otros usos (ha)')
    poa_ejecucion = models.CharField('No. POA en ejecución', max_length=200)
    area_poa = models.FloatField('Área del POA (ha)')
    permiso_poa = models.CharField('No. de permiso del POA', max_length=200)
    volumen_cosecha = models.FloatField('Volumen total disponible por cosecha anual (m3)')
    segui_plantaciones = models.FloatField('Plantaciones (ha)')
    registro_orfn = models.CharField('Registro ORFN', max_length=200)
    certificado = models.IntegerField(choices=CERTIFICADO_CHOICE)
    tipo_certificacion = models.ManyToManyField(TipoCertificacion, 
                        verbose_name="Tipo de certificacion")
    estado_certificado = models.IntegerField(choices=ESTADO_CERTIFICADO_CHOICE)
    
    sequimiento = models.ForeignKey(Seguimiento)
        
    class Meta:
        verbose_name_plural = "Datos para el seguimiento de monitoreo"

