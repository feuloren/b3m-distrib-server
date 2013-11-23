# -*- coding:utf-8 -*-

from .base import *
from ..models import Tarif, Commande

class RechercheHandler(BaseHandler):
    @returns_json
    def get(self):
        term = self.get_argument('q', None)
        if term is None:
            return {'commandes' : None}
        else:
            results = self.db.query(Commande).\
                join(Commande.tarif).\
                filter(Commande.nom.like('%'+term+'%') | Commande.prenom.like('%'+term+'%') | Commande.mail.like('%'+term+'%')).\
                limit(20)
            return {'commandes' : (commande.info_summary for commande in results)}
