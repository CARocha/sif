# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OrganizacionPublica'
        db.create_table('bosques_organizacionpublica', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('bosques', ['OrganizacionPublica'])

        # Adding model 'SeguimientoSegundaTranformacion'
        db.create_table('bosques_seguimientosegundatranformacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.EmpresaSegundaTransformacion'])),
        ))
        db.send_create_signal('bosques', ['SeguimientoSegundaTranformacion'])

        # Adding model 'EmpresaComercializadora'
        db.create_table('bosques_empresacomercializadora', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('bosques', ['EmpresaComercializadora'])

        # Adding model 'DatosPrimeraTransforma'
        db.create_table('bosques_datosprimeratransforma', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('hombres', self.gf('django.db.models.fields.IntegerField')()),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')()),
            ('codigo_certificacion', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('estado_certificado', self.gf('django.db.models.fields.IntegerField')()),
            ('entidad_certificadora', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.EntidadCertificadora'], null=True, blank=True)),
            ('status', self.gf('django.db.models.fields.DateField')()),
            ('regente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.RegenteForestal'])),
            ('asistencia', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.AsistenciaTecnica'])),
            ('servicio_extraccion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.ServicioExtraccion'])),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.EmpresaComercializadora'])),
            ('relacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.RelacionComercial'])),
            ('desde', self.gf('django.db.models.fields.IntegerField')()),
            ('volumen_madera_rollo', self.gf('django.db.models.fields.FloatField')()),
            ('volumen_madera_aserrada', self.gf('django.db.models.fields.FloatField')()),
            ('volumen_carbon', self.gf('django.db.models.fields.FloatField')()),
            ('volumen_lena', self.gf('django.db.models.fields.FloatField')()),
            ('p_tranformacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.SeguimientoPrimeraTransformacion'])),
        ))
        db.send_create_signal('bosques', ['DatosPrimeraTransforma'])

        # Adding M2M table for field tipo_certificacion on 'DatosPrimeraTransforma'
        db.create_table('bosques_datosprimeratransforma_tipo_certificacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('datosprimeratransforma', models.ForeignKey(orm['bosques.datosprimeratransforma'], null=False)),
            ('tipocertificacion', models.ForeignKey(orm['bosques.tipocertificacion'], null=False))
        ))
        db.create_unique('bosques_datosprimeratransforma_tipo_certificacion', ['datosprimeratransforma_id', 'tipocertificacion_id'])

        # Adding M2M table for field producto_vende on 'DatosPrimeraTransforma'
        db.create_table('bosques_datosprimeratransforma_producto_vende', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('datosprimeratransforma', models.ForeignKey(orm['bosques.datosprimeratransforma'], null=False)),
            ('productovenden', models.ForeignKey(orm['bosques.productovenden'], null=False))
        ))
        db.create_unique('bosques_datosprimeratransforma_producto_vende', ['datosprimeratransforma_id', 'productovenden_id'])

        # Adding model 'AlianzaNegocion'
        db.create_table('bosques_alianzanegocion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bosques', ['AlianzaNegocion'])

        # Adding model 'ServicioExtraccion'
        db.create_table('bosques_servicioextraccion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('bosques', ['ServicioExtraccion'])

        # Adding model 'ApoyoProduccion'
        db.create_table('bosques_apoyoproduccion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('bosques', ['ApoyoProduccion'])

        # Adding model 'NoMaderable'
        db.create_table('bosques_nomaderable', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('bosques', ['NoMaderable'])

        # Adding model 'DatosSegundaTranformacion'
        db.create_table('bosques_datossegundatranformacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('hombres', self.gf('django.db.models.fields.IntegerField')()),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')()),
            ('codigo', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('estado_certificado', self.gf('django.db.models.fields.IntegerField')()),
            ('entidad_certificadora', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.EntidadCertificadora'], null=True, blank=True)),
            ('fecha_status', self.gf('django.db.models.fields.DateField')()),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.EmpresaComercializadora'])),
            ('relacion', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.RelacionComercial'])),
            ('desde_cuando', self.gf('django.db.models.fields.DateField')()),
            ('volumen_promedio', self.gf('django.db.models.fields.FloatField')()),
            ('fksegunda', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.SeguimientoSegundaTranformacion'])),
        ))
        db.send_create_signal('bosques', ['DatosSegundaTranformacion'])

        # Adding M2M table for field alianza on 'DatosSegundaTranformacion'
        db.create_table('bosques_datossegundatranformacion_alianza', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('datossegundatranformacion', models.ForeignKey(orm['bosques.datossegundatranformacion'], null=False)),
            ('alianzanegocio', models.ForeignKey(orm['bosques.alianzanegocio'], null=False))
        ))
        db.create_unique('bosques_datossegundatranformacion_alianza', ['datossegundatranformacion_id', 'alianzanegocio_id'])

        # Adding M2M table for field tipo_certificacion on 'DatosSegundaTranformacion'
        db.create_table('bosques_datossegundatranformacion_tipo_certificacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('datossegundatranformacion', models.ForeignKey(orm['bosques.datossegundatranformacion'], null=False)),
            ('tipocertificacion', models.ForeignKey(orm['bosques.tipocertificacion'], null=False))
        ))
        db.create_unique('bosques_datossegundatranformacion_tipo_certificacion', ['datossegundatranformacion_id', 'tipocertificacion_id'])

        # Adding M2M table for field proveedores on 'DatosSegundaTranformacion'
        db.create_table('bosques_datossegundatranformacion_proveedores', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('datossegundatranformacion', models.ForeignKey(orm['bosques.datossegundatranformacion'], null=False)),
            ('proveedoressuministros', models.ForeignKey(orm['bosques.proveedoressuministros'], null=False))
        ))
        db.create_unique('bosques_datossegundatranformacion_proveedores', ['datossegundatranformacion_id', 'proveedoressuministros_id'])

        # Adding M2M table for field servicio_operacionales on 'DatosSegundaTranformacion'
        db.create_table('bosques_datossegundatranformacion_servicio_operacionales', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('datossegundatranformacion', models.ForeignKey(orm['bosques.datossegundatranformacion'], null=False)),
            ('prestadoresserviciooperacionales', models.ForeignKey(orm['bosques.prestadoresserviciooperacionales'], null=False))
        ))
        db.create_unique('bosques_datossegundatranformacion_servicio_operacionales', ['datossegundatranformacion_id', 'prestadoresserviciooperacionales_id'])

        # Adding M2M table for field tipo_producto on 'DatosSegundaTranformacion'
        db.create_table('bosques_datossegundatranformacion_tipo_producto', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('datossegundatranformacion', models.ForeignKey(orm['bosques.datossegundatranformacion'], null=False)),
            ('tipoproducto', models.ForeignKey(orm['bosques.tipoproducto'], null=False))
        ))
        db.create_unique('bosques_datossegundatranformacion_tipo_producto', ['datossegundatranformacion_id', 'tipoproducto_id'])

        # Adding model 'PrestadoresServicioOperacionales'
        db.create_table('bosques_prestadoresserviciooperacionales', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bosques', ['PrestadoresServicioOperacionales'])

        # Adding model 'OrganizacionEmpresarial'
        db.create_table('bosques_organizacionempresarial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('bosques', ['OrganizacionEmpresarial'])

        # Adding model 'RelacionComercial'
        db.create_table('bosques_relacioncomercial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('bosques', ['RelacionComercial'])

        # Adding model 'EmpresaSegundaTransformacion'
        db.create_table('bosques_empresasegundatransformacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('encuestador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.Encuestador'])),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.Empresa'])),
            ('nombre_comercial', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('nombre_corto', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('creacion', self.gf('django.db.models.fields.IntegerField')()),
            ('funcionando', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre_director', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cedula', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('desde', self.gf('django.db.models.fields.DateField')()),
            ('tel_convencional', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('tel_celular', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('pagina_web', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Departamento'])),
            ('municipio', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['lugar.Municipio'])),
            ('comunidad', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['lugar.Comunidad'])),
            ('latitud', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitud', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('gobierno_gti', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre_gti', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.GobiernoGti'], null=True, blank=True)),
            ('madera', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.Madera'], null=True, blank=True)),
            ('propia_secado', self.gf('django.db.models.fields.FloatField')()),
            ('volumen_anual', self.gf('django.db.models.fields.FloatField')()),
            ('promedio', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('bosques', ['EmpresaSegundaTransformacion'])

        # Adding M2M table for field org_empresarial on 'EmpresaSegundaTransformacion'
        db.create_table('bosques_empresasegundatransformacion_org_empresarial', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('empresasegundatransformacion', models.ForeignKey(orm['bosques.empresasegundatransformacion'], null=False)),
            ('organizacionempresarial', models.ForeignKey(orm['bosques.organizacionempresarial'], null=False))
        ))
        db.create_unique('bosques_empresasegundatransformacion_org_empresarial', ['empresasegundatransformacion_id', 'organizacionempresarial_id'])

        # Adding M2M table for field organizado on 'EmpresaSegundaTransformacion'
        db.create_table('bosques_empresasegundatransformacion_organizado', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('empresasegundatransformacion', models.ForeignKey(orm['bosques.empresasegundatransformacion'], null=False)),
            ('organizado', models.ForeignKey(orm['bosques.organizado'], null=False))
        ))
        db.create_unique('bosques_empresasegundatransformacion_organizado', ['empresasegundatransformacion_id', 'organizado_id'])

        # Adding M2M table for field area_trabajo on 'EmpresaSegundaTransformacion'
        db.create_table('bosques_empresasegundatransformacion_area_trabajo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('empresasegundatransformacion', models.ForeignKey(orm['bosques.empresasegundatransformacion'], null=False)),
            ('areatrabajosegunda', models.ForeignKey(orm['bosques.areatrabajosegunda'], null=False))
        ))
        db.create_unique('bosques_empresasegundatransformacion_area_trabajo', ['empresasegundatransformacion_id', 'areatrabajosegunda_id'])

        # Adding M2M table for field apoyo_produccion on 'EmpresaSegundaTransformacion'
        db.create_table('bosques_empresasegundatransformacion_apoyo_produccion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('empresasegundatransformacion', models.ForeignKey(orm['bosques.empresasegundatransformacion'], null=False)),
            ('apoyoproduccion', models.ForeignKey(orm['bosques.apoyoproduccion'], null=False))
        ))
        db.create_unique('bosques_empresasegundatransformacion_apoyo_produccion', ['empresasegundatransformacion_id', 'apoyoproduccion_id'])

        # Adding M2M table for field producto_vende on 'EmpresaSegundaTransformacion'
        db.create_table('bosques_empresasegundatransformacion_producto_vende', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('empresasegundatransformacion', models.ForeignKey(orm['bosques.empresasegundatransformacion'], null=False)),
            ('productosvendensegunda', models.ForeignKey(orm['bosques.productosvendensegunda'], null=False))
        ))
        db.create_unique('bosques_empresasegundatransformacion_producto_vende', ['empresasegundatransformacion_id', 'productosvendensegunda_id'])

        # Adding M2M table for field no_maderable on 'EmpresaSegundaTransformacion'
        db.create_table('bosques_empresasegundatransformacion_no_maderable', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('empresasegundatransformacion', models.ForeignKey(orm['bosques.empresasegundatransformacion'], null=False)),
            ('nomaderable', models.ForeignKey(orm['bosques.nomaderable'], null=False))
        ))
        db.create_unique('bosques_empresasegundatransformacion_no_maderable', ['empresasegundatransformacion_id', 'nomaderable_id'])

        # Adding M2M table for field nivel_tecnologico on 'EmpresaSegundaTransformacion'
        db.create_table('bosques_empresasegundatransformacion_nivel_tecnologico', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('empresasegundatransformacion', models.ForeignKey(orm['bosques.empresasegundatransformacion'], null=False)),
            ('niveltecnologico', models.ForeignKey(orm['bosques.niveltecnologico'], null=False))
        ))
        db.create_unique('bosques_empresasegundatransformacion_nivel_tecnologico', ['empresasegundatransformacion_id', 'niveltecnologico_id'])

        # Adding M2M table for field otro_social on 'EmpresaSegundaTransformacion'
        db.create_table('bosques_empresasegundatransformacion_otro_social', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('empresasegundatransformacion', models.ForeignKey(orm['bosques.empresasegundatransformacion'], null=False)),
            ('socialeseconomico', models.ForeignKey(orm['bosques.socialeseconomico'], null=False))
        ))
        db.create_unique('bosques_empresasegundatransformacion_otro_social', ['empresasegundatransformacion_id', 'socialeseconomico_id'])

        # Adding M2M table for field otro_ambiental on 'EmpresaSegundaTransformacion'
        db.create_table('bosques_empresasegundatransformacion_otro_ambiental', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('empresasegundatransformacion', models.ForeignKey(orm['bosques.empresasegundatransformacion'], null=False)),
            ('ambientales', models.ForeignKey(orm['bosques.ambientales'], null=False))
        ))
        db.create_unique('bosques_empresasegundatransformacion_otro_ambiental', ['empresasegundatransformacion_id', 'ambientales_id'])

        # Adding M2M table for field vision_empresarial on 'EmpresaSegundaTransformacion'
        db.create_table('bosques_empresasegundatransformacion_vision_empresarial', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('empresasegundatransformacion', models.ForeignKey(orm['bosques.empresasegundatransformacion'], null=False)),
            ('visionempresarial', models.ForeignKey(orm['bosques.visionempresarial'], null=False))
        ))
        db.create_unique('bosques_empresasegundatransformacion_vision_empresarial', ['empresasegundatransformacion_id', 'visionempresarial_id'])

        # Adding model 'AsistenciaTecnica'
        db.create_table('bosques_asistenciatecnica', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('bosques', ['AsistenciaTecnica'])

        # Adding model 'ProductosVendenSegunda'
        db.create_table('bosques_productosvendensegunda', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('bosques', ['ProductosVendenSegunda'])

        # Adding model 'ServicioSecado'
        db.create_table('bosques_serviciosecado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bosques', ['ServicioSecado'])

        # Adding model 'ProductoVenden'
        db.create_table('bosques_productovenden', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('bosques', ['ProductoVenden'])

        # Adding model 'AreaTrabajoSegunda'
        db.create_table('bosques_areatrabajosegunda', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('bosques', ['AreaTrabajoSegunda'])

        # Adding model 'AlianzaNegocio'
        db.create_table('bosques_alianzanegocio', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('bosques', ['AlianzaNegocio'])

        # Adding model 'TrabajoTranformacion'
        db.create_table('bosques_trabajotranformacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bosques', ['TrabajoTranformacion'])

        # Adding model 'ProductosVenden'
        db.create_table('bosques_productosvenden', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bosques', ['ProductosVenden'])

        # Adding model 'SeguimientoRegente'
        db.create_table('bosques_seguimientoregente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('regente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.RegenteForestal'])),
        ))
        db.send_create_signal('bosques', ['SeguimientoRegente'])

        # Adding model 'EmpresaPrimeraTransformacion'
        db.create_table('bosques_empresaprimeratransformacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_llenado', self.gf('django.db.models.fields.DateField')()),
            ('encuestador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.Encuestador'])),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.Empresa'])),
            ('nombre_empresa_forestal', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('nombre_corto', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('fecha_creacion', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre_director', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('cedula', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('desde', self.gf('django.db.models.fields.DateField')()),
            ('tel_convencional', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('tel_celular', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('pagina_web', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Departamento'])),
            ('municipio', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['lugar.Municipio'])),
            ('comunidad', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['lugar.Comunidad'])),
            ('latitud', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitud', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('gobierno_gti', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre_gti', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.GobiernoGti'], null=True, blank=True)),
            ('capasidad_horno', self.gf('django.db.models.fields.FloatField')()),
        ))
        db.send_create_signal('bosques', ['EmpresaPrimeraTransformacion'])

        # Adding M2M table for field org_empresarial on 'EmpresaPrimeraTransformacion'
        db.create_table('bosques_empresaprimeratransformacion_org_empresarial', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('empresaprimeratransformacion', models.ForeignKey(orm['bosques.empresaprimeratransformacion'], null=False)),
            ('organizacionempresarial', models.ForeignKey(orm['bosques.organizacionempresarial'], null=False))
        ))
        db.create_unique('bosques_empresaprimeratransformacion_org_empresarial', ['empresaprimeratransformacion_id', 'organizacionempresarial_id'])

        # Adding M2M table for field alianza on 'EmpresaPrimeraTransformacion'
        db.create_table('bosques_empresaprimeratransformacion_alianza', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('empresaprimeratransformacion', models.ForeignKey(orm['bosques.empresaprimeratransformacion'], null=False)),
            ('alianzanegocio', models.ForeignKey(orm['bosques.alianzanegocio'], null=False))
        ))
        db.create_unique('bosques_empresaprimeratransformacion_alianza', ['empresaprimeratransformacion_id', 'alianzanegocio_id'])

        # Adding M2M table for field organizado on 'EmpresaPrimeraTransformacion'
        db.create_table('bosques_empresaprimeratransformacion_organizado', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('empresaprimeratransformacion', models.ForeignKey(orm['bosques.empresaprimeratransformacion'], null=False)),
            ('organizado', models.ForeignKey(orm['bosques.organizado'], null=False))
        ))
        db.create_unique('bosques_empresaprimeratransformacion_organizado', ['empresaprimeratransformacion_id', 'organizado_id'])

        # Adding M2M table for field area_trabajo on 'EmpresaPrimeraTransformacion'
        db.create_table('bosques_empresaprimeratransformacion_area_trabajo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('empresaprimeratransformacion', models.ForeignKey(orm['bosques.empresaprimeratransformacion'], null=False)),
            ('trabajotranformacion', models.ForeignKey(orm['bosques.trabajotranformacion'], null=False))
        ))
        db.create_unique('bosques_empresaprimeratransformacion_area_trabajo', ['empresaprimeratransformacion_id', 'trabajotranformacion_id'])

        # Adding M2M table for field servicio_secado on 'EmpresaPrimeraTransformacion'
        db.create_table('bosques_empresaprimeratransformacion_servicio_secado', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('empresaprimeratransformacion', models.ForeignKey(orm['bosques.empresaprimeratransformacion'], null=False)),
            ('serviciosecado', models.ForeignKey(orm['bosques.serviciosecado'], null=False))
        ))
        db.create_unique('bosques_empresaprimeratransformacion_servicio_secado', ['empresaprimeratransformacion_id', 'serviciosecado_id'])

        # Adding M2M table for field productos_venden on 'EmpresaPrimeraTransformacion'
        db.create_table('bosques_empresaprimeratransformacion_productos_venden', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('empresaprimeratransformacion', models.ForeignKey(orm['bosques.empresaprimeratransformacion'], null=False)),
            ('productosvenden', models.ForeignKey(orm['bosques.productosvenden'], null=False))
        ))
        db.create_unique('bosques_empresaprimeratransformacion_productos_venden', ['empresaprimeratransformacion_id', 'productosvenden_id'])

        # Adding M2M table for field otro_social on 'EmpresaPrimeraTransformacion'
        db.create_table('bosques_empresaprimeratransformacion_otro_social', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('empresaprimeratransformacion', models.ForeignKey(orm['bosques.empresaprimeratransformacion'], null=False)),
            ('socialeseconomico', models.ForeignKey(orm['bosques.socialeseconomico'], null=False))
        ))
        db.create_unique('bosques_empresaprimeratransformacion_otro_social', ['empresaprimeratransformacion_id', 'socialeseconomico_id'])

        # Adding M2M table for field otro_ambiental on 'EmpresaPrimeraTransformacion'
        db.create_table('bosques_empresaprimeratransformacion_otro_ambiental', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('empresaprimeratransformacion', models.ForeignKey(orm['bosques.empresaprimeratransformacion'], null=False)),
            ('ambientales', models.ForeignKey(orm['bosques.ambientales'], null=False))
        ))
        db.create_unique('bosques_empresaprimeratransformacion_otro_ambiental', ['empresaprimeratransformacion_id', 'ambientales_id'])

        # Adding model 'VisionEmpresarial'
        db.create_table('bosques_visionempresarial', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('bosques', ['VisionEmpresarial'])

        # Adding model 'NivelTecnologico'
        db.create_table('bosques_niveltecnologico', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal('bosques', ['NivelTecnologico'])

        # Adding model 'RegenteForestal'
        db.create_table('bosques_regenteforestal', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('llenado', self.gf('django.db.models.fields.DateField')()),
            ('encuestador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.Encuestador'])),
            ('nombre_regente', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('codigo_regente', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('no_cedula', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('org_publica', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.OrganizacionPublica'])),
            ('tel_convencional', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('tel_celular', self.gf('django.db.models.fields.CharField')(max_length=50, null=True, blank=True)),
            ('correo', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('pagina_web', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Departamento'])),
            ('municipio', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['lugar.Municipio'])),
            ('comunidad', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['lugar.Comunidad'])),
            ('fecha_acreditacion', self.gf('django.db.models.fields.DateField')()),
            ('experiencia', self.gf('django.db.models.fields.IntegerField')()),
            ('desde', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('perfil', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('bosques', ['RegenteForestal'])

        # Adding M2M table for field organizado on 'RegenteForestal'
        db.create_table('bosques_regenteforestal_organizado', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('regenteforestal', models.ForeignKey(orm['bosques.regenteforestal'], null=False)),
            ('organizado', models.ForeignKey(orm['bosques.organizado'], null=False))
        ))
        db.create_unique('bosques_regenteforestal_organizado', ['regenteforestal_id', 'organizado_id'])

        # Adding M2M table for field organizacion on 'RegenteForestal'
        db.create_table('bosques_regenteforestal_organizacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('regenteforestal', models.ForeignKey(orm['bosques.regenteforestal'], null=False)),
            ('organizacion', models.ForeignKey(orm['bosques.organizacion'], null=False))
        ))
        db.create_unique('bosques_regenteforestal_organizacion', ['regenteforestal_id', 'organizacion_id'])

        # Adding M2M table for field area_trabajo on 'RegenteForestal'
        db.create_table('bosques_regenteforestal_area_trabajo', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('regenteforestal', models.ForeignKey(orm['bosques.regenteforestal'], null=False)),
            ('areatrabajo', models.ForeignKey(orm['bosques.areatrabajo'], null=False))
        ))
        db.create_unique('bosques_regenteforestal_area_trabajo', ['regenteforestal_id', 'areatrabajo_id'])

        # Adding model 'AreaTrabajo'
        db.create_table('bosques_areatrabajo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('bosques', ['AreaTrabajo'])

        # Adding model 'DatosSeguimientoRegente'
        db.create_table('bosques_datosseguimientoregente', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_seguimiento', self.gf('django.db.models.fields.DateField')()),
            ('hombre', self.gf('django.db.models.fields.IntegerField')()),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')()),
            ('no_pgmf_regencia', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('area_pgmf', self.gf('django.db.models.fields.FloatField')()),
            ('codigo_pgmf', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('fecha_ingreso', self.gf('django.db.models.fields.DateField')()),
            ('no_poa_regencia', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('area_total_poa', self.gf('django.db.models.fields.FloatField')()),
            ('codigo_poa', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('volumenes_totales', self.gf('django.db.models.fields.FloatField')()),
            ('fkregente', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.SeguimientoRegente'])),
        ))
        db.send_create_signal('bosques', ['DatosSeguimientoRegente'])

        # Adding model 'SeguimientoPrimeraTransformacion'
        db.create_table('bosques_seguimientoprimeratransformacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre_empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.EmpresaPrimeraTransformacion'])),
        ))
        db.send_create_signal('bosques', ['SeguimientoPrimeraTransformacion'])


    def backwards(self, orm):
        # Deleting model 'OrganizacionPublica'
        db.delete_table('bosques_organizacionpublica')

        # Deleting model 'SeguimientoSegundaTranformacion'
        db.delete_table('bosques_seguimientosegundatranformacion')

        # Deleting model 'EmpresaComercializadora'
        db.delete_table('bosques_empresacomercializadora')

        # Deleting model 'DatosPrimeraTransforma'
        db.delete_table('bosques_datosprimeratransforma')

        # Removing M2M table for field tipo_certificacion on 'DatosPrimeraTransforma'
        db.delete_table('bosques_datosprimeratransforma_tipo_certificacion')

        # Removing M2M table for field producto_vende on 'DatosPrimeraTransforma'
        db.delete_table('bosques_datosprimeratransforma_producto_vende')

        # Deleting model 'AlianzaNegocion'
        db.delete_table('bosques_alianzanegocion')

        # Deleting model 'ServicioExtraccion'
        db.delete_table('bosques_servicioextraccion')

        # Deleting model 'ApoyoProduccion'
        db.delete_table('bosques_apoyoproduccion')

        # Deleting model 'NoMaderable'
        db.delete_table('bosques_nomaderable')

        # Deleting model 'DatosSegundaTranformacion'
        db.delete_table('bosques_datossegundatranformacion')

        # Removing M2M table for field alianza on 'DatosSegundaTranformacion'
        db.delete_table('bosques_datossegundatranformacion_alianza')

        # Removing M2M table for field tipo_certificacion on 'DatosSegundaTranformacion'
        db.delete_table('bosques_datossegundatranformacion_tipo_certificacion')

        # Removing M2M table for field proveedores on 'DatosSegundaTranformacion'
        db.delete_table('bosques_datossegundatranformacion_proveedores')

        # Removing M2M table for field servicio_operacionales on 'DatosSegundaTranformacion'
        db.delete_table('bosques_datossegundatranformacion_servicio_operacionales')

        # Removing M2M table for field tipo_producto on 'DatosSegundaTranformacion'
        db.delete_table('bosques_datossegundatranformacion_tipo_producto')

        # Deleting model 'PrestadoresServicioOperacionales'
        db.delete_table('bosques_prestadoresserviciooperacionales')

        # Deleting model 'OrganizacionEmpresarial'
        db.delete_table('bosques_organizacionempresarial')

        # Deleting model 'RelacionComercial'
        db.delete_table('bosques_relacioncomercial')

        # Deleting model 'EmpresaSegundaTransformacion'
        db.delete_table('bosques_empresasegundatransformacion')

        # Removing M2M table for field org_empresarial on 'EmpresaSegundaTransformacion'
        db.delete_table('bosques_empresasegundatransformacion_org_empresarial')

        # Removing M2M table for field organizado on 'EmpresaSegundaTransformacion'
        db.delete_table('bosques_empresasegundatransformacion_organizado')

        # Removing M2M table for field area_trabajo on 'EmpresaSegundaTransformacion'
        db.delete_table('bosques_empresasegundatransformacion_area_trabajo')

        # Removing M2M table for field apoyo_produccion on 'EmpresaSegundaTransformacion'
        db.delete_table('bosques_empresasegundatransformacion_apoyo_produccion')

        # Removing M2M table for field producto_vende on 'EmpresaSegundaTransformacion'
        db.delete_table('bosques_empresasegundatransformacion_producto_vende')

        # Removing M2M table for field no_maderable on 'EmpresaSegundaTransformacion'
        db.delete_table('bosques_empresasegundatransformacion_no_maderable')

        # Removing M2M table for field nivel_tecnologico on 'EmpresaSegundaTransformacion'
        db.delete_table('bosques_empresasegundatransformacion_nivel_tecnologico')

        # Removing M2M table for field otro_social on 'EmpresaSegundaTransformacion'
        db.delete_table('bosques_empresasegundatransformacion_otro_social')

        # Removing M2M table for field otro_ambiental on 'EmpresaSegundaTransformacion'
        db.delete_table('bosques_empresasegundatransformacion_otro_ambiental')

        # Removing M2M table for field vision_empresarial on 'EmpresaSegundaTransformacion'
        db.delete_table('bosques_empresasegundatransformacion_vision_empresarial')

        # Deleting model 'AsistenciaTecnica'
        db.delete_table('bosques_asistenciatecnica')

        # Deleting model 'ProductosVendenSegunda'
        db.delete_table('bosques_productosvendensegunda')

        # Deleting model 'ServicioSecado'
        db.delete_table('bosques_serviciosecado')

        # Deleting model 'ProductoVenden'
        db.delete_table('bosques_productovenden')

        # Deleting model 'AreaTrabajoSegunda'
        db.delete_table('bosques_areatrabajosegunda')

        # Deleting model 'AlianzaNegocio'
        db.delete_table('bosques_alianzanegocio')

        # Deleting model 'TrabajoTranformacion'
        db.delete_table('bosques_trabajotranformacion')

        # Deleting model 'ProductosVenden'
        db.delete_table('bosques_productosvenden')

        # Deleting model 'SeguimientoRegente'
        db.delete_table('bosques_seguimientoregente')

        # Deleting model 'EmpresaPrimeraTransformacion'
        db.delete_table('bosques_empresaprimeratransformacion')

        # Removing M2M table for field org_empresarial on 'EmpresaPrimeraTransformacion'
        db.delete_table('bosques_empresaprimeratransformacion_org_empresarial')

        # Removing M2M table for field alianza on 'EmpresaPrimeraTransformacion'
        db.delete_table('bosques_empresaprimeratransformacion_alianza')

        # Removing M2M table for field organizado on 'EmpresaPrimeraTransformacion'
        db.delete_table('bosques_empresaprimeratransformacion_organizado')

        # Removing M2M table for field area_trabajo on 'EmpresaPrimeraTransformacion'
        db.delete_table('bosques_empresaprimeratransformacion_area_trabajo')

        # Removing M2M table for field servicio_secado on 'EmpresaPrimeraTransformacion'
        db.delete_table('bosques_empresaprimeratransformacion_servicio_secado')

        # Removing M2M table for field productos_venden on 'EmpresaPrimeraTransformacion'
        db.delete_table('bosques_empresaprimeratransformacion_productos_venden')

        # Removing M2M table for field otro_social on 'EmpresaPrimeraTransformacion'
        db.delete_table('bosques_empresaprimeratransformacion_otro_social')

        # Removing M2M table for field otro_ambiental on 'EmpresaPrimeraTransformacion'
        db.delete_table('bosques_empresaprimeratransformacion_otro_ambiental')

        # Deleting model 'VisionEmpresarial'
        db.delete_table('bosques_visionempresarial')

        # Deleting model 'NivelTecnologico'
        db.delete_table('bosques_niveltecnologico')

        # Deleting model 'RegenteForestal'
        db.delete_table('bosques_regenteforestal')

        # Removing M2M table for field organizado on 'RegenteForestal'
        db.delete_table('bosques_regenteforestal_organizado')

        # Removing M2M table for field organizacion on 'RegenteForestal'
        db.delete_table('bosques_regenteforestal_organizacion')

        # Removing M2M table for field area_trabajo on 'RegenteForestal'
        db.delete_table('bosques_regenteforestal_area_trabajo')

        # Deleting model 'AreaTrabajo'
        db.delete_table('bosques_areatrabajo')

        # Deleting model 'DatosSeguimientoRegente'
        db.delete_table('bosques_datosseguimientoregente')

        # Deleting model 'SeguimientoPrimeraTransformacion'
        db.delete_table('bosques_seguimientoprimeratransformacion')


    models = {
        'bosques.alianzanegocio': {
            'Meta': {'object_name': 'AlianzaNegocio'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'bosques.alianzanegocion': {
            'Meta': {'object_name': 'AlianzaNegocion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.ambientales': {
            'Meta': {'object_name': 'Ambientales'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.apoyoproduccion': {
            'Meta': {'object_name': 'ApoyoProduccion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'bosques.areatrabajo': {
            'Meta': {'object_name': 'AreaTrabajo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'bosques.areatrabajosegunda': {
            'Meta': {'object_name': 'AreaTrabajoSegunda'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'bosques.asistenciatecnica': {
            'Meta': {'object_name': 'AsistenciaTecnica'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'bosques.auditor': {
            'Meta': {'object_name': 'Auditor'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.buenaspracticas': {
            'Meta': {'object_name': 'BuenasPracticas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.datos': {
            'Meta': {'object_name': 'Datos'},
            'area_poa': ('django.db.models.fields.FloatField', [], {}),
            'auditor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.Auditor']", 'null': 'True', 'blank': 'True'}),
            'bosque_bajo_manejo': ('django.db.models.fields.FloatField', [], {}),
            'entidad_certificadora': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.EntidadCertificadora']", 'null': 'True', 'blank': 'True'}),
            'estado_certificado': ('django.db.models.fields.IntegerField', [], {}),
            'fecha_seguimiento': ('django.db.models.fields.DateField', [], {}),
            'hombre': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'otros_usos': ('django.db.models.fields.FloatField', [], {}),
            'permiso_poa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'poa_ejecucion': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'registro_orfn': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'segui_plantaciones': ('django.db.models.fields.FloatField', [], {}),
            'sequimiento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.Seguimiento']"}),
            'tipo_certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.TipoCertificacion']", 'symmetrical': 'False'}),
            'uso_agricola': ('django.db.models.fields.FloatField', [], {}),
            'uso_agroforestal': ('django.db.models.fields.FloatField', [], {}),
            'uso_foretal': ('django.db.models.fields.FloatField', [], {}),
            'uso_pecuario': ('django.db.models.fields.FloatField', [], {}),
            'visita_auditoria': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'volumen_cosecha': ('django.db.models.fields.FloatField', [], {})
        },
        'bosques.datosprimeratransforma': {
            'Meta': {'object_name': 'DatosPrimeraTransforma'},
            'asistencia': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.AsistenciaTecnica']"}),
            'codigo_certificacion': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'desde': ('django.db.models.fields.IntegerField', [], {}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.EmpresaComercializadora']"}),
            'entidad_certificadora': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.EntidadCertificadora']", 'null': 'True', 'blank': 'True'}),
            'estado_certificado': ('django.db.models.fields.IntegerField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'hombres': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'p_tranformacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.SeguimientoPrimeraTransformacion']"}),
            'producto_vende': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.ProductoVenden']", 'symmetrical': 'False'}),
            'regente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.RegenteForestal']"}),
            'relacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.RelacionComercial']"}),
            'servicio_extraccion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.ServicioExtraccion']"}),
            'status': ('django.db.models.fields.DateField', [], {}),
            'tipo_certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.TipoCertificacion']", 'symmetrical': 'False'}),
            'volumen_carbon': ('django.db.models.fields.FloatField', [], {}),
            'volumen_lena': ('django.db.models.fields.FloatField', [], {}),
            'volumen_madera_aserrada': ('django.db.models.fields.FloatField', [], {}),
            'volumen_madera_rollo': ('django.db.models.fields.FloatField', [], {})
        },
        'bosques.datosseguimientoregente': {
            'Meta': {'object_name': 'DatosSeguimientoRegente'},
            'area_pgmf': ('django.db.models.fields.FloatField', [], {}),
            'area_total_poa': ('django.db.models.fields.FloatField', [], {}),
            'codigo_pgmf': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'codigo_poa': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'fecha_ingreso': ('django.db.models.fields.DateField', [], {}),
            'fecha_seguimiento': ('django.db.models.fields.DateField', [], {}),
            'fkregente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.SeguimientoRegente']"}),
            'hombre': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'no_pgmf_regencia': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'no_poa_regencia': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'volumenes_totales': ('django.db.models.fields.FloatField', [], {})
        },
        'bosques.datossegundatranformacion': {
            'Meta': {'object_name': 'DatosSegundaTranformacion'},
            'alianza': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.AlianzaNegocio']", 'symmetrical': 'False'}),
            'codigo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'desde_cuando': ('django.db.models.fields.DateField', [], {}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.EmpresaComercializadora']"}),
            'entidad_certificadora': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.EntidadCertificadora']", 'null': 'True', 'blank': 'True'}),
            'estado_certificado': ('django.db.models.fields.IntegerField', [], {}),
            'fecha_status': ('django.db.models.fields.DateField', [], {}),
            'fksegunda': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.SeguimientoSegundaTranformacion']"}),
            'hombres': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mujeres': ('django.db.models.fields.IntegerField', [], {}),
            'proveedores': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.ProveedoresSuministros']", 'symmetrical': 'False'}),
            'relacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.RelacionComercial']"}),
            'servicio_operacionales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.PrestadoresServicioOperacionales']", 'symmetrical': 'False'}),
            'tipo_certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.TipoCertificacion']", 'symmetrical': 'False'}),
            'tipo_producto': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['bosques.TipoProducto']", 'null': 'True', 'blank': 'True'}),
            'volumen_promedio': ('django.db.models.fields.FloatField', [], {})
        },
        'bosques.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.empresacomercializadora': {
            'Meta': {'object_name': 'EmpresaComercializadora'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'bosques.empresaprimeratransformacion': {
            'Meta': {'object_name': 'EmpresaPrimeraTransformacion'},
            'alianza': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.AlianzaNegocio']", 'symmetrical': 'False'}),
            'area_trabajo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.TrabajoTranformacion']", 'symmetrical': 'False'}),
            'capasidad_horno': ('django.db.models.fields.FloatField', [], {}),
            'cedula': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'comunidad': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['lugar.Comunidad']"}),
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'desde': ('django.db.models.fields.DateField', [], {}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.Empresa']"}),
            'encuestador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.Encuestador']"}),
            'fecha_creacion': ('django.db.models.fields.IntegerField', [], {}),
            'fecha_llenado': ('django.db.models.fields.DateField', [], {}),
            'gobierno_gti': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'municipio': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre_corto': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nombre_director': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nombre_empresa_forestal': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nombre_gti': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.GobiernoGti']", 'null': 'True', 'blank': 'True'}),
            'org_empresarial': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.OrganizacionEmpresarial']", 'symmetrical': 'False'}),
            'organizado': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.Organizado']", 'symmetrical': 'False'}),
            'otro_ambiental': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['bosques.Ambientales']", 'null': 'True', 'blank': 'True'}),
            'otro_social': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['bosques.SocialesEconomico']", 'null': 'True', 'blank': 'True'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'productos_venden': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.ProductosVenden']", 'symmetrical': 'False'}),
            'servicio_secado': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.ServicioSecado']", 'symmetrical': 'False'}),
            'tel_celular': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'tel_convencional': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'bosques.empresasegundatransformacion': {
            'Meta': {'object_name': 'EmpresaSegundaTransformacion'},
            'apoyo_produccion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.ApoyoProduccion']", 'symmetrical': 'False'}),
            'area_trabajo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.AreaTrabajoSegunda']", 'symmetrical': 'False'}),
            'cedula': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'comunidad': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['lugar.Comunidad']"}),
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'creacion': ('django.db.models.fields.IntegerField', [], {}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'desde': ('django.db.models.fields.DateField', [], {}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.Empresa']"}),
            'encuestador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.Encuestador']"}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'funcionando': ('django.db.models.fields.IntegerField', [], {}),
            'gobierno_gti': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'madera': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.Madera']", 'null': 'True', 'blank': 'True'}),
            'municipio': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nivel_tecnologico': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.NivelTecnologico']", 'symmetrical': 'False'}),
            'no_maderable': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.NoMaderable']", 'symmetrical': 'False'}),
            'nombre_comercial': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nombre_corto': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'nombre_director': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nombre_gti': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.GobiernoGti']", 'null': 'True', 'blank': 'True'}),
            'org_empresarial': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.OrganizacionEmpresarial']", 'symmetrical': 'False'}),
            'organizado': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.Organizado']", 'symmetrical': 'False'}),
            'otro_ambiental': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['bosques.Ambientales']", 'null': 'True', 'blank': 'True'}),
            'otro_social': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['bosques.SocialesEconomico']", 'null': 'True', 'blank': 'True'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'producto_vende': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.ProductosVendenSegunda']", 'symmetrical': 'False'}),
            'promedio': ('django.db.models.fields.FloatField', [], {}),
            'propia_secado': ('django.db.models.fields.FloatField', [], {}),
            'tel_celular': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'tel_convencional': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'vision_empresarial': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.VisionEmpresarial']", 'symmetrical': 'False'}),
            'volumen_anual': ('django.db.models.fields.FloatField', [], {})
        },
        'bosques.encuestador': {
            'Meta': {'object_name': 'Encuestador'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.entidadcertificadora': {
            'Meta': {'object_name': 'EntidadCertificadora'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.especiesintroducidas': {
            'Meta': {'object_name': 'EspeciesIntroducidas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.especiesnaturales': {
            'Meta': {'object_name': 'EspeciesNaturales'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.gobiernogti': {
            'Meta': {'object_name': 'GobiernoGti'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.madera': {
            'Meta': {'object_name': 'Madera'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.metodoextraccion': {
            'Meta': {'object_name': 'MetodoExtraccion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.niveltecnologico': {
            'Meta': {'object_name': 'NivelTecnologico'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'bosques.nomaderable': {
            'Meta': {'object_name': 'NoMaderable'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'bosques.organizacion': {
            'Meta': {'object_name': 'Organizacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.organizacionempresarial': {
            'Meta': {'object_name': 'OrganizacionEmpresarial'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'bosques.organizacionpublica': {
            'Meta': {'object_name': 'OrganizacionPublica'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'bosques.organizado': {
            'Meta': {'object_name': 'Organizado'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.prestadoresserviciooperacionales': {
            'Meta': {'object_name': 'PrestadoresServicioOperacionales'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.procesoindustrialbosque': {
            'Meta': {'object_name': 'ProcesoIndustrialBosque'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.productosvenden': {
            'Meta': {'object_name': 'ProductosVenden'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.productosvendensegunda': {
            'Meta': {'object_name': 'ProductosVendenSegunda'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'bosques.productovenden': {
            'Meta': {'object_name': 'ProductoVenden'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'bosques.propietariobosques': {
            'Meta': {'unique_together': "(('nombre_propietario',),)", 'object_name': 'PropietarioBosques'},
            'area_certificada': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'area_propiedad': ('django.db.models.fields.FloatField', [], {}),
            'area_umf': ('django.db.models.fields.FloatField', [], {}),
            'bosques_umf': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.TipoBosqueUmf']", 'symmetrical': 'False'}),
            'buenas_practicas': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.BuenasPracticas']", 'symmetrical': 'False'}),
            'cedula_propietario': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'cedula_tecnico': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'codigo_certificado': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'codigo_umf': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'comunidad': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['lugar.Comunidad']"}),
            'consumo': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'coordenadas_umf': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'desde': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.Empresa']"}),
            'encuestador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.Encuestador']"}),
            'extraccion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.MetodoExtraccion']", 'symmetrical': 'False'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'gobierno_gti': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'madera': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.Madera']", 'null': 'True', 'blank': 'True'}),
            'madera_procesada': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'municipio': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'naturales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.EspeciesNaturales']", 'symmetrical': 'False'}),
            'nombre_gti': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.GobiernoGti']", 'null': 'True', 'blank': 'True'}),
            'nombre_propiedad': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nombre_propietario': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nombre_umf': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'organizacion': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['bosques.Organizacion']", 'null': 'True', 'blank': 'True'}),
            'organizado': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.Organizado']", 'symmetrical': 'False'}),
            'otro_ambiental': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['bosques.Ambientales']", 'null': 'True', 'blank': 'True'}),
            'otro_social': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['bosques.SocialesEconomico']", 'null': 'True', 'blank': 'True'}),
            'periodo_vigencia': ('django.db.models.fields.IntegerField', [], {}),
            'poas_umf': ('django.db.models.fields.IntegerField', [], {}),
            'procesos_industriales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.ProcesoIndustrialBosque']", 'symmetrical': 'False'}),
            'producto_no_maderable': ('django.db.models.fields.IntegerField', [], {}),
            'representante_tecnico': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sexo_propietario': ('django.db.models.fields.IntegerField', [], {}),
            'sexo_tecnico': ('django.db.models.fields.IntegerField', [], {}),
            'tecnico_ruc': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tel_celular': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'tel_convencional': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'tipo_certificacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.TipoCertificacion']", 'symmetrical': 'False'}),
            'tipo_producto': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['bosques.TipoProducto']", 'null': 'True', 'blank': 'True'}),
            'tipo_propiedad': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.TipoPropiedadBosque']", 'symmetrical': 'False'}),
            'web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        },
        'bosques.proveedoressuministros': {
            'Meta': {'object_name': 'ProveedoresSuministros'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.regenteforestal': {
            'Meta': {'object_name': 'RegenteForestal'},
            'area_trabajo': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.AreaTrabajo']", 'symmetrical': 'False'}),
            'codigo_regente': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'comunidad': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['lugar.Comunidad']"}),
            'correo': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'desde': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'encuestador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.Encuestador']"}),
            'experiencia': ('django.db.models.fields.IntegerField', [], {}),
            'fecha_acreditacion': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'llenado': ('django.db.models.fields.DateField', [], {}),
            'municipio': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'no_cedula': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'nombre_regente': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'org_publica': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.OrganizacionPublica']"}),
            'organizacion': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['bosques.Organizacion']", 'null': 'True', 'blank': 'True'}),
            'organizado': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.Organizado']", 'symmetrical': 'False'}),
            'pagina_web': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'perfil': ('django.db.models.fields.TextField', [], {}),
            'tel_celular': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'}),
            'tel_convencional': ('django.db.models.fields.CharField', [], {'max_length': '50', 'null': 'True', 'blank': 'True'})
        },
        'bosques.relacioncomercial': {
            'Meta': {'object_name': 'RelacionComercial'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'bosques.seguimiento': {
            'Meta': {'unique_together': "(('propietario',),)", 'object_name': 'Seguimiento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'propietario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.PropietarioBosques']"})
        },
        'bosques.seguimientoprimeratransformacion': {
            'Meta': {'object_name': 'SeguimientoPrimeraTransformacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre_empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.EmpresaPrimeraTransformacion']"})
        },
        'bosques.seguimientoregente': {
            'Meta': {'object_name': 'SeguimientoRegente'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'regente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.RegenteForestal']"})
        },
        'bosques.seguimientosegundatranformacion': {
            'Meta': {'object_name': 'SeguimientoSegundaTranformacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.EmpresaSegundaTransformacion']"})
        },
        'bosques.servicioextraccion': {
            'Meta': {'object_name': 'ServicioExtraccion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'bosques.serviciosecado': {
            'Meta': {'object_name': 'ServicioSecado'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.socialeseconomico': {
            'Meta': {'object_name': 'SocialesEconomico'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.tipobosqueumf': {
            'Meta': {'object_name': 'TipoBosqueUmf'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.tipocertificacion': {
            'Meta': {'object_name': 'TipoCertificacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.tipoproducto': {
            'Meta': {'object_name': 'TipoProducto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.tipopropiedadbosque': {
            'Meta': {'object_name': 'TipoPropiedadBosque'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.tiposecados': {
            'Meta': {'object_name': 'TipoSecados'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.trabajotranformacion': {
            'Meta': {'object_name': 'TrabajoTranformacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.visionempresarial': {
            'Meta': {'object_name': 'VisionEmpresarial'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'lugar.comunidad': {
            'Meta': {'object_name': 'Comunidad'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'municipio': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Municipio']"}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'lugar.departamento': {
            'Meta': {'object_name': 'Departamento'},
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        },
        'lugar.municipio': {
            'Meta': {'ordering': "['departamento__nombre']", 'object_name': 'Municipio'},
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'extension': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '10', 'decimal_places': '2', 'blank': 'True'}),
            'id': ('django.db.models.fields.IntegerField', [], {'primary_key': 'True'}),
            'latitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'longitud': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '8', 'decimal_places': '5', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['bosques']