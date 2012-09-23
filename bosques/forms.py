# -*- coding: UTF-8 -*-

from django.forms import ModelForm
from models import *
from django import forms
from django.forms.widgets import CheckboxSelectMultiple

class PropietarioBosquesForm(ModelForm):
    tipo_propiedad = forms.ModelMultipleChoiceField(queryset = TipoPropiedadBosque.objects.order_by('nombre'),
                                                    widget = forms.CheckboxSelectMultiple())
    organizado = forms.ModelMultipleChoiceField(queryset = Organizado.objects.order_by('nombre'),
                                                    widget = forms.CheckboxSelectMultiple())
    #organizacion = forms.ModelMultipleChoiceField(queryset = Organizacion.objects.order_by('nombre'),
     #                                             required=False)
    tipo_producto = forms.ModelMultipleChoiceField(queryset = TipoProducto.objects.order_by('nombre'),
                                                    widget = forms.CheckboxSelectMultiple(), required=False)
    procesos_industriales = forms.ModelMultipleChoiceField(queryset = ProcesoIndustrialBosque.objects.order_by('nombre'),
                                                    widget = forms.CheckboxSelectMultiple())
    #secado = forms.ModelMultipleChoiceField(queryset = TipoSecados.objects.order_by('nombre'),
    #                                                widget = forms.CheckboxSelectMultiple())
    buenas_practicas = forms.ModelMultipleChoiceField(queryset = BuenasPracticas.objects.order_by('nombre'),
                                                    widget = forms.CheckboxSelectMultiple())
    #proveedores = forms.ModelMultipleChoiceField(queryset = ProveedoresSuministros.objects.order_by('nombre'),
    #                                                widget = forms.CheckboxSelectMultiple())
    bosques_umf = forms.ModelMultipleChoiceField(queryset = TipoBosqueUmf.objects.order_by('nombre'),
                                                    widget = forms.CheckboxSelectMultiple())
    extraccion = forms.ModelMultipleChoiceField(queryset = MetodoExtraccion.objects.order_by('nombre'),
                                                    widget = forms.CheckboxSelectMultiple())

    # def __init__(self, *args, **kwargs):
    #     super(PropietarioBosquesForm, self).__init__(*args, **kwargs)
    #     rel = ManyToOneRel(self.instance.tipo_producto.model, 'id') 
    #     self.fields['tipo_producto'].widget = RelatedFieldWidgetWrapper(self.fields['tipo_producto'].widget, rel, self.admin_site)
    
    class Meta:
        #widgets = {'tipo_propiedad': forms.CheckboxSelectMultiple}
    	model = PropietarioBosques

SINO_CHOICE = (
    ('', '-----'),
    (1, 'Si'),
    (2, 'No')
)

def get_anios():
    choices = []
    years = []
    for en in PropietarioBosques.objects.all().order_by('year'):
        years.append(en.fecha.year)
    for year in list(set(years)):
        choices.append((year, year))
    return choices

class FiltroBosquesForm(forms.Form):
    fecha = forms.ChoiceField(choices=get_anios(),required=False)
    tipo_propiedad = forms.ModelChoiceField(queryset=TipoPropiedadBosque.objects.all(), 
                                            label=u'Tipo de propiedad',
                                            required=False)
    #area_total = forms.FloatField(label=u'Area total', required=False)
    organizado = forms.ModelChoiceField(queryset=Organizado.objects.all(),
                                        label=u'Organizado', required=False)
    gti = forms.ChoiceField(choices=SINO_CHOICE, label=u'Gobierno GTI', required=False)
    tipo_bosque_umf = forms.ModelChoiceField(queryset=TipoBosqueUmf.objects.all(),
                                             label=u'Tipo de Bosques UMF', required=False)
    tipo_certificacion = forms.ModelChoiceField(queryset=TipoCertificacion.objects.all(),
                                           label=u'Certificación', required=False)

class PrimeraTransformacionForm(forms.Form):
    org_empresarial = forms.ModelChoiceField(queryset=OrganizacionEmpresarial.objects.all(), 
                                            label=u'Organizacion',
                                            required=False)
    gobierno_gti = forms.ChoiceField(choices=SINO_CHOICE, label=u'Gobierno GTI', required=False)
    area_trabajo = forms.ModelChoiceField(queryset=TrabajoTranformacion.objects.all(), 
                                            label=u'Area de Trabajo',
                                            required=False)
    productos_venden = forms.ModelChoiceField(queryset=ProductosVenden.objects.all(), 
                                            label=u'Productos que venden',
                                            required=False)

class SegundaTransformacionForm(forms.Form):
    org_empresarial = forms.ModelChoiceField(queryset=OrganizacionEmpresarial.objects.all(), 
                                            label=u'Organizacion',
                                            required=False)
    gobierno_gti = forms.ChoiceField(choices=SINO_CHOICE, label=u'Gobierno GTI', required=False)
    area_trabajo = forms.ModelChoiceField(queryset=AreaTrabajoSegunda.objects.all(), 
                                            label=u'Area de Trabajo',
                                            required=False)
    producto_vende = forms.ModelChoiceField(queryset=ProductosVendenSegunda.objects.all(), 
                                            label=u'Productos que venden',
                                            required=False)

class RegenteForestalForm(forms.Form):
    organizado = forms.ModelChoiceField(queryset=Organizado.objects.all(), 
                                            label=u'Organizado',
                                            required=False)
    area_trabajo = forms.ModelChoiceField(queryset=AreaTrabajo.objects.all(), 
                                            label=u'Area de Trabajo',
                                            required=False)