# *-* coding:utf-8
from django import forms
from models import Categoria, Noticia


class BuscaForm(forms.Form):
    termo = forms.CharField(max_length=100,label='',)

    termo.widget.attrs['size'] = '32'
    termo.widget.attrs['class'] = 'text'
    termo.error_messages = {'required': 'O termo da pesquisa deve ser informado'}

    def clean_termo(self):
        msg = self.cleaned_data['termo'].strip()
        if(msg==''):
            raise forms.ValidationError("O termo da pesquisa deve ser informado")
        if len(msg) < 3:
            raise forms.ValidationError("O termo informado deve ter pelo menos 3 caracteres")
        return msg

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria

class NoticiaForm(forms.ModelForm):
    class Meta:
        model = Noticia
