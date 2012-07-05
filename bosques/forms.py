# -*- coding: UTF-8 -*-

from django.forms import ModelForm
from models import *
from django import forms
from django.forms.widgets import CheckboxSelectMultiple

class PropietarioBosquesForm(ModelForm):
    #tipo_propiedad = forms.ModelMultipleChoiceField(queryset = TipoPropiedadBosque.objects.order_by('nombre'),
    #                                      widget = forms.CheckboxSelectMultiple())
    class Meta:
        widgets = {'tipo_propiedad': forms.CheckboxSelectMultiple}
    	model = PropietarioBosques
