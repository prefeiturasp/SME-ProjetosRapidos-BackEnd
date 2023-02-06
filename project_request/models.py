import pytz
import re
from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

local_timezone = pytz.timezone(settings.TIME_ZONE)


class ProjectRequest(models.Model):
    ''' Classe que representa uma solicitação de projeto '''

    # dados do contratante
    name = models.CharField(_("Nome"), max_length=44, null=False, blank=False)
    email = models.CharField(
        _("E-mail"), max_length=255, null=False, blank=False)
    phone = models.CharField(
        _("Telefone"), max_length=13, null=True, blank=True)
    responsible_name = models.CharField(
        _("Nome do responsável"), max_length=44, null=False, blank=False)
    coordenadoria = models.CharField(
        _("Coordenadoria"), max_length=255, null=True, blank=True)

    # entedimento da demanda
    demand = models.TextField(_("Sobre a demanda"), null=False, blank=False)
    demand_type = models.CharField(
        _("Tipo de demanda"), max_length=255, null=False, blank=False)
    approx_release_date = models.DateTimeField(
        _("Data aproximada de lançamento"), auto_now=True)
    target_users = models.CharField(
        _("Principais usuários"), max_length=255, null=False, blank=False)
    approx_quantity_users = models.PositiveIntegerField(
        _("Quantidade aproximada de usuários"), null=False, blank=False)
    users_actions = models.TextField(
        _("Ações do sistema"), null=False, blank=False)
    external_factors = models.TextField(
        _("Fatores externos que continuam impactando o usuário"), null=False, blank=False)
    functionalities = models.TextField(
        _("Funcionalidades"), null=False, blank=False)

    register_datetime = models.DateTimeField(
        _("Data de registro"), auto_now=True)

    def __str__(self):
        return '{} - {}...'.format(self.name, self.demand_type[:20])

    def save(self, *args, **kwargs):
        self.format_phone()
        return super(ProjectRequest, self).save(*args, **kwargs)

    class Meta:
        verbose_name = _('solicitação de projeto')
        verbose_name_plural = _('solicitações de projeto')

    def format_phone(self):
        '''
        Retorna phone sem formatação (somente números)
        :return: phone
        '''
        if self.phone:
            self.phone = re.sub('[()/-/+]', '', self.phone)
            self.phone = self.phone.replace(" ", "")
            self.phone = self.phone[-11:]
