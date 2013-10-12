#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os.path

import json

from sqlalchemy.orm import scoped_session, sessionmaker
from .models import *  # import the engine to bind

from . import settings as app_settings

where_am_i = os.path.dirname(__file__)

def import_listing(file_path):
    pass
