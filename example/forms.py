from .models import Arvore
from django import forms

class ArvoreModelForm(forms.ModelForm):
    class Meta:
        model = Arvore
        fields = '__all__'