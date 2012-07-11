# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Encuestador'
        db.create_table('bosques_encuestador', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bosques', ['Encuestador'])

        # Adding model 'Empresa'
        db.create_table('bosques_empresa', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bosques', ['Empresa'])

        # Adding model 'TipoPropiedadBosque'
        db.create_table('bosques_tipopropiedadbosque', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bosques', ['TipoPropiedadBosque'])

        # Adding model 'Organizado'
        db.create_table('bosques_organizado', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bosques', ['Organizado'])

        # Adding model 'Organizacion'
        db.create_table('bosques_organizacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bosques', ['Organizacion'])

        # Adding model 'GobiernoGti'
        db.create_table('bosques_gobiernogti', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bosques', ['GobiernoGti'])

        # Adding model 'EspeciesNaturales'
        db.create_table('bosques_especiesnaturales', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bosques', ['EspeciesNaturales'])

        # Adding model 'EspeciesIntroducidas'
        db.create_table('bosques_especiesintroducidas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bosques', ['EspeciesIntroducidas'])

        # Adding model 'Madera'
        db.create_table('bosques_madera', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bosques', ['Madera'])

        # Adding model 'TipoProducto'
        db.create_table('bosques_tipoproducto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bosques', ['TipoProducto'])

        # Adding model 'ProcesoIndustrialBosque'
        db.create_table('bosques_procesoindustrialbosque', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bosques', ['ProcesoIndustrialBosque'])

        # Adding model 'TipoSecados'
        db.create_table('bosques_tiposecados', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bosques', ['TipoSecados'])

        # Adding model 'BuenasPracticas'
        db.create_table('bosques_buenaspracticas', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bosques', ['BuenasPracticas'])

        # Adding model 'ProveedoresSuministros'
        db.create_table('bosques_proveedoressuministros', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bosques', ['ProveedoresSuministros'])

        # Adding model 'TipoBosqueUmf'
        db.create_table('bosques_tipobosqueumf', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bosques', ['TipoBosqueUmf'])

        # Adding model 'MetodoExtraccion'
        db.create_table('bosques_metodoextraccion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bosques', ['MetodoExtraccion'])

        # Adding model 'PropietarioBosques'
        db.create_table('bosques_propietariobosques', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha', self.gf('django.db.models.fields.DateField')()),
            ('encuestador', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.Encuestador'])),
            ('empresa', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.Empresa'])),
            ('nombre_propietario', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('sexo_propietario', self.gf('django.db.models.fields.IntegerField')()),
            ('cedula_propietario', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('propietario_ruc', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('representante_tecnico', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('sexo_tecnico', self.gf('django.db.models.fields.IntegerField')()),
            ('cedula_tecnico', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('tecnico_ruc', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('nombre_propiedad', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('registro_catastral', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('area_propiedad', self.gf('django.db.models.fields.FloatField')()),
            ('tel_convencional', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('tel_celular', self.gf('django.db.models.fields.CharField')(max_length=15, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('web', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('direccion', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('latitud', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('longitud', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('departamento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lugar.Departamento'])),
            ('municipio', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['lugar.Municipio'])),
            ('comunidad', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['lugar.Comunidad'])),
            ('desde', self.gf('django.db.models.fields.DateField')()),
            ('gobierno_gti', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre_gti', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.GobiernoGti'], null=True, blank=True)),
            ('madera', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.Madera'], null=True, blank=True)),
            ('madera_procesada', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('consumo', self.gf('django.db.models.fields.IntegerField')(null=True, blank=True)),
            ('producto_no_maderable', self.gf('django.db.models.fields.IntegerField')()),
            ('nombre_umf', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('area_umf', self.gf('django.db.models.fields.FloatField')()),
            ('codigo_umf', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('periodo_vigencia', self.gf('django.db.models.fields.IntegerField')()),
            ('poas_umf', self.gf('django.db.models.fields.IntegerField')()),
            ('secado_horno', self.gf('django.db.models.fields.FloatField')()),
            ('codigo_certificado', self.gf('django.db.models.fields.CharField')(max_length=200, null=True, blank=True)),
            ('area_certificada', self.gf('django.db.models.fields.FloatField')(null=True, blank=True)),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal('bosques', ['PropietarioBosques'])

        # Adding M2M table for field tipo_propiedad on 'PropietarioBosques'
        db.create_table('bosques_propietariobosques_tipo_propiedad', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('propietariobosques', models.ForeignKey(orm['bosques.propietariobosques'], null=False)),
            ('tipopropiedadbosque', models.ForeignKey(orm['bosques.tipopropiedadbosque'], null=False))
        ))
        db.create_unique('bosques_propietariobosques_tipo_propiedad', ['propietariobosques_id', 'tipopropiedadbosque_id'])

        # Adding M2M table for field organizado on 'PropietarioBosques'
        db.create_table('bosques_propietariobosques_organizado', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('propietariobosques', models.ForeignKey(orm['bosques.propietariobosques'], null=False)),
            ('organizado', models.ForeignKey(orm['bosques.organizado'], null=False))
        ))
        db.create_unique('bosques_propietariobosques_organizado', ['propietariobosques_id', 'organizado_id'])

        # Adding M2M table for field organizacion on 'PropietarioBosques'
        db.create_table('bosques_propietariobosques_organizacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('propietariobosques', models.ForeignKey(orm['bosques.propietariobosques'], null=False)),
            ('organizacion', models.ForeignKey(orm['bosques.organizacion'], null=False))
        ))
        db.create_unique('bosques_propietariobosques_organizacion', ['propietariobosques_id', 'organizacion_id'])

        # Adding M2M table for field naturales on 'PropietarioBosques'
        db.create_table('bosques_propietariobosques_naturales', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('propietariobosques', models.ForeignKey(orm['bosques.propietariobosques'], null=False)),
            ('especiesnaturales', models.ForeignKey(orm['bosques.especiesnaturales'], null=False))
        ))
        db.create_unique('bosques_propietariobosques_naturales', ['propietariobosques_id', 'especiesnaturales_id'])

        # Adding M2M table for field introducida on 'PropietarioBosques'
        db.create_table('bosques_propietariobosques_introducida', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('propietariobosques', models.ForeignKey(orm['bosques.propietariobosques'], null=False)),
            ('especiesintroducidas', models.ForeignKey(orm['bosques.especiesintroducidas'], null=False))
        ))
        db.create_unique('bosques_propietariobosques_introducida', ['propietariobosques_id', 'especiesintroducidas_id'])

        # Adding M2M table for field tipo_producto on 'PropietarioBosques'
        db.create_table('bosques_propietariobosques_tipo_producto', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('propietariobosques', models.ForeignKey(orm['bosques.propietariobosques'], null=False)),
            ('tipoproducto', models.ForeignKey(orm['bosques.tipoproducto'], null=False))
        ))
        db.create_unique('bosques_propietariobosques_tipo_producto', ['propietariobosques_id', 'tipoproducto_id'])

        # Adding M2M table for field procesos_industriales on 'PropietarioBosques'
        db.create_table('bosques_propietariobosques_procesos_industriales', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('propietariobosques', models.ForeignKey(orm['bosques.propietariobosques'], null=False)),
            ('procesoindustrialbosque', models.ForeignKey(orm['bosques.procesoindustrialbosque'], null=False))
        ))
        db.create_unique('bosques_propietariobosques_procesos_industriales', ['propietariobosques_id', 'procesoindustrialbosque_id'])

        # Adding M2M table for field secado on 'PropietarioBosques'
        db.create_table('bosques_propietariobosques_secado', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('propietariobosques', models.ForeignKey(orm['bosques.propietariobosques'], null=False)),
            ('tiposecados', models.ForeignKey(orm['bosques.tiposecados'], null=False))
        ))
        db.create_unique('bosques_propietariobosques_secado', ['propietariobosques_id', 'tiposecados_id'])

        # Adding M2M table for field buenas_practicas on 'PropietarioBosques'
        db.create_table('bosques_propietariobosques_buenas_practicas', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('propietariobosques', models.ForeignKey(orm['bosques.propietariobosques'], null=False)),
            ('buenaspracticas', models.ForeignKey(orm['bosques.buenaspracticas'], null=False))
        ))
        db.create_unique('bosques_propietariobosques_buenas_practicas', ['propietariobosques_id', 'buenaspracticas_id'])

        # Adding M2M table for field proveedores on 'PropietarioBosques'
        db.create_table('bosques_propietariobosques_proveedores', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('propietariobosques', models.ForeignKey(orm['bosques.propietariobosques'], null=False)),
            ('proveedoressuministros', models.ForeignKey(orm['bosques.proveedoressuministros'], null=False))
        ))
        db.create_unique('bosques_propietariobosques_proveedores', ['propietariobosques_id', 'proveedoressuministros_id'])

        # Adding M2M table for field bosques_umf on 'PropietarioBosques'
        db.create_table('bosques_propietariobosques_bosques_umf', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('propietariobosques', models.ForeignKey(orm['bosques.propietariobosques'], null=False)),
            ('tipobosqueumf', models.ForeignKey(orm['bosques.tipobosqueumf'], null=False))
        ))
        db.create_unique('bosques_propietariobosques_bosques_umf', ['propietariobosques_id', 'tipobosqueumf_id'])

        # Adding M2M table for field extraccion on 'PropietarioBosques'
        db.create_table('bosques_propietariobosques_extraccion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('propietariobosques', models.ForeignKey(orm['bosques.propietariobosques'], null=False)),
            ('metodoextraccion', models.ForeignKey(orm['bosques.metodoextraccion'], null=False))
        ))
        db.create_unique('bosques_propietariobosques_extraccion', ['propietariobosques_id', 'metodoextraccion_id'])

        # Adding model 'Seguimiento'
        db.create_table('bosques_seguimiento', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('propietario', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.PropietarioBosques'])),
        ))
        db.send_create_signal('bosques', ['Seguimiento'])

        # Adding model 'TipoCertificacion'
        db.create_table('bosques_tipocertificacion', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal('bosques', ['TipoCertificacion'])

        # Adding model 'Datos'
        db.create_table('bosques_datos', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fecha_seguimiento', self.gf('django.db.models.fields.DateField')()),
            ('hombre', self.gf('django.db.models.fields.IntegerField')()),
            ('mujeres', self.gf('django.db.models.fields.IntegerField')()),
            ('uso_agricola', self.gf('django.db.models.fields.FloatField')()),
            ('uso_pecuario', self.gf('django.db.models.fields.FloatField')()),
            ('uso_foretal', self.gf('django.db.models.fields.FloatField')()),
            ('bosque_bajo_manejo', self.gf('django.db.models.fields.FloatField')()),
            ('uso_agroforestal', self.gf('django.db.models.fields.FloatField')()),
            ('otros_usos', self.gf('django.db.models.fields.FloatField')()),
            ('poa_ejecucion', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('area_poa', self.gf('django.db.models.fields.FloatField')()),
            ('permiso_poa', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('volumen_cosecha', self.gf('django.db.models.fields.FloatField')()),
            ('segui_plantaciones', self.gf('django.db.models.fields.FloatField')()),
            ('registro_orfn', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('certificado', self.gf('django.db.models.fields.IntegerField')()),
            ('estado_certificado', self.gf('django.db.models.fields.IntegerField')()),
            ('sequimiento', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['bosques.Seguimiento'])),
        ))
        db.send_create_signal('bosques', ['Datos'])

        # Adding M2M table for field tipo_certificacion on 'Datos'
        db.create_table('bosques_datos_tipo_certificacion', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('datos', models.ForeignKey(orm['bosques.datos'], null=False)),
            ('tipocertificacion', models.ForeignKey(orm['bosques.tipocertificacion'], null=False))
        ))
        db.create_unique('bosques_datos_tipo_certificacion', ['datos_id', 'tipocertificacion_id'])

    def backwards(self, orm):
        # Deleting model 'Encuestador'
        db.delete_table('bosques_encuestador')

        # Deleting model 'Empresa'
        db.delete_table('bosques_empresa')

        # Deleting model 'TipoPropiedadBosque'
        db.delete_table('bosques_tipopropiedadbosque')

        # Deleting model 'Organizado'
        db.delete_table('bosques_organizado')

        # Deleting model 'Organizacion'
        db.delete_table('bosques_organizacion')

        # Deleting model 'GobiernoGti'
        db.delete_table('bosques_gobiernogti')

        # Deleting model 'EspeciesNaturales'
        db.delete_table('bosques_especiesnaturales')

        # Deleting model 'EspeciesIntroducidas'
        db.delete_table('bosques_especiesintroducidas')

        # Deleting model 'Madera'
        db.delete_table('bosques_madera')

        # Deleting model 'TipoProducto'
        db.delete_table('bosques_tipoproducto')

        # Deleting model 'ProcesoIndustrialBosque'
        db.delete_table('bosques_procesoindustrialbosque')

        # Deleting model 'TipoSecados'
        db.delete_table('bosques_tiposecados')

        # Deleting model 'BuenasPracticas'
        db.delete_table('bosques_buenaspracticas')

        # Deleting model 'ProveedoresSuministros'
        db.delete_table('bosques_proveedoressuministros')

        # Deleting model 'TipoBosqueUmf'
        db.delete_table('bosques_tipobosqueumf')

        # Deleting model 'MetodoExtraccion'
        db.delete_table('bosques_metodoextraccion')

        # Deleting model 'PropietarioBosques'
        db.delete_table('bosques_propietariobosques')

        # Removing M2M table for field tipo_propiedad on 'PropietarioBosques'
        db.delete_table('bosques_propietariobosques_tipo_propiedad')

        # Removing M2M table for field organizado on 'PropietarioBosques'
        db.delete_table('bosques_propietariobosques_organizado')

        # Removing M2M table for field organizacion on 'PropietarioBosques'
        db.delete_table('bosques_propietariobosques_organizacion')

        # Removing M2M table for field naturales on 'PropietarioBosques'
        db.delete_table('bosques_propietariobosques_naturales')

        # Removing M2M table for field introducida on 'PropietarioBosques'
        db.delete_table('bosques_propietariobosques_introducida')

        # Removing M2M table for field tipo_producto on 'PropietarioBosques'
        db.delete_table('bosques_propietariobosques_tipo_producto')

        # Removing M2M table for field procesos_industriales on 'PropietarioBosques'
        db.delete_table('bosques_propietariobosques_procesos_industriales')

        # Removing M2M table for field secado on 'PropietarioBosques'
        db.delete_table('bosques_propietariobosques_secado')

        # Removing M2M table for field buenas_practicas on 'PropietarioBosques'
        db.delete_table('bosques_propietariobosques_buenas_practicas')

        # Removing M2M table for field proveedores on 'PropietarioBosques'
        db.delete_table('bosques_propietariobosques_proveedores')

        # Removing M2M table for field bosques_umf on 'PropietarioBosques'
        db.delete_table('bosques_propietariobosques_bosques_umf')

        # Removing M2M table for field extraccion on 'PropietarioBosques'
        db.delete_table('bosques_propietariobosques_extraccion')

        # Deleting model 'Seguimiento'
        db.delete_table('bosques_seguimiento')

        # Deleting model 'TipoCertificacion'
        db.delete_table('bosques_tipocertificacion')

        # Deleting model 'Datos'
        db.delete_table('bosques_datos')

        # Removing M2M table for field tipo_certificacion on 'Datos'
        db.delete_table('bosques_datos_tipo_certificacion')

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
            'Meta': {'object_name': 'PropietarioBosques'},
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
            'departamento': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lugar.Departamento']"}),
            'desde': ('django.db.models.fields.DateField', [], {}),
            'direccion': ('django.db.models.fields.CharField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'empresa': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.Empresa']"}),
            'encuestador': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['bosques.Encuestador']"}),
            'extraccion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.MetodoExtraccion']", 'symmetrical': 'False'}),
            'fecha': ('django.db.models.fields.DateField', [], {}),
            'gobierno_gti': ('django.db.models.fields.IntegerField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'introducida': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.EspeciesIntroducidas']", 'symmetrical': 'False'}),
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
            'organizacion': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.Organizacion']", 'symmetrical': 'False'}),
            'organizado': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.Organizado']", 'symmetrical': 'False'}),
            'periodo_vigencia': ('django.db.models.fields.IntegerField', [], {}),
            'poas_umf': ('django.db.models.fields.IntegerField', [], {}),
            'procesos_industriales': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.ProcesoIndustrialBosque']", 'symmetrical': 'False'}),
            'producto_no_maderable': ('django.db.models.fields.IntegerField', [], {}),
            'propietario_ruc': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'proveedores': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.ProveedoresSuministros']", 'symmetrical': 'False'}),
            'registro_catastral': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'representante_tecnico': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'secado': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['bosques.TipoSecados']", 'symmetrical': 'False'}),
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
            'Meta': {'object_name': 'Seguimiento'},
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