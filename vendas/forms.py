from django import forms
from .models import *


class VendaForm(forms.ModelForm):
    class Meta:
        model = Venda
        fields = ['nome', 'valor', 'numero_venda', 'observacao', 'comprovante_venda', 'exemplo_upload',
                  'produtos', 'cliente']