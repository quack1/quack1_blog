Title: Piloter un daemon P2P Transmission à distance
Date: 2013-08-06 13:48 
Author: Quack1
Category: Geek
Tags: Transmission, Linux, P2P, Serveur
Slug: transmission_server_remote
Summary: Si vous avez, sur une de vos machines, un &laquo;daemon&raquo; Transmission pour télécharger vos images ISO GNU/Linux, vous pouvez lancer vos téléchargements via l'interface Web de gestion logiciel. Cependant, il existe un autre moyen de piloter, plus finement, ce client P2P.

Le client P2P renommé [Transmission](http://doc.ubuntu-fr.org/transmission "Transmission sur la Doc Ubuntu-fr"), installé par défaut sur Ubuntu, dispose d'une version &laquo;headless&raquo; que l'on peut installer sur un serveur sans interface graphique.

Ce _daemon_ permet de récupérer des images ISO depuis un serveur, et est gérable depuis une interface Web. Le problème c'est que, quand on ajoute un `.torrent`, tout est sauvegardé par défaut dans un seul dossier.

Sauf que moi, j'aime bien que mes image ISO soient bien triées dans plusieurs dossiers, du coup ça me les casse un peu de devoir tout redéplacer après parce que (1) c'est chiant à faire, (2) si on le fait, ça implique de devoir arrêter de seeder les fichier, et (3) si on veut seeder, il faut avoir le fichier à 2 endroits différents.

Du coup, je me suis penché un peu plus sur le truc, et j'ai découvert qu'il existait un outil qui permet de gérer plus finement Transmission, directement depuis la ligne de commande.

Cet outil, c'est **`transmission-remote`**, disponible dans les dépôts de toute bonne distrib' GNU/Linux.

Je ne vais pas détailler tout le machin, pour ça vous avez le `man`, je vais juste donner la commande permettant de lancer un téléchargement sur un serveur distant (en passant par le service Web) à partir d'un `.torrent`, tout en fixant un répertoire de destination différent de celui par défaut.

	:::zsh
	transmission-remote server:9091/transmission/ -a fichier.torrent -w /repertoire/de/destination/ -n user:password

- `server:9091/transmission/` : URI du service Web de transmission
- `-a fichier.torrent` : Fichier `.torrent`
- `-w /repertoire/de/destination/` : Répertoire de destination, sur le serveur distant
- `-n user:password` : login et mot de passe de connexion au service Web