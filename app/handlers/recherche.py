# -*- coding:utf-8 -*-

from .base import *
from ..models import Tarif, Commande

class RechercheHandler(BaseHandler):
    @returns_json
    @authenticated
    def get(self):
        term = self.get_argument('q', None)
        if term is None:
            return None
        else:
            results = self.db.query(Commande).filter(Commande.nom.like('%'+term+'%') | Commande.prenom.like('%'+term+'%') | Commande.mail.like('%'+term+'%')).limit(20)
            return (commande.info_summary for commande in results)
