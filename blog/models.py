# *-* coding:utf-8
from django.db import models
from django.core.urlresolvers import reverse
from django.core.validators import MaxLengthValidator
from django.db.models.signals import pre_save
from django.dispatch import receiver
from datetime import datetime
from django.utils.translation import ugettext_lazy as _

class Blog(models.Model):
    nome = models.CharField(_('nome'), max_length=150, help_text=_('O nome do blog'))
    blogueiro = models.CharField(_('blogueiro'), max_length=250, help_text=('O nome do blogueiro'))
    chave = models.SlugField(_('palavra chave'), unique=True)
    email = models.EmailField(_('e-mail'), blank=True)

    def __unicode__(self):
        return u'%s' % (self.nome)

    def get_absolute_url(self):
        return reverse('blog.views.listar_postagens_por_blog',
            kwargs = {'slug': self.chave})

    class Meta:
        ordering = ['nome']

class Postagem(models.Model):
    titulo = models.CharField(_('titulo'), max_length=150)
    texto = models.TextField(_('texto'))
    resumo = models.TextField(validators=[MaxLengthValidator(300)])
    data_publicacao = models.DateTimeField(_('data de publicação'),default=datetime.now)
    data_atualizacao = models.DateTimeField(_('data de atualização'))
    referencia = models.URLField(_('referência'), blank=True)
    chave = models.SlugField(_('palavra chave'), unique=True)
    blog = models.ForeignKey(Blog)

    def __unicode__(self):
        return u'%s' % (self.titulo)

    def get_absolute_url(self):
        return reverse('blog.views.buscar_postagem_por_chave',
            kwargs = {'slug': self.chave})

    @receiver(pre_save)
    def blog_pre_save(signal, instance, sender, **kwargs):
        instance.data_atualizacao = datetime.now()

    class Meta:
        ordering = ['-data_publicacao']
        verbose_name =  _('Post')
        verbose_name_plural = _('Posts')
        get_latest_by = '-data_publicacao'
