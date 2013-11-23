# -*- coding : utf-8 -*-

from .models import *

Session = sessionmaker(bind=engine)

def get_commandes_retirees():
    session = Session()
    commandes = session.query(Commande).filter(Commande.date_retrait != None)
    return (commande.id for commande in commandes)

