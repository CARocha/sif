# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ProVendenBosque'
        db.create_table('bosques_provendenbosque', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bosques', ['ProVendenBosque'])

        # Adding field 'PropietarioBosques.primera_transformacion'
        db.add_column('bosques_propietariobosques', 'primera_transformacion',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.EmpresaPrimeraTransformacion'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'PropietarioBosques.regente'
        db.add_column('bosques_propietariobosques', 'regente',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.RegenteForestal'], null=True, blank=True),
                      keep_default=False)

        # Adding M2M table for field producto_venden on 'PropietarioBosques'
        db.create_table('bosques_propietariobosques_producto_venden', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('propietariobosques', models.ForeignKey(orm['bosques.propietariobosques'], null=False)),
            ('provendenbosque', models.ForeignKey(orm['bosques.provendenbosque'], null=False))
        ))
        db.create_unique('bosques_propietariobosques_producto_venden', ['propietariobosques_id', 'provendenbosque_id'])

        # Deleting field 'DatosSegundaTranformacion.empresa'
        db.delete_column('bosques_datossegundatranformacion', 'empresa_id')


    def backwards(self, orm):
        # Deleting model 'ProVendenBosque'
        db.delete_table('bosques_provendenbosque')

        # Deleting field 'PropietarioBosques.primera_transformacion'
        db.delete_column('bosques_propietariobosques', 'primera_transformacion_id')

        # Deleting field 'PropietarioBosques.regente'
        db.delete_column('bosques_propietariobosques', 'regente_id')

        # Removing M2M table for field producto_venden on 'PropietarioBosques'
        db.delete_table('bosques_propietariobosques_producto_venden')

        # Adding field 'DatosSegundaTranformacion.empresa'
        db.add_column('bosques_datossegundatranformacion', 'empresa',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['bosques.EmpresaComercializadora']),
                      keep_default=False)


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
            'entidad_certificadora': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.EntidadCertificadora']", 'null': 'True', 'blank': 'True'}),
            'estado_certificado': ('django.db.models.fields.IntegerField', [], {}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
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
            'primera_transformacion': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.EmpresaPrimeraTransformacion']", 'null': 'True', 'blank': 'True'}),
            'procesos_industriales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.ProcesoIndustrialBosque']", 'symmetrical': 'False'}),
            'producto_no_maderable': ('django.db.models.fields.IntegerField', [], {}),
            'producto_venden': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['bosques.ProVendenBosque']", 'null': 'True', 'blank': 'True'}),
            'regente': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.RegenteForestal']", 'null': 'True', 'blank': 'True'}),
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
        'bosques.provendenbosque': {
            'Meta': {'object_name': 'ProVendenBosque'},
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