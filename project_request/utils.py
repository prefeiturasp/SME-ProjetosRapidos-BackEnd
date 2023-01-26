import sys
from django.conf import settings
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import render_to_string


def send_email_new_request_message():
    html_template = 'simple_message.html'
    dict = {
        'subject': '[Projetos Rápidos] Novo cadastro',
        'subtitle': 'Um novo cadastro da frente de Projetos Rápidos foi realizado. Acesse www.projetosrapidos.sme.prefeitura.sp.gov.br/admin para visualizá-lo.',
    }
    try:
        context = Context(dict)
        content = render_to_string(html_template, {'context': context})
        send_email = EmailMessage(dict['subject'], content, settings.DEFAULT_FROM_EMAIL, [
                                  settings.DEFAULT_TO_EMAIL])
        send_email.content_subtype = 'html'
        send_email.send()
    except:
        print('erro send_email_new_request_message', sys.exc_info()[0])
        raise
