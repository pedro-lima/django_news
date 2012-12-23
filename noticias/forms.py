# *-* coding:utf-8
from django import forms

class BuscaForm(forms.Form):
    termo = forms.CharField(max_length=200,label=u'Busca')

    clean_termo(self):
        msg = self.cleaned_data['termo']
        if len(msg) < 5:
            raise. forms.ValidationError('Palavra pequena')
        return msg

#class ComentarioForm(forms.Form):
#    nome = forms.CharField()
#    email = forms.CharField()
#    mensagem = forms.CharField()
#    noticia = forms.CharField(widget=forms.HiddenInput)
