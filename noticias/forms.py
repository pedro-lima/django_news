# *-* coding:utf-8
from django import forms

TOPICOS_COMENTARIOS = (('1','Elogio'),('2','Sugestão'),('3','Reclamação'))

class ContatoForm(forms.Form):
    assunto = forms.CharField()
    nome = forms.CharField()
    email = forms.EmailField(required=False)
    mensagem = forms.CharField(widget=forms.Textarea)
    tipo = forms.ChoiceField(widget=forms.Select, choices=TOPICOS_COMENTARIOS)

class BuscaForm(forms.Form):
    termo = forms.CharField()

#class ComentarioForm(forms.Form):
#    nome = forms.CharField()
#    email = forms.CharField()
#    mensagem = forms.CharField(widget=forms.Textarea)
#    noticia = forms.CharField(widget=forms.HiddenInput)
