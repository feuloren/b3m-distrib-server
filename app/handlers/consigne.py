# -*- coding:utf-8 -*-

from .base import *
from ..models import *
from datetime import datetime

class ConsigneListe(BaseHandler):
    @returns_json
    def get(self):
        commandes = self.db.query(Consigne)
        return {'consignes' : (commande.info_summary for commande in commandes)}

class ConsigneRendre(BaseHandler):
    @returns_json
    def get(self, id):
        commande = self.db.query(Commande).get(id)
        if not(commande.date_retrait is None):
            nombre = int(self.get_argument('consignes'))
            consigne = ConsigneRendue(commande = commande,
                                      nombre = nombre,
                                      date = datetime.today())
            self.db.add(consigne)
            self.db.commit()
            return {'success' : True}
        else:
            raise ServerException("La commande n'est pas retirée !")
