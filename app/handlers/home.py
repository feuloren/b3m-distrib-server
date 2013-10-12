#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .base import *

class HomeHandler(BaseHandler):
    @returns_json
    @authenticated
    def get(self):
        return 'welcome '+self.current_user
