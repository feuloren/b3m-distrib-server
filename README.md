Serveur pour la distribution de paniers B3M
================================

Permet de partager les données entre les smartphones sans passer par internet

Dépendances
-----------

Python2, Tornado, SqlAlchemy et SQlite

Installation
------------

Vous pouvez utilisez le script bootstrap_fexchange.py pour créer un virtualenv et installer les librairies python nécessaires.
Sous ubuntu il faut au préalable installer python-virtualenv

Pour créer le virtualenv
```
python bootstrap_b3m_server.py
```

Pour activer le virtualenv
```
source activate
```

Pour en sortir
```
deactivate
```

Il peut être utile de mettre à jour le virtualenv après avoir fait un pull
```
python update_virtualenv.py
```

Lancement
---------

```
./b3m-server
```

Il est possible de configurer le serveur grâce à l'option --do
Voici les actions disponibles pour le moment
 * configure : Crée le fichier de configuration settings.py

L'option -d ou --debug passe l'application en mode debug :
 * Le serveur est relancé si un fichier python est modifié

