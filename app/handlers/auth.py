#-*- coding: utf-8 -*-

from .base import *

class LoginHandler(BaseHandler):
    @returns_json
    def get(self):
        login = self.get_argument('login', None)
        print "Logging as :", login
        self.set_logged_user(login)
        return {'success' : True}

class LogoutHandler(BaseHandler):
    @returns_json
    @authenticated
    def get(self):
        self.clear_cookie('user')
        return {}
