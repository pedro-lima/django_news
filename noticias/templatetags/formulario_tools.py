from django import template
from noticias.forms import BuscaForm

register = template.Library()

class ExibirFormularioBuscaNode(template.Node):
    def __init__(self):
        pass
    
    def render(self,context):  
        context['formulario_busca'] = BuscaForm()
        return ''

@register.tag
def exibir_formulario_busca(parser,token):
    return ExibirFormularioBuscaNode()
    
