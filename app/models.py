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
#Session = sessionmaker(bind=engine)
#session = Session()
Base = declarative_base()

class Utilisateur(Base):
    __tablename__ = 'utilisateurs'
    id = Column(Integer, primary_key=True)
    login = Column(String(10), nullable=True)
    prenom = Column(String(30), nullable=False)
    nom = Column(String(30), nullable=False)
    email = Column(String(100), nullable=False)
    mdp = Column(String(128), nullable=False) #sha512
    offres = relationship("Offre", order_by="Offre.id", backref="offre")

utilisateurs_table = Utilisateur.__table__

metadata = Base.metadata

def create_all():
    metadata.create_all(engine)
