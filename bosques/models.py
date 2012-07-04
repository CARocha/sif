from django.db import models
import datetime

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
    nombre = models.CharField(max_length)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Tipo de propiedad del bosque"
        
class Organizado(models.Model):
    nombre = models.CharField(max_length)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Organizado"

class Organizacion(models.Model):
    nombre = models.CharField(max_length)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Organizacion"
        
class GobiernoGti(models.Model):
    nombre = models.CharField(max_length)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Gobiernos territoriales indigenas"

class EspeciesNaturales(models.Model):
    nombre = models.CharField(max_length)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Especies forestales naturales"

class EspeciesIntroducidas(models.Model):
    nombre = models.CharField(max_length)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Especies plantaciones introducidas"
        
MADERA_CHOICE = (
    (1, 'Maderas en rollo')
)

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
    nombre = models.CharField(max_length)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Tipo de productos"
        
class ProcesoIndustrialBosque(models.Model):
    nombre = models.CharField(max_length)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Otros procesos industriales integrados al bosque"
        
class TipoSecados(models.Model):
    nombre = models.CharField(max_length)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Tipos de secados"

class BuenasPracticas(models.Model):
    nombre = models.CharField(max_length)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Buenas prácticas que implementan"

class ProveedoresSuministros(models.Model):
    nombre = models.CharField(max_length)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Principales proveedores de suministros y materiales"
        
class TipoBosqueUmf(models.Model):
    nombre = models.CharField(max_length)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Tipo de Bosque de la UMF"
        
class MetodoExtraccion(models.Model):
    nombre = models.CharField(max_length)
    
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural = "Método de extracción de la madera"
        
#--------------- Ficha principal -----------------------------------------------                
class PropietarioBosques(models.Model):
    fecha = models.DateField()
    encuestador = models.ForeignKey(Encuestador)
    empresa = models.ForeignKey(Empresa)
    nombre_propietario = models.CharField('Nombre del propietario o representante legal', 
                                           max_length=200, 
                                           help_text='Nombre del propietario o representante legal')
    sexo_propietario = models.IntegerField(choices=SEXO_CHOICE)
    cedula_propietario = models.CharField(max_length=200, help_text='Cédula')
    propietario_ruc = models.CharField(max_length=200, help_text='Registro RUC')
    representante_tecnico = models.CharField('Nombre del representante técnico', 
                                           max_length=200, 
                                           help_text='Nombre del representante técnico')
    sexo_tecnico = models.IntegerField(choices=SEXO_CHOICE)
    cedula_tecnico = models.CharField(max_length=200, help_text='Cédula')
    tecnico_ruc = models.CharField(max_length=200, help_text='Registro RUC')
    nombre_propiedad = models.CharField('Nombre de la propiedad', 
                                           max_length=200, 
                                           help_text='Nombre de la propiedad')
    registro_catastral = models.CharField(max_length=200, help_text='No. registro catrastal')
    tipo_propiedad = models.ManyToManyField(TipoPropiedadBosque)
    area_propiedad = models.FloatField('Área total de la propiedad en ha', help_text='área total en ha')
    tel_convencional = models.CharField('Teléfono convencional', max_length=15, null=True, blank=True)
    tel_celular = models.CharField('Teléfono celular', max_length=15, null=True, blank=True)
    email = models.EmailField('Correo electrónico', null=True, blank=True)
    web = models.LinkField('Página web', null=True, blank=True)
    direccion = models.CharField('Dirección', max_length=200, null=True, blank=True)
    latitud = models.FloatField(null=True, blank=True)
    longitud = models.FloatField(null=True, blank=True)
    departamento = models.ForeignKey(Departamento)
    municipio = models.ForeignKey(Municipio)
    comunidad = models.ForeignKey(Comunidad)
    organizado = models.ManyToManyField(Organizado)
    organizacion = models.ManyToManyField(Organizacion)
    desde = models.DateField()
    gobierno_gti = models.IntegerField('Gobierno territorial indigena (GTI)', choices=SINO_CHOICE)
    nombre_gti = models.ForeignKey(GobiernoGti)
    naturales = models.ManyToManyField(EspeciesNaturales, verbose_name='Especies naturales')
    introducida = models.ManyToManyField(EspeciesIntroducidas, verbose_name='Especies introducidas')
    madera = models.IntegerField(choices=MADERA_CHOICE)
    madera_procesada = models.IntegerField(choices=MADERA_PROCESADAS_CHOICE)
    consumo = models.IntegerField(choices=CONSUMO_CHOICE)
    producto_no_maderable = models.IntegerField(choices=SINO_CHOICE)
    tipo_producto = models.ManyToManyField(TipoProducto)
    procesos_industriales = models.ManyToManyField(ProcesoIndustrialBosque)
    secado = models.ManyToManyField(TipoSecados)
    buenas_practicas = models.ManyToManyField(BuenasPracticas)
    proveedores = models.ManyToManyField(ProveedoresSuministros)
    nombre_umf = models.CharField('Nombre de la UMF', max_length=200)
    area_umf = models.FloatField('Área de la UMF (ha)')
    codigo_umf = models.CharField('Código de la UMF (INAFOR)', max_length=200)
    periodo_vigencia = models.IntegerField('Periodo de vigencia (años)')
    poas_umf = models.IntegerField('POAS en la UMF')
    bosques_umf = model.ManyToManyField(TipoBosqueUmf)
    extraccion = models.ManyToManyField(MetodoExtraccion)
    secado_horno = models.FloatField('Capacidad de secado del horno')
    codigo_certificado = models.CharField(max_length=200, null=True, blank=True)
    area_certificada = models.FloatField(null=True, blank=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
