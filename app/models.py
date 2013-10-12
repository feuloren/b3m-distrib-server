#!/usr/bin/env python
# -*- coding:utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, Boolean, Text, ForeignKey, Enum, Numeric, Date
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.hybrid import hybrid_property

import settings as app_settings

url = 'sqlite:///' + app_settings.db_path
engine = create_engine(url, echo=False)

Base = declarative_base()

class Tarif(Base):
    __tablename__ = 'tarifs'
    id = Column(Integer, primary_key=True)
    billetterie = Column(Integer, nullable=False)
    nom = Column(String(300), nullable=True)
    nom_article = Column(String(300), nullable=False)
    code_article = Column(Integer, nullable=False)

class Commande(Base):
    __tablename__ = 'commandes'
    id = Column(Integer, primary_key=True)
    tarif = Column(Integer, ForeignKey('tarifs.id'), nullable=False)
    barcode = Column(String(10), nullable=False)
    nom = Column(String(300), nullable=False)
    prenom = Column(String(300), nullable=False)
    mail = Column(String(300), nullable=False)
    date_commande = Column(DateTime, nullable=True)
    date_paiement = Column(DateTime, nullable=True)
    date_retrait = Column(DateTime, nullable=True)
    login_retrait = Column(String(20))

    @property
    def info_summary(self):
        return {'id' : self.id,
                'nom' : self.nom,
                'prenom' : self.prenom,
                'mail' : self.mail,
                'date_commande' : self.date_commande,
                'date_paiement' : self.date_paiement,
                'date_retrait' : self.date_retrait}

metadata = Base.metadata

def create_all():
    metadata.create_all(engine)
