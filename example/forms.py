from django import forms

from .models import Arvore


class ArvoreModelForm(forms.ModelForm):
    class Meta:
        model = Arvore
        exclude = ('is_deleted',)
