#!/usr/bin/env python
# -*- coding:utf-8 -*-

from os import urandom
from hashlib import sha256

# Liste des paramètres de l'application :
# Il peuvent être autogénéres (ex: cookie_secret)
# ou demandés à l'utilisateur
liste = [
    dict(name='cookie_secret', gen=(lambda : sha256(urandom(24)).hexdigest())),
    dict(name='db_path', desc="Chemin d'accès à la base de données", 
     default="db.sqlite"),
    dict(name='static_url', desc="Url d'accès aux fichiers statiques",
     default="/static/"),
    dict(name='port', desc="Port sur lequel écouter les requêtes",
         default="8080"),
]

