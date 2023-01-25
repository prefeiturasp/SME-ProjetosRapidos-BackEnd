from general.email import send_email_support


def send_email_new_request_message():
    message = """
        <body class="bg-light">
        <div class="container">
            <img class="ax-center my-10 w-24" src="https://assets.bootstrapemail.com/logos/light/square.png" />
            <div class="card p-6 p-lg-10 space-y-4">
            <h1 class="h3 fw-700">
                Simple Card
            </h1>
            <p>
                Here is a very simple card. It has responsive padding so it gets less padding on mobile to fill the screen more.
                Hopefully it can be useful to you. It is very simple and basic but can be used for a lot of simple emails.
            </p>
            <a class="btn btn-primary p-3 fw-700" href="https://app.bootstrapemail.com/templates">Visit Website</a>
            </div>
            <img class="ax-center mt-10 w-40" src="https://assets.bootstrapemail.com/logos/light/text.png" />
            <div class="text-muted text-center my-6">
            Sent with <3 from Hip Corp. <br>
            Hip Corp. 1 Hip Street<br>
            Gnarly State, 01234 USA <br>
            </div>
        </div>
        </body>
    """
    send_email_support(
        "[Projetos Rápidos] Nova mensagem",
        message,
        recipient_list=["idscotic@sme.prefeitura.sp.gov.br"]
    )
    #
    # Olá,

    # Você recebeu uma nova mensagem pelo formulário de contato:

    # *|DADOS CADASTRADOS NA MENSAGEM - CRITÉRIO 1.2|*

    # Obrigado
