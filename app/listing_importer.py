#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os.path

import json
from datetime import datetime

from sqlalchemy.orm import scoped_session, sessionmaker
from .models import *  # import the engine to bind

from . import settings as app_settings

where_am_i = os.path.dirname(__file__)

# create a configured "Session" class
Session = sessionmaker(bind=engine)
    
def import_listing(file_path):
    # create a Session
    session = Session()
    
    try:
        fichier = open(file_path, 'r')
    except IOError as e:
        print "- ERREUR : Impossible d'ouvrir le listing des commandes -"
        print e
        return

    try:
        data = json.loads(fichier.read())
    except ValueError as e:
        print "- ERREUR : Impossible de parser le listing des commandes -"
        print e
        return

    billetterie = data['billetterie']
    print "- Import de la billetterie", billetterie, " -"

    for tarif in data['tarifs']:
        t = Tarif(id = tarif['id'],
            billetterie_id = billetterie,
            nom = tarif['nom'],
            code_article = tarif['code_article'],
            nom_article = tarif['nom_article']
            )
        session.add(t)

    def parse_date(date):
        if date:
            return datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
        else:
            return None

    for commande in data['commandes']:
        c = Commande(id = commande['id'],
                     tarif_id = commande['tarif'],
                     barcode = commande['barcode'],
                     nom = commande['nom'],
                     prenom = commande['prenom'],
                     mail = commande['mail'],
                     date_commande = parse_date(commande['date_commande']),
                     date_paiement = parse_date(commande['date_paiement']),
                     date_retrait = parse_date(commande['date_retrait'])
                     )
        session.add(c)

    session.commit()

def import_consignes(file_path):
    # create a Session
    session = Session()
    
    try:
        fichier = open(file_path, 'r')
    except IOError as e:
        print "- ERREUR : Impossible d'ouvrir le listing des consignes -"
        print e
        return

    try:
        data = json.loads(fichier.read())
    except ValueError as e:
        print "- ERREUR : Impossible de parser le listing des consignes -"
        print e
        return

    for consigne in data['consignes']:
        c = Consigne(nom = consigne['nom'],
                     tarif = int(consigne['tarif'])
                     )
        session.add(c)

    session.commit()
