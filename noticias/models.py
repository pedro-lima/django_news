# *-* coding:utf-8
from django.db import models
from datetime import datetime
from django.core.validators import MaxLengthValidator
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.dispatch import receiver
from ckeditor.fields import RichTextField
from django.utils.translation import ugettext_lazy as _

class Categoria(models.Model):
    nome = models.CharField(_(u'nome'), max_length=150, unique=True)
    chave = models.SlugField(_(u'palavra chave'), unique=True)

    def __unicode__(self):
        return u'%s' % (self.nome)

    def get_absolute_url(self):
        return reverse('noticias.views.listar_noticias_por_categoria',
            kwargs = {'slug': self.chave}
        )

    class Meta:
        ordering = ['nome']

class Noticia(models.Model):
    titulo = models.CharField(_(u'título'),max_length=255)
    sub_titulo = models.CharField(_(u'subtitulo'), max_length=255)
    data_publicacao = models.DateTimeField(_(u'data de publicação'),default=datetime.now)
    data_atualizacao = models.DateTimeField(_(u'data de atualização'))
    texto = RichTextField(_(u'texto'))
    resumo = models.TextField(_(u'resumo'), validators=[MaxLengthValidator(300)])
    referencia = models.URLField(_(u'referência'), blank=True)
    chave = models.SlugField(_(u'palavra chave'), unique=True)
    categorias = models.ManyToManyField(Categoria,verbose_name=_(u'categorias'))

    def __unicode__(self):
        return u'%s - %s' % (self.titulo, self.sub_titulo)

    def get_absolute_url(self):
        return reverse('noticias.views.buscar_noticia_por_chave',
            kwargs={'slug':self.chave})

    def get_short_date(self):
        return self.data_publicacao.strftime('%d/%m')

    @receiver(pre_save)
    def noticia_pre_save(signal, instance, sender, **kwargs):
        instance.data_atualizacao = datetime.now()

    class Meta:
        ordering = ['-data_publicacao']
        verbose_name = _(u'notícia')
        verbose_name_plural = _(u'notícias')
        get_latest_by = '-data_publicacao'

#class Comentario(models.Model):
#    nome = models.CharField(max_length=250)
#    email = models.EmailField()
#    data = models.DateTimeField()
#    mensagem = models.TextField()
#    aprovado = models.BooleanField()
#    noticia = models.ForeignKey(Noticia)
#
#    def __unicode__(self):
#        return u'%s - %s' % (self.email, self.noticia)
#
#    class Meta:
#        ordering = ['-data']
#        get_latest_by = 'data'
#        verbose_name = 'comentário'
#        verbose_name_plural = 'comentários'

class Video(models.Model):
    titulo = models.CharField(_(u'título'), max_length=150)
    url = models.URLField(_(u'link do vídeo'))
    noticia = models.OneToOneField(Noticia)

    def __unicode__(self):
        return u'%s' % (self.titulo)

    class Meta:
        verbose_name = _(u'vídeo')
        verbose_name_plural = _(u'vídeos')


#Imagens
