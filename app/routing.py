# -*- coding:utf-8 -*-

from tornado.web import URLSpec as route
from handlers import *

routes = [
    route(r"/", HomeHandler),
    route(r"/recherche", RechercheHandler),
    # Créer un article, il faut être authentifié
    route(r"/commande/infos/(\d+)", CommandeGetInfos),
    route(r"/commande/retirer/(\d+)", CommandeRetirer),
    route(r"/login", LoginHandler),
    route(r"/logout", LogoutHandler),
    route(r"/consignes/liste", ConsigneListe),
    route(r"/consignes/rendre/(\d+)", ConsigneRendre),
]
