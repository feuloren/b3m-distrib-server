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
    __tablename__ = 'tarif'
    id = Column(Integer, primary_key=True)
    billetterie_id = Column(Integer, nullable=False)
    nom = Column(String(300), nullable=True)
    nom_article = Column(String(300), nullable=False)
    code_article = Column(Integer, nullable=False)

class Commande(Base):
    __tablename__ = 'commande'
    id = Column(Integer, primary_key=True)
    tarif_id = Column(Integer, ForeignKey('tarif.id'), nullable=False)
    barcode = Column(String(10), nullable=False)
    nom = Column(String(300), nullable=False)
    prenom = Column(String(300), nullable=False)
    mail = Column(String(300), nullable=False)
    date_commande = Column(DateTime, nullable=True)
    date_paiement = Column(DateTime, nullable=True)
    date_retrait = Column(DateTime, nullable=True)
    login_retrait = Column(String(20))

    tarif = relationship("Tarif", backref=backref('commandes', order_by=id))

    @property
    def info_summary(self):
        return {'id' : self.id,
                'nom' : self.nom,
                'prenom' : self.prenom,
                'mail' : self.mail,
                'date_commande' : self.date_commande,
                'date_paiement' : self.date_paiement,
                'date_retrait' : self.date_retrait,
                'nom_tarif' : self.tarif.nom}

class Consigne(Base):
    __tablename__ = 'consigne'
    id = Column(Integer, primary_key=True)
    nom = Column(String(40), nullable=False)
    tarif = Column(Integer(4), nullable=False)

    @property
    def info_summary(self):
        return {'id' : self.id,
                'nom' : self.nom,
                'tarif' : self.tarif}

class ConsigneRendue(Base):
    __tablename__ = 'consigne_rendue'
    id = Column(Integer, primary_key=True)
    commande_id = Column(Integer, ForeignKey('commande.id'), nullable=False)
    nombre = Column(Integer, nullable=False)
    date = Column(DateTime, nullable=False)

    commande = relationship("Commande", backref=backref('consignes_rendues', order_by=id))

metadata = Base.metadata

def create_all():
    metadata.create_all(engine)
