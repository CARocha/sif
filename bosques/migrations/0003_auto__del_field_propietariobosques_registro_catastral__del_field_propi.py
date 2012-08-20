# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'PropietarioBosques.registro_catastral'
        db.delete_column('bosques_propietariobosques', 'registro_catastral')

        # Deleting field 'PropietarioBosques.propietario_ruc'
        db.delete_column('bosques_propietariobosques', 'propietario_ruc')

        # Adding field 'PropietarioBosques.coordenadas_umf'
        db.add_column('bosques_propietariobosques', 'coordenadas_umf',
                      self.gf('django.db.models.fields.TextField')(null=True, blank=True),
                      keep_default=False)

        # Removing M2M table for field secado on 'PropietarioBosques'
        db.delete_table('bosques_propietariobosques_secado')

        # Removing M2M table for field proveedores on 'PropietarioBosques'
        db.delete_table('bosques_propietariobosques_proveedores')

        # Removing M2M table for field introducida on 'PropietarioBosques'
        db.delete_table('bosques_propietariobosques_introducida')

        # Adding unique constraint on 'PropietarioBosques', fields ['nombre_propietario']
        db.create_unique('bosques_propietariobosques', ['nombre_propietario'])

        # Adding unique constraint on 'Seguimiento', fields ['propietario']
        db.create_unique('bosques_seguimiento', ['propietario_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Seguimiento', fields ['propietario']
        db.delete_unique('bosques_seguimiento', ['propietario_id'])

        # Removing unique constraint on 'PropietarioBosques', fields ['nombre_propietario']
        db.delete_unique('bosques_propietariobosques', ['nombre_propietario'])

        # Adding field 'PropietarioBosques.registro_catastral'
        db.add_column('bosques_propietariobosques', 'registro_catastral',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=200),
                      keep_default=False)

        # Adding field 'PropietarioBosques.propietario_ruc'
        db.add_column('bosques_propietariobosques', 'propietario_ruc',
                      self.gf('django.db.models.fields.CharField')(default=None, max_length=200),
                      keep_default=False)

        # Deleting field 'PropietarioBosques.coordenadas_umf'
        db.delete_column('bosques_propietariobosques', 'coordenadas_umf')

        # Adding M2M table for field secado on 'PropietarioBosques'
        db.create_table('bosques_propietariobosques_secado', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('propietariobosques', models.ForeignKey(orm['bosques.propietariobosques'], null=False)),
            ('tiposecados', models.ForeignKey(orm['bosques.tiposecados'], null=False))
        ))
        db.create_unique('bosques_propietariobosques_secado', ['propietariobosques_id', 'tiposecados_id'])

        # Adding M2M table for field proveedores on 'PropietarioBosques'
        db.create_table('bosques_propietariobosques_proveedores', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('propietariobosques', models.ForeignKey(orm['bosques.propietariobosques'], null=False)),
            ('proveedoressuministros', models.ForeignKey(orm['bosques.proveedoressuministros'], null=False))
        ))
        db.create_unique('bosques_propietariobosques_proveedores', ['propietariobosques_id', 'proveedoressuministros_id'])

        # Adding M2M table for field introducida on 'PropietarioBosques'
        db.create_table('bosques_propietariobosques_introducida', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('propietariobosques', models.ForeignKey(orm['bosques.propietariobosques'], null=False)),
            ('especiesintroducidas', models.ForeignKey(orm['bosques.especiesintroducidas'], null=False))
        ))
        db.create_unique('bosques_propietariobosques_introducida', ['propietariobosques_id', 'especiesintroducidas_id'])


    models = {
        'bosques.buenaspracticas': {
            'Meta': {'object_name': 'BuenasPracticas'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.datos': {
            'Meta': {'object_name': 'Datos'},
            'area_poa': ('django.db.models.fields.FloatField', [], {}),
            'bosque_bajo_manejo': ('django.db.models.fields.FloatField', [], {}),
            'certificado': ('django.db.models.fields.IntegerField', [], {}),
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
            'volumen_cosecha': ('django.db.models.fields.FloatField', [], {})
        },
        'bosques.empresa': {
            'Meta': {'object_name': 'Empresa'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.encuestador': {
            'Meta': {'object_name': 'Encuestador'},
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
        'bosques.organizacion': {
            'Meta': {'object_name': 'Organizacion'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.organizado': {
            'Meta': {'object_name': 'Organizado'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        },
        'bosques.procesoindustrialbosque': {
            'Meta': {'object_name': 'ProcesoIndustrialBosque'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
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
            'periodo_vigencia': ('django.db.models.fields.IntegerField', [], {}),
            'poas_umf': ('django.db.models.fields.IntegerField', [], {}),
            'procesos_industriales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.ProcesoIndustrialBosque']", 'symmetrical': 'False'}),
            'producto_no_maderable': ('django.db.models.fields.IntegerField', [], {}),
            'representante_tecnico': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'secado_horno': ('django.db.models.fields.FloatField', [], {}),
            'sexo_propietario': ('django.db.models.fields.IntegerField', [], {}),
            'sexo_tecnico': ('django.db.models.fields.IntegerField', [], {}),
            'tecnico_ruc': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'tel_celular': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
            'tel_convencional': ('django.db.models.fields.CharField', [], {'max_length': '15', 'null': 'True', 'blank': 'True'}),
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
        'bosques.seguimiento': {
            'Meta': {'unique_together': "(('propietario',),)", 'object_name': 'Seguimiento'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'propietario': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.PropietarioBosques']"})
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