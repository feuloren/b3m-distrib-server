#-*- coding: utf-8 -*-

from .base import *

class LoginHandler(BaseHandler):
    @returns_json
    def get(self):
        login = self.get_argument('login', None)
        self.set_logged_user(login)
        return True

class LogoutHandler(BaseHandler):
    @returns_json
    @authenticated
    def get(self):
        self.clear_cookie('user')
