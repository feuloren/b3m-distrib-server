#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import os
import optparse
from app.configure import interactive_config, update

parser = optparse.OptionParser()
parser.add_option('-d', '--debug', dest='debug', default=False, action='store_true', help=u'Lancement en mode debug')
parser.add_option('-k', '--keep', dest='keep', default=False, action='store_true', help=u"Garder les données déjà présentes")
parser.add_option('-D', '--do', dest='action', nargs=1, action='store', default=False, help=u'Action à effectuer (pour le déploiement et la maintenance)')
parser.add_option('-l', '--listing', dest='listing', nargs=1, action='store', default=False, help=u'Emplacement du fichier de listing')
parser.add_option('-c', '--consignes', dest='consignes', nargs=1, action='store', default=False, help=u'Emplacement du fichier de consignes')

options, args = parser.parse_args()

try:
    os.environ['VIRTUAL_ENV']
except KeyError:
    print """############
## Attention
## Vous n'êtes pas dans le virtualenv,
## référez vous au fichier README.md pour plus d'informations
############"""

try:
    import app.settings
except ImportError:
    print "- Configuration de l'application -"
    interactive_config()
    import app.settings

if not app.settings.up_to_date():
    print "- Mise à jour du fichier de paramètres -"
    update()
    reload(app.settings)

if options.action:
    action = options.action
    if action == 'create_tables':
        from app import models
        print "= Création des tables ="
        models.metadata.create_all(models.engine)
        print "= Succès "

    elif action == 'drop_tables':
        from app import models
        print "= Suppression des tables ="
        models.metadata.drop_all(models.engine)
        print "= Succès ="

    elif action == 'configure':
        print "= Configuration interactive ="
        interactive_config()

    elif action == 'export-retraits':
        print "= Liste des commandes retirées ="
        from app import export
        for id in export.get_commandes_retirees():
            print id, ',',

    else:
        print "Action invalide"
    
else:
    if not(options.listing):
        print "Merci d'indiquer l'emplacement du fichier listing avec l'option --listing"
        exit()

    if not(options.keep):
        from app import models
        print "= Configuration de la base de données ="
        models.metadata.drop_all(models.engine)
        print "- Destruction terminée -"
        models.metadata.create_all(models.engine)
        print "- Création terminée -\n"

        from app import listing_importer
        print "= Import du fichier listing ="
        listing_importer.import_listing(options.listing)
        print "- import Terminé -\n"

        if options.consignes:
            print "= Import du fichier des consignes ="
            listing_importer.import_consignes(options.consignes)
            print "- Import terminé -\n"

    from app import server
    print "= Lancement du serveur ="
    if options.debug:
        print "- Mode Débug -"
    server.run(options.debug)
