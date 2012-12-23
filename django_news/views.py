# Create your views here.

from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import FormContato

def enviar_mensagem(request):
    if request.method == "GET":
        form = FormContato()
        return render_to_response('contato.html', locals(),
            context_instance=RequestContext(request),)
    else:
        form = FormContato(request.POST)
        if form.is_valid():
            form.enviar()
            sucesso = True
        return render_to_response('contato.html', locals(),context_instance=RequestContext(request),)
