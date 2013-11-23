#!/usr/bin/env python
# -*- coding:utf-8 -*-

from .base import *

class HomeHandler(BaseHandler):
    @returns_json
    def get(self):
        return {'hello':'world'}
