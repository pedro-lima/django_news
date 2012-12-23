from django import forms
from django.core.mail import send_mail

class FormContato(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    mensagem = forms.CharField(widget=forms.Textarea)

    def enviar(self):
        titulo = 'Mensagem enviada pelo site'
        destino = 'pedro_jampa86@yahoo.com.br'
        texto = """
        Nome: %(nome)s
        E-mail: %(email)s
        Mensagem:
        %(mensagem)s
        """ % self.cleaned_data

        send_mail(
            subject=titulo,
            message=texto,
            from_email=destino,
            recipient_list=[destino],
            )
