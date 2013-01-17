# *-* coding:utf-8
from django.contrib import admin
from models import Blog, Postagem

class BlogAdmin(admin.ModelAdmin):
    #listagem
    list_display  = ['nome','blogueiro','chave',]
    list_per_page = 20
    
class PostagemAdmin(admin.ModelAdmin):
    #listagem
    list_display  = ['titulo','data_publicacao','data_atualizacao',]
    search_fields = ['titulo','sub_titulo','data_publicacao','data_atualizacao','chave','blog',]
    list_filter   = ['data_publicacao',] 
    date_hierarchy = 'data_publicacao'
    ordering = ['-data_atualizacao','-data_publicacao',]
    list_per_page = 20
    #formulario
    fieldsets = [
         ['Post',{'fields':['titulo','texto','resumo','referencia','chave']}],
         ['Blog',{'fields':['blog',]}],
         ['Datas',{'fields':['data_publicacao',]}]
    ]

admin.site.register(Blog,BlogAdmin)
admin.site.register(Postagem,PostagemAdmin)
