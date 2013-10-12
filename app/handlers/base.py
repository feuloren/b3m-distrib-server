# -*- coding:utf-8 -*-

import tornado.web
import json
import types
from datetime import datetime

class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
        return self.application.db

    def get_current_user(self):
        self.current_user = self.get_secure_cookie("user", None)
        return self.current_user

    def static_url(self, filename):
        """On stocke nos fichiers statiques sous un autre domaine.
        et on n'a pas besoin du versionnage des fichiers"""
        self.require_setting("static_url")
        
        return self.application.settings["static_url"] + filename

    def set_logged_user(self, login):
        if login:
            self.set_secure_cookie('user', str(login))

class ServerException(Exception):
    pass

class CompleteEncoder(json.JSONEncoder):
    """Un encodeur json plus complet qui permet de gérer les générateur et les
       datetime
    """

    def default(self, o):
        if isinstance(o, types.GeneratorType):
            return list(o)
        elif isinstance(o, datetime):
            return o.strftime("%Y-%m-%d %H:%M:%S")
        return json.JSONEncoder.default(self, o)

def returns_json(func):
    def wrapper(self, *args, **kwargs):
        try:
            result = func(self, *args, **kwargs)
        except ServerException as e:
            result = {'erreur' : {'type' : e.__class__.__name__,
                                  'message' : e.message}}
        self.write(json.dumps(result, cls=CompleteEncoder))

    return wrapper

def authenticated(func):
    def wrapper(self, *args, **kwargs):
        if not self.current_user:
            raise tornado.web.HTTPError(403)
        return func(self, *args, **kwargs)

    return wrapper
