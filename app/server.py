#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os.path

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.httpclient
from tornado.options import define, options

from sqlalchemy.orm import scoped_session, sessionmaker
from .models import *  # import the engine to bind

from . import settings as app_settings
from .routing import routes

where_am_i = os.path.dirname(__file__)

class Application(tornado.web.Application):
    def __init__(self, debug):
        settings = {
            'cookie_secret': app_settings.cookie_secret,
            "template_path": os.path.join(where_am_i, "..", "templates"),
            "static_path": os.path.join(where_am_i, "..", "static"),
            "debug": debug,
            "static_url": app_settings.static_url,
            "login_url":"/login",
            }
        tornado.web.Application.__init__(self, routes, **settings)
        # Have one global connection.
        self.db = scoped_session(sessionmaker(bind=engine))

def run(debug=False):
    http_server = tornado.httpserver.HTTPServer(Application(debug))
    http_server.listen(int(app_settings.port))
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    run()
