from django.conf import settings
from config.utils import email_utils


def send_email_new_request_message_admin():
    dict = {
        'subject': '[Projetos Rápidos] Novo cadastro',
        'title': 'Olá!',
        'subtitle': '''Um novo cadastro da frente de Projetos Rápidos foi realizado.
                       Acesse www.projetosrapidos.sme.prefeitura.sp.gov.br/admin para visualizá-lo.'''
    }
    email_utils.send_email_ctrl(
        '[Projetos Rápidos] Novo cadastro',
        dict,
        'simple_message.html',
        settings.DEFAULT_TO_EMAIL
    )


def send_email_new_request_message(data):
    list_info = """
        <ul>
            <li><strong>Data de registro</strong> {}</li>
            <li><strong>Nome</strong> {}</li>
            <li><strong>E-mail</strong> {}</li>
            <li><strong>Telefone</strong> {}</li>
            <li><strong>Coordenadoria</strong> {}</li>
            <li><strong>Nome do responsável</strong> {}</li>
            <hr>
            <li><strong>Qual sua necessidade de desenvolvimento de portais/sistemas?</strong> {}</li>
            <li><strong>O sistema resolverá</strong> {}</li>
            <li><strong>Qual a data aproximada que o produto precisa estar pronto para uso?</strong> {}</li>
            <li><strong>Quem serão os principais usuários deste produto digital?</strong> {}</li>
            <li><strong>Quantas pessoas você estima que utilizarão este sistema/portal?</strong> {}</li>            
            <li><strong>Elenque as ações que os usuários realizarão neste sistema/portal</strong> {}</li>            
            <li><strong>Existem fatores externos que continuam impactando o usuário, apesar da construção de um sistema/portal, como burocracias ou outros sistemas? Em caso afirmativo, explique melhor</strong> {}</li>            
            <li><strong>Quais funcionalidades você entende que o sistema deve disponibilizar?</strong> {}</li>            
        </ul>
    """.format(data.register_datetime.strftime('%d/%m/%y %H:%M'), data.name, data.email, data.phone, data.coordenadoria, data.responsible_name,
               data.demand, data.demand_type, data.approx_release_date.strftime('%d/%m/%y'), data.target_users, data.approx_quantity_users,
               data.users_actions, data.external_factors, data.functionalities)

    dict = {
        'subject': '[Projetos Rápidos] Novo cadastro',
        'title': 'Olá, {}!'.format(data.name),
        'subtitle': 'Sua solicitação foi registrada com sucesso.',
        'body': list_info
    }
    email_utils.send_email_ctrl(
        '[Projetos Rápidos] Novo cadastro',
        dict,
        'simple_message.html',
        data.email
    )
