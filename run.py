#!/usr/bin/env python
# encoding: utf8

from werkzeug.middleware.dispatcher import DispatcherMiddleware
from spyne.server.wsgi import WsgiApplication

from apps import spyned, admin
from apps.flasked import app


# Os serviços SOAP são aplicativos wsgi distintos, 
# devemos usar middleware de dispatcher para reunir todos os aps
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, mounts={
    '/soap': WsgiApplication(spyned.create_app(app)),
    '/admin': WsgiApplication(admin.create_app(app))
    })


if __name__ == '__main__':
    app.run()
