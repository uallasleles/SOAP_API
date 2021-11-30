# encoding: utf8

from spyne import Iterable, Integer, Unicode, rpc, Application, Service
from spyne.protocol.http import HttpRpc
from spyne.protocol.json import JsonDocument
from spyne.protocol.html import HtmlColumnTable


class HelloWorldService(Service):
    @rpc(Unicode, Integer, _returns=Iterable(Unicode))
    def hello(ctx, name, times):
        name = name or ctx.udc.config['HELLO']
        for i in range(times):
            yield u'Hello, %s' % name


class UserDefinedContext(object):
    def __init__(self, flask_config):
        self.config = flask_config


def create_app(flask_app):
    """Cria o aplicativo de serviços SOAP e distribui a configuração do Flask 
    no contexto definido pelo usuário para cada chamada de método.
    """
    application = Application(
        [HelloWorldService], 'spyne.examples.flask',
        # O protocolo de entrada é definido como HttpRpc para tornar nosso serviço fácil de chamar.
        in_protocol=HttpRpc(validator='soft'),
        out_protocol=HtmlColumnTable(ignore_wrappers=True),
    )

    # Use o gancho `method_call` para passar a configuração do frasco para cada contexto de método de serviço. 
    # Mas se você tiver alguma ideia melhor, faça uma solicitação de pull.
    # NOTA. Recuso a ideia de envolver cada chamada no contexto do aplicativo Flask 
    # porque, na verdade, estamos dentro do contexto do aplicativo Spyne, não no Flask.
    def _flask_config_context(ctx):
        ctx.udc = UserDefinedContext(flask_app.config)
    application.event_manager.add_listener('method_call', _flask_config_context)

    return application
