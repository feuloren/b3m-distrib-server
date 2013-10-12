# -*- coding:utf-8 -*-

from .base import *
from ..models import *
from datetime import datetime

class CommandeGetInfos(BaseHandler):
    @returns_json
    @authenticated
    def get(self, barcode):
        if len(barcode) != 10:
            raise ServerException("Code-barre invalide")

        id = barcode[4:]
        commande = self.db.query(Commande).get(id)
        if commande is None:
            raise ServerException("Cette commande n'existe pas")
        else:
            # tests divers et variéés
            return commande.info_summary

class CommandeRetirer(BaseHandler):
    @returns_json
    @authenticated
    def get(self, id):
        commande = self.db.query(Commande).get(id)
        if commande.date_retrait is None:
            commande.login_retrait = self.current_user
            commande.date_retrait = datetime.today()
            self.db.commit()
            return True
        else:
            raise ServerException("Commande déjà retirée")
