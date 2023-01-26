import sys
from django.template.loader import render_to_string
from django.template import Context
from django.core.mail import EmailMessage
from django.conf import settings


def send_email_new_contact_message(data):
    html_template = 'simple_message.html'

    phone = "-" if data.phone is None else data.phone
    coordenadoria = "-" if data.coordenadoria is None else data.coordenadoria

    list_info = """
        <ul style="margin:0;padding:0">
            <li><strong>Nome</strong> {}</li>
            <li><strong>E-mail</strong> {}</li>
            <li><strong>Telefone</strong> {}</li>
            <li><strong>Coordenadoria</strong> {}</li>
            <li><strong>Mensagem</strong> {}</li>
        </ul>
    """.format(data.name, data.email, phone, coordenadoria, data.message)

    dict = {
        'subject': '[Projetos Rápidos] Nova mensagem',
        'subtitle': 'Você recebeu uma nova mensagem pelo formulário de contato:',
        'body': list_info
    }
    try:
        context = Context(dict)
        content = render_to_string(html_template, {'context': context})
        send_email = EmailMessage(dict['subject'], content, settings.DEFAULT_FROM_EMAIL, [
                                  settings.DEFAULT_TO_EMAIL])
        send_email.content_subtype = 'html'
        send_email.send()
    except:
        print('erro send_email_new_contact_message', sys.exc_info()[0])
        raise
