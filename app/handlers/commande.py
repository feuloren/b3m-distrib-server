# -*- coding:utf-8 -*-

from .base import *
from ..models import *
from datetime import datetime

class CommandeGetInfos(BaseHandler):
    @returns_json
    def get(self, barcode):
        if len(barcode) != 10:
            raise ServerException("Code-barre invalide")

        commande = self.db.query(Commande).\
            filter_by(barcode=barcode).\
            join(Commande.tarif).first()
        if commande is None:
            raise ServerException("Cette commande n'existe pas")
        else:
            # tests divers et variéés
            return commande.info_summary

class CommandeRetirer(BaseHandler):
    @returns_json
    @authenticated
    def get(self, id):
        login = self.get_argument('login') # pas besoin de vérifier car on utilise @authenticated
        commande = self.db.query(Commande).get(id)
        if commande.date_retrait is None:
            commande.login_retrait = login
            commande.date_retrait = datetime.today()
            self.db.commit()
            return {'success' : True}
        else:
            raise ServerException("Commande déjà retirée")
