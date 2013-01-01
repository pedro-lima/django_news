# *-* coding:utf-8
from django.contrib  import admin
from noticias.models import Categoria, Noticia,  Video

class CategoriaAdmin(admin.ModelAdmin):
    #listagem
    list_display = ['nome','chave',]
    search_fields = ['nome','chave',]
    list_per_page = 20

class VideoInline(admin.TabularInline):
    model = Video

class NoticiaAdmin(admin.ModelAdmin):
    #listagem
    list_display = ['titulo','data_publicacao','data_atualizacao','chave']
    search_fields = ['titulo','sub_titulo','data_publicacao','data_atualizacao','chave','categorias']
    list_filter = ['data_publicacao',]
    date_hierarchy = 'data_publicacao'
    ordering = ['-data_atualizacao','-data_publicacao',]
    list_per_page = 20
    #formulario
    filter_horizontal = ['categorias',]
    inlines = [VideoInline,]
    fieldsets = [
         ['Noticia',{'fields':['titulo','sub_titulo','texto','resumo','referencia','chave']}],
         ['Categorias',{'fields':['categorias',]}],
         ['Datas',{'fields':['data_publicacao',]}]
    ]

# News's models
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Noticia,NoticiaAdmin)
