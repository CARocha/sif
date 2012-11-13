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
        verbose_name_plural = "Organización"
        
class GobiernoGti(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Gobiernos territoriales indígenas"

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
        verbose_name_plural = "Especies de plantaciones introducidas"
        
class Madera(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Madera"

MADERA_PROCESADAS_CHOICE = (
    (1, 'Con moto sierra'),
    (2, 'Aserradero')
)

CONSUMO_CHOICE = (
    (1, 'Nacional'),
    (2, 'Exportación'),
    (3, 'Ambos')
)

class TipoProducto(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Tipo de producto"
        
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
        verbose_name_plural = "Tipos de secado"

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

class TipoCertificacion(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Tipos de certificación"

class SocialesEconomico(models.Model):
    nombre = models.CharField('Nombre', max_length=200)
    class Meta:
        verbose_name = ('Sociales y económicos')
        verbose_name_plural = ('Sociales y económicos')

    def __unicode__(self):
        return self.nombre

class Ambientales(models.Model):
    nombre = models.CharField(max_length=200)
    class Meta:
        verbose_name = ('Ambientales')
        verbose_name_plural = ('Ambientales')

    def __unicode__(self):
        return self.nombre

class ProVendenBosque(models.Model):
    nombre = models.CharField(max_length=200)
    class Meta:
        verbose_name = ('Tipo de producto que venden en manejo de bosque')
        verbose_name_plural = ('Tipo de producto que venden en manejo de bosque')

    def __unicode__(self):
        return self.nombre
    
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
    #propietario_ruc = models.CharField('RUC', max_length=200, help_text='Registro RUC del propietario') #se va
    representante_tecnico = models.CharField('Nombre del técnico', 
                                           max_length=200, 
                                           help_text='Nombre del representante técnico')
    sexo_tecnico = models.IntegerField(choices=SEXO_CHOICE)
    cedula_tecnico = models.CharField('Cédula', max_length=200, help_text='Cédula del representante técnico')
    tecnico_ruc = models.CharField('RUC', max_length=200, help_text='Registro RUC del técnico')
    nombre_propiedad = models.CharField('Nombre de la propiedad', 
                                           max_length=200, 
                                           help_text='Nombre de la propiedad')
    #registro_catastral = models.CharField(max_length=200, help_text='No. registro catrastal') #se va
    tipo_propiedad = models.ManyToManyField(TipoPropiedadBosque)
    area_propiedad = models.FloatField('Área total de la propiedad en ha', help_text='Área total en ha')
    tel_convencional = models.CharField('Teléfono convencional', max_length=15, null=True, blank=True)
    tel_celular = models.CharField('Teléfono celular', max_length=15, null=True, blank=True)
    email = models.EmailField('Correo electrónico', null=True, blank=True)
    web = models.URLField('Página web', null=True, blank=True)
    direccion = models.CharField('Dirección del propietario', max_length=200, null=True, blank=True)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    
    departamento = models.ForeignKey(Departamento)
    municipio = ChainedForeignKey(
        Municipio,
        chained_field="departamento",
        chained_model_field="departamento",
        show_all=False,
        auto_choose=True
    )
    comunidad = ChainedForeignKey(
        Comunidad,
        chained_field="municipio",
        chained_model_field="municipio",
        show_all=False,
        auto_choose=True
    )
    
    organizado = models.ManyToManyField(Organizado)
    organizacion = models.ManyToManyField(Organizacion, verbose_name="Nombre de organización", null=True, blank=True)
    desde = models.DateField('Desde cuando', null=True, blank=True)
    gobierno_gti = models.IntegerField('Gobierno territorial indígena (GTI)', choices=SINO_CHOICE)
    nombre_gti = models.ForeignKey(GobiernoGti, null=True, blank=True)
    naturales = models.ManyToManyField(EspeciesNaturales, verbose_name='Especies naturales')
    #introducida = models.ManyToManyField(EspeciesIntroducidas, verbose_name='Especies introducidas')
    madera = models.ForeignKey(Madera, null=True, blank=True)
    madera_procesada = models.IntegerField(choices=MADERA_PROCESADAS_CHOICE, null=True, blank=True)
    consumo = models.IntegerField(choices=CONSUMO_CHOICE, null=True, blank=True)
    producto_no_maderable = models.IntegerField(choices=SINO_CHOICE)
    tipo_producto = models.ManyToManyField(TipoProducto, null=True, blank=True)
    procesos_industriales = models.ManyToManyField(ProcesoIndustrialBosque)
    #secado = models.ManyToManyField(TipoSecados)
    buenas_practicas = models.ManyToManyField(BuenasPracticas)
    #proveedores = models.ManyToManyField(ProveedoresSuministros)
    coordenadas_umf = models.TextField(null=True, blank=True)
    nombre_umf = models.CharField('Nombre de la UMF', max_length=200)
    area_umf = models.FloatField('Área de la UMF (ha)')
    codigo_umf = models.CharField('Código de la UMF (INAFOR)', max_length=200)
    periodo_vigencia = models.IntegerField('Período de vigencia (años)')
    poas_umf = models.IntegerField('POAS en la UMF')
    bosques_umf = models.ManyToManyField(TipoBosqueUmf)
    extraccion = models.ManyToManyField(MetodoExtraccion)
    #secado_horno = models.FloatField('Capacidad de secado del horno')
    codigo_certificado = models.CharField(max_length=200, null=True, blank=True)
    area_certificada = models.FloatField(null=True, blank=True)
    otro_social = models.ManyToManyField(SocialesEconomico, null=True, blank=True)
    otro_ambiental = models.ManyToManyField(Ambientales, null=True, blank=True)
    tipo_certificacion = models.ManyToManyField(TipoCertificacion, 
                        verbose_name="Tipo de certificación")

    year = models.IntegerField(editable=False)

    def clean(self):
        from django.core.exceptions import ValidationError
    
        if self.area_umf > self.area_propiedad:
            raise ValidationError('El área de la UMF no puede ser mayor al área total de la propiedad')
    
    def save(self, *args, **kwargs):
        self.year = self.fecha.year

        super(PropietarioBosques, self).save(*args, **kwargs)
        if not Seguimiento.objects.filter(propietario=self):
            seguimiento = Seguimiento()
            seguimiento.propietario = self
            seguimiento.save()

    def __unicode__(self):
        return self.nombre_propietario

    class Meta:
        verbose_name_plural = "Empresa de manejo de bosques"
        unique_together = ('nombre_propietario',)
    
#--------------------- modelo de seguimiento de ficha 1-----------------------------------

class Seguimiento(models.Model):
    propietario = models.ForeignKey(PropietarioBosques)
    
    def __unicode__(self):
        return self.propietario.nombre_propietario
        
    class Meta:
        verbose_name_plural = "Seguimiento de manejo de bosques"
        unique_together = ('propietario',)

CERTIFICADO_CHOICE = (
    (1, 'Si'),
    (2, 'No'),
    (3, 'En proceso')
)

ESTADO_CERTIFICADO_CHOICE = (
    (1, 'Vigente'),
    (2, 'Suspendido'),
    (3, 'Renovado'),
    (4, 'Cancelado')
)

class Auditor(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Auditores"
        
class EntidadCertificadora(models.Model):
    nombre = models.CharField(max_length=200)
    
    def __unicode__(self):
        return self.nombre
        
    class Meta:
        verbose_name_plural = "Entidades certificadoras"
                
class Datos(models.Model):
    fecha_seguimiento = models.DateField('Fecha')
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
    #certificado = models.IntegerField(choices=CERTIFICADO_CHOICE)
    tipo_certificacion = models.ManyToManyField(TipoCertificacion, 
                        verbose_name="Tipo de certificación")
    estado_certificado = models.IntegerField(choices=ESTADO_CERTIFICADO_CHOICE, null=True, blank=True)
    visita_auditoria = models.DateField(null=True, blank=True)
    auditor = models.ForeignKey(Auditor, null=True, blank=True)
    entidad_certificadora = models.ForeignKey(EntidadCertificadora, null=True, blank=True)
    primera_transformacion = models.ForeignKey('EmpresaPrimeraTransformacion',
                                                related_name='EmpresaPrimeraTransformacion1',
                                                null=True, blank=True)
    producto_venden = models.ManyToManyField(ProVendenBosque, 
                                            verbose_name=u'Tipo de producto que venden 1',
                                            related_name=u'producto_venden',
                                            null=True, blank=True)
    primera_transformacion2 = models.ForeignKey('EmpresaPrimeraTransformacion',
                                                related_name='EmpresaPrimeraTransformacion2',
                                                null=True, blank=True)
    producto_venden2 = models.ManyToManyField(ProVendenBosque, 
                                            verbose_name=u'Tipo de producto que venden 2',
                                            related_name=u'producto_vende2',
                                            null=True, blank=True)
    primera_transformacion3 = models.ForeignKey('EmpresaPrimeraTransformacion',
                                                related_name='EmpresaPrimeraTransformacion3',
                                                null=True, blank=True)
    producto_venden3 = models.ManyToManyField(ProVendenBosque, 
                                            verbose_name=u'Tipo de producto que venden 3',
                                            related_name=u'producto_vende3',
                                            null=True, blank=True)
    regente = models.ForeignKey('RegenteForestal',null=True, blank=True)
    
    sequimiento = models.ForeignKey(Seguimiento)
        
    class Meta:
        verbose_name_plural = "Datos para el seguimiento del monitoreo"

#--------------------------- Regente forestal ----------------------------------

class OrganizacionPublica(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = ('OrganizacionPublica')
        verbose_name_plural = ('OrganizacionPublicas')

    def __unicode__(self):
        return self.nombre

class AreaTrabajo(models.Model):
    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name = ('Área de trabajo')
        verbose_name_plural = ('Área de trabajo')

    def __unicode__(self):
        return self.nombre

class RegenteForestal(models.Model):
    llenado = models.DateField()
    encuestador = models.ForeignKey(Encuestador)
    nombre_regente = models.CharField(max_length=200)
    codigo_regente = models.CharField(max_length=200)
    no_cedula = models.CharField(max_length=200)
    org_publica = models.ForeignKey(OrganizacionPublica)
    tel_convencional = models.CharField(max_length=50, null=True, blank=True)
    tel_celular = models.CharField(max_length=50, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    pagina_web = models.URLField(null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    departamento = models.ForeignKey(Departamento)
    municipio = ChainedForeignKey(
        Municipio,
        chained_field="departamento",
        chained_model_field="departamento",
        show_all=False,
        auto_choose=True
    )
    comunidad = ChainedForeignKey(
        Comunidad,
        chained_field="municipio",
        chained_model_field="municipio",
        show_all=False,
        auto_choose=True
    )
    fecha_acreditacion = models.DateField()
    experiencia = models.IntegerField()
    organizado = models.ManyToManyField(Organizado)
    organizacion = models.ManyToManyField(Organizacion, verbose_name="Nombre organización", null=True, blank=True)
    desde = models.DateField('Desde', null=True, blank=True)
    area_trabajo = models.ManyToManyField(AreaTrabajo)
    perfil = models.TextField()

    class Meta:
        verbose_name = ('Regente forestal')
        verbose_name_plural = ('Regentes forestales')

    def __unicode__(self):
        return self.nombre_regente

#--------------------------- seguimiento de regente --------------------------------------

class SeguimientoRegente(models.Model):
    regente = models.ForeignKey(RegenteForestal)

    class Meta:
        verbose_name = ('Seguimiento regente forestal')
        verbose_name_plural = ('Seguimiento regente forestal')
        unique_together = ('regente',)

    def __unicode__(self):
        return self.regente.nombre_regente
    
class DatosSeguimientoRegente(models.Model):
    fecha_seguimiento = models.DateField()
    hombre = models.IntegerField()
    mujeres = models.IntegerField()
    no_pgmf_regencia = models.CharField(max_length=200)
    area_pgmf = models.FloatField()
    codigo_pgmf = models.CharField(max_length=200)
    fecha_ingreso = models.DateField()
    no_poa_regencia = models.CharField(max_length=200)
    area_total_poa = models.FloatField()
    codigo_poa = models.CharField(max_length=200)
    volumenes_totales = models.FloatField()

    fkregente = models.ForeignKey(SeguimientoRegente)
    
    def __unicode__(self):
        return self.no_pgmf_regencia
        
    class Meta:
        verbose_name = ('Seguimiento datos regente forestal')
        verbose_name_plural = ('Seguimiento datos regente forestal')

#--------------------------- Empresa forestal de primera tranformacion ------------------

class OrganizacionEmpresarial(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = ('Tipo organización empresarial')

    def __unicode__(self):
        return self.nombre

class AlianzaNegocio(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = ('Alianza de negocios')

    def __unicode__(self):
        return self.nombre

class TrabajoTranformacion(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = ('Trabajo transformación')
        verbose_name_plural = ('Trabajo transformaciones')

    def __unicode__(self):
        return self.nombre

class ServicioSecado(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = ('Servicio de secado de la madera')
        verbose_name_plural = ('Servicio de secado de la madera')

    def __unicode__(self):
        return self.nombre

class ProductosVenden(models.Model):
    nombre = models.CharField(max_length=200)

    class Meta:
        verbose_name = ('Productos que venden')
        verbose_name_plural = ('Productos que venden')

    def __unicode__(self):
        return self.nombre

class EmpresaPrimeraTransformacion(models.Model):
    fecha_llenado = models.DateField()
    encuestador = models.ForeignKey(Encuestador)
    empresa = models.ForeignKey(Empresa)
    nombre_empresa_forestal = models.CharField(max_length=200)
    nombre_corto = models.CharField(max_length=50)
    fecha_creacion = models.IntegerField('Año de creación')
    org_empresarial = models.ManyToManyField(OrganizacionEmpresarial)
    nombre_director = models.CharField(max_length=200)
    cedula = models.CharField(max_length=50)
    alianza = models.ManyToManyField(AlianzaNegocio)
    organizado = models.ManyToManyField(Organizado)
    desde = models.DateField(null=True, blank=True)
    tel_convencional = models.CharField(max_length=50, null=True, blank=True)
    tel_celular = models.CharField(max_length=50, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    pagina_web = models.URLField(null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    departamento = models.ForeignKey(Departamento)
    municipio = ChainedForeignKey(
        Municipio,
        chained_field="departamento",
        chained_model_field="departamento",
        show_all=False,
        auto_choose=True
    )
    comunidad = ChainedForeignKey(
        Comunidad,
        chained_field="municipio",
        chained_model_field="municipio",
        show_all=False,
        auto_choose=True
    )
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    gobierno_gti = models.IntegerField('Gobierno territorial indígena (GTI)', choices=SINO_CHOICE)
    nombre_gti = models.ForeignKey(GobiernoGti, null=True, blank=True)
    area_trabajo = models.ManyToManyField(TrabajoTranformacion)
    servicio_secado = models.ManyToManyField(ServicioSecado)
    capasidad_horno = models.FloatField()
    productos_venden = models.ManyToManyField(ProductosVenden)
    otro_social = models.ManyToManyField(SocialesEconomico, null=True, blank=True)
    otro_ambiental = models.ManyToManyField(Ambientales, null=True, blank=True)

    class Meta:
        verbose_name = ('Empresa forestal de primera transformación')
        verbose_name_plural = ('Empresa forestal de primera transformación')

    def __unicode__(self):
        return self.nombre_corto

# -------------------------- Seguimiento Primera transformacion ----------------
    
class SeguimientoPrimeraTransformacion(models.Model):
    nombre_empresa = models.ForeignKey(EmpresaPrimeraTransformacion)

    class Meta:
        verbose_name = ('Seguimiento empresa forestal primera transformación')
        verbose_name_plural = ('Seguimiento empresa forestal primera transformación')
        unique_together = ('nombre_empresa',)
            
    def __unicode__(self):
        return self.nombre_empresa.nombre_corto

class AsistenciaTecnica(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Asistencia técnica"

    def __unicode__(self):
        return self.nombre

class ServicioExtraccion(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Servicio de extracción"

    def __unicode__(self):
        return self.nombre

class EmpresaComercializadora(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Empresa comercializadora"

    def __unicode__(self):
        return self.nombre

class RelacionComercial(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Tipo de relación comercial"

    def __unicode__(self):
        return self.nombre

class ProductoVenden(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Tipo de productos que le vende"

    def __unicode__(self):
        return self.nombre

#-------------------------- seguimiento datos primera tranformación ----------------

class DatosPrimeraTransforma(models.Model):
    fecha = models.DateField()
    hombres = models.IntegerField()
    mujeres = models.IntegerField()
    tipo_certificacion = models.ManyToManyField(TipoCertificacion, 
                        verbose_name="Tipo de certificación")
    codigo_certificacion = models.CharField(max_length=100)
    estado_certificado = models.IntegerField(choices=ESTADO_CERTIFICADO_CHOICE)
    entidad_certificadora = models.ForeignKey(EntidadCertificadora, null=True, blank=True)
    status = models.DateField()
    regente = models.ForeignKey(RegenteForestal, null=True, blank=True)
    asistencia = models.ForeignKey(AsistenciaTecnica, null=True, blank=True)
    servicio_extraccion = models.ForeignKey(ServicioExtraccion, null=True, blank=True)
    empresa = models.ForeignKey(EmpresaComercializadora, null=True, blank=True)
    relacion = models.ForeignKey(RelacionComercial, null=True, blank=True)
    producto_vende = models.ManyToManyField(ProductoVenden, null=True, blank=True)
    desde = models.IntegerField('Desde cuándo le vende', null=True, blank=True)
    volumen_madera_rollo = models.FloatField()
    volumen_madera_aserrada = models.FloatField()
    volumen_carbon = models.FloatField()
    volumen_lena = models.FloatField('Leña')

    p_tranformacion = models.ForeignKey(SeguimientoPrimeraTransformacion)

    #def __unicode__(self):
    #    return self.fecha

    class Meta:
        verbose_name_plural = "Datos de seguimiento de primera transformación"

#-------------------------------- Empresa forestal de segunda transformacion --------------

class AreaTrabajoSegunda(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Área de trabajo de segunda transformación"

    def __unicode__(self):
        return self.nombre

class ApoyoProduccion(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Prestador de servicio de apoyo a la producción"

    def __unicode__(self):
        return self.nombre

class ProductosVendenSegunda(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Productos que venden de la segunda transformación"

    def __unicode__(self):
        return self.nombre

class NoMaderable(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "No maderables"

    def __unicode__(self):
        return self.nombre   

class NivelTecnologico(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Nivel tecnológico"

    def __unicode__(self):
        return self.nombre  

class VisionEmpresarial(models.Model):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Visión empresarial"

    def __unicode__(self):
        return self.nombre       

class EmpresaSegundaTransformacion(models.Model):
    fecha = models.DateField()
    encuestador = models.ForeignKey(Encuestador)
    empresa = models.ForeignKey(Empresa)
    nombre_comercial = models.CharField(max_length=200)
    nombre_corto = models.CharField(max_length=50)
    creacion = models.IntegerField('Año de creación')
    funcionando = models.IntegerField('Años funcionando')
    org_empresarial = models.ManyToManyField(OrganizacionEmpresarial)
    nombre_director = models.CharField(max_length=200)
    cedula = models.CharField(max_length=50)
    organizado = models.ManyToManyField(Organizado)
    desde = models.DateField(null=True, blank=True)
    tel_convencional = models.CharField(max_length=50, null=True, blank=True)
    tel_celular = models.CharField(max_length=50, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    pagina_web = models.URLField(null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    departamento = models.ForeignKey(Departamento)
    municipio = ChainedForeignKey(
        Municipio,
        chained_field="departamento",
        chained_model_field="departamento",
        show_all=False,
        auto_choose=True
    )
    comunidad = ChainedForeignKey(
        Comunidad,
        chained_field="municipio",
        chained_model_field="municipio",
        show_all=False,
        auto_choose=True
    )
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    gobierno_gti = models.IntegerField('Gobierno territorial indígena (GTI)', choices=SINO_CHOICE)
    nombre_gti = models.ForeignKey(GobiernoGti, null=True, blank=True)
    area_trabajo = models.ManyToManyField(AreaTrabajoSegunda)
    apoyo_produccion = models.ManyToManyField(ApoyoProduccion)
    madera = models.ForeignKey(Madera, null=True, blank=True)
    producto_vende = models.ManyToManyField(ProductosVendenSegunda)
    no_maderable = models.ManyToManyField(NoMaderable)
    nivel_tecnologico = models.ManyToManyField(NivelTecnologico)
    propia_secado = models.FloatField('Capacidad propia de secado de la madera')
    volumen_anual = models.FloatField('Volumen anual de madera procesada(pie tablar)')
    promedio = models.FloatField('Promedio mensual de las unidades producidas')
    otro_social = models.ManyToManyField(SocialesEconomico, null=True, blank=True)
    otro_ambiental = models.ManyToManyField(Ambientales, null=True, blank=True)
    vision_empresarial = models.ManyToManyField(VisionEmpresarial)

    def __unicode__(self):
        return self.nombre_comercial

    class Meta:
        verbose_name_plural = "Empresas forestal de segunda transformación"
#----------------------- seguimiento de la segunda tranformacion --------------------

class SeguimientoSegundaTranformacion(models.Model):
    nombre = models.ForeignKey(EmpresaSegundaTransformacion)

    def __unicode__(self):
        return self.nombre.nombre_comercial

    class Meta:
        verbose_name_plural = "Seguimiento empresa forestal de segunda transformación"
        unique_together = ('nombre',)

class AlianzaNegocion(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

class PrestadoresServicioOperacionales(models.Model):
    nombre = models.CharField(max_length=200)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Principales prestadores de servicios operacionales"

# ---------------------------Datos seguimiento segunda tranformación ---------------------
class TipoProductoSegundaTransformacion(models.Model):
    nombre = models.CharField(max_length=150)

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de productos de la segunda transformación"

class DatosSegundaTranformacion(models.Model):
    fecha = models.DateField()
    alianza = models.ManyToManyField(AlianzaNegocio)
    hombres = models.IntegerField()
    mujeres = models.IntegerField()
    tipo_certificacion = models.ManyToManyField(TipoCertificacion, 
                        verbose_name="Tipo de certificación")
    codigo = models.CharField('Código de certificación', max_length=50)
    estado_certificado = models.IntegerField(choices=ESTADO_CERTIFICADO_CHOICE)
    entidad_certificadora = models.ForeignKey(EntidadCertificadora, null=True, blank=True)
    fecha_status = models.DateField()
    proveedores = models.ManyToManyField(ProveedoresSuministros)
    servicio_operacionales = models.ManyToManyField(PrestadoresServicioOperacionales, null=True, blank=True)
    #empresa = models.ForeignKey(EmpresaComercializadora)
    relacion = models.ForeignKey(RelacionComercial, null=True, blank=True)
    t_producto = models.ManyToManyField(TipoProductoSegundaTransformacion, verbose_name=u'Tipo producto',null=True, blank=True)
    desde_cuando = models.DateField(null=True, blank=True)
    volumen_promedio = models.FloatField(null=True, blank=True)

    fksegunda = models.ForeignKey(SeguimientoSegundaTranformacion)

    def __unicode__(self):
        return self.codigo

    class Meta:
        verbose_name = ('Datos de seguimiento segunda transformación')
        verbose_name_plural = ('Datos de seguimiento segunda transformación')