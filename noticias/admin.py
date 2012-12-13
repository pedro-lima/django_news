# *-* coding:utf-8
from django.contrib  import admin
from noticias.models import Categoria, Regiao, Reporter, Noticia, Comentario, Video

class CategoriaAdmin(admin.ModelAdmin):
    #listagem
    list_display = ['nome','chave',]
    search_fields = ['nome','chave',]
    list_per_page = 20

class RegiaoAdmin(admin.ModelAdmin):
    #listagem
    list_display = ['nome','chave',]
    search_fields = ['nome','chave',]
    list_per_page = 20

class ReporterAdmin(admin.ModelAdmin):
    #listagem
    list_display = ['nome','sobrenome','email',]
    search_fields = ['nome','sobrenome','email',]
    list_per_page = 20

class VideoInline(admin.TabularInline):
    model = Video

class NoticiaAdmin(admin.ModelAdmin):
    #listagem
    list_display = ['titulo','data_publicacao','data_atualizacao','chave','regiao','reporter']
    search_fields = ['titulo','sub_titulo','data_publicacao','data_atualizacao','chave','regiao','categorias','reporter']
    list_filter = ['data_publicacao',]
    date_hierarchy = 'data_publicacao'
    ordering = ['-data_atualizacao','-data_publicacao',]
    list_per_page = 20
    #formulario
    filter_horizontal = ['categorias',]
    inlines = [VideoInline,]
    fieldsets = [
         ['Noticia',{'fields':['titulo','sub_titulo','texto','referencia','chave']}],
         ['Região',{'fields':['regiao',]}],
         ['Categorias',{'fields':['categorias',]}],
         ['Reporter',{'fields':['reporter',]}],
         ['Datas',{'fields':['data_publicacao','data_atualizacao',]}]
    ]

# News's models
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Regiao,RegiaoAdmin)
admin.site.register(Reporter,ReporterAdmin)
admin.site.register(Noticia,NoticiaAdmin)
admin.site.register(Comentario)
