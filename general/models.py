import re
from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactMessage(models.Model):
    ''' Classe que representa uma mensagem de contato '''

    name = models.CharField(_("Nome"), max_length=44, null=False, blank=False)
    email = models.CharField(
        _("E-mail"), max_length=255, null=False, blank=False)
    coordenadoria = models.CharField(
        _("Coordenadoria"), max_length=255, null=True, blank=True)
    phone = models.CharField(
        _("Telefone"), max_length=13, null=True, blank=True)
    message = models.TextField(_("Mensagem"), null=False, blank=False)
    register_datetime = models.DateTimeField(
        _("Data de registro"), auto_now=True)

    def __str__(self):
        return '{} - {}...'.format(self.name, self.message[:20])

    def save(self, *args, **kwargs):
        self.format_phone()
        return super(ContactMessage, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('mensagem de contato')
        verbose_name_plural = _('mensagens de contato')

    def format_phone(self):
        '''
        Retorna phone sem formatação (somente números)
        :return: phone
        '''
        if self.phone:
            self.phone = re.sub('[()/-/+]', '', self.phone)
            self.phone = self.phone.replace(" ", "")
            self.phone = self.phone[-11:]
