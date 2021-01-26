from django import forms
from .models import encriptarMod,descriptarMod

class encriptarFor (forms.ModelForm):
    class Meta:
        model = encriptarMod
        fields=('__all__')

class descriptarFor(forms.ModelForm):
    class Meta:
        model=descriptarMod
        fields=('__all__')