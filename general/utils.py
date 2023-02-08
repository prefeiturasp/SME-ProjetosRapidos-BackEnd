from django.conf import settings
from config.utils import email_utils


def send_email_new_contact_message(data):
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
        'title': 'Olá!',
        'subtitle': 'Você recebeu uma nova mensagem pelo formulário de contato:',
        'body': list_info
    }
    email_utils.send_email_ctrl(
        '[Projetos Rápidos] Nova mensagem',
        dict,
        'simple_message.html',
        settings.DEFAULT_TO_EMAIL
    )
