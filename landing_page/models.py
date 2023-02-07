from datetime import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _


class Section(models.Model):
    ''' Classe que representa uma seção da landing page '''

    tag_id = models.CharField(
        _("tag id"), max_length=255, null=False, blank=False)
    title = models.TextField(_("título"), null=False, blank=False)
    body = models.TextField(_("corpo"), null=True, blank=True)
    img = models.ImageField(
        _("imagem"), upload_to='landing_page/', blank=True, null=True)
    creation_datetime = models.DateTimeField(
        _("data de criação"), auto_now=True)
    edition_datetime = models.DateTimeField(
        _("última atualização"), null=True, blank=True)

    class Meta:
        verbose_name = _('seção')
        verbose_name_plural = _('seções')

    def __str__(self):
        return self.tag_id

    def save(self, *args, **kwargs):
        self.edition_datetime = datetime.now()

        return super(Section, self).save(*args, **kwargs)
