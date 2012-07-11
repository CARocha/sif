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
    organizacion = forms.ModelMultipleChoiceField(queryset = Organizacion.objects.order_by('nombre'),
                                                    widget = forms.CheckboxSelectMultiple())
    tipo_producto = forms.ModelMultipleChoiceField(queryset = TipoProducto.objects.order_by('nombre'),
                                                    widget = forms.CheckboxSelectMultiple(), required=False)
    procesos_industriales = forms.ModelMultipleChoiceField(queryset = ProcesoIndustrialBosque.objects.order_by('nombre'),
                                                    widget = forms.CheckboxSelectMultiple())
    secado = forms.ModelMultipleChoiceField(queryset = TipoSecados.objects.order_by('nombre'),
                                                    widget = forms.CheckboxSelectMultiple())
    buenas_practicas = forms.ModelMultipleChoiceField(queryset = BuenasPracticas.objects.order_by('nombre'),
                                                    widget = forms.CheckboxSelectMultiple())
    proveedores = forms.ModelMultipleChoiceField(queryset = ProveedoresSuministros.objects.order_by('nombre'),
                                                    widget = forms.CheckboxSelectMultiple())
    bosques_umf = forms.ModelMultipleChoiceField(queryset = TipoBosqueUmf.objects.order_by('nombre'),
                                                    widget = forms.CheckboxSelectMultiple())
    extraccion = forms.ModelMultipleChoiceField(queryset = MetodoExtraccion.objects.order_by('nombre'),
                                                    widget = forms.CheckboxSelectMultiple())
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
    fecha = forms.ChoiceField(choices=get_anios())
    tipo_propiedad = forms.ModelChoiceField(queryset=TipoPropiedadBosque.objects.all(), 
                                            label=u'Tipo de propiedad',
                                            required=False)
    #area_total = forms.FloatField(label=u'Area total', required=False)
    organizado = forms.ModelChoiceField(queryset=Organizado.objects.all(),
                                        label=u'Organizado', required=False)
    gti = forms.ChoiceField(choices=SINO_CHOICE, label=u'Gobierno GTI', required=False)
    tipo_bosque_umf = forms.ModelChoiceField(queryset=TipoBosqueUmf.objects.all(),
                                             label=u'Tipo de Bosques UMF', required=False)
    #certificacion = forms.ModelChoiceField(queryset=TipoCertificacion.objects.all(),
    #                                       label=u'Certificación', required=False)