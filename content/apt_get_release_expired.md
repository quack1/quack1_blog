Title: Contourner l'erreur « Le fichier Release a expiré » dans APT
Date: 2013-10-23 09:16 
Author: Quack1
Category: Linux
Tags: Linux, Debian, Apt, Job, planet-libre, planet-ubuntu
Slug: apt_get_release_expired
Summary: 

J'ai quelques billets en cours qui sont juste des petites astuces, relativement faciles à trouver sur Internet, mais que je préfère garder au chaud ici!

Premier truc, concernant _apt_ — le [système de gestion de paquets sur Debian](https://fr.wikipedia.org/wiki/Advanced_Packaging_Tool), pas les [attaques ciblées](https://en.wikipedia.org/wiki/Advanced_Persistent_Threat) ;-).

Quand on fait ses mises à jour et installations de paquets depuis des miroirs des dépôts officiels, on peut obtenir l'erreur « `E: Release file expired, ignoring http://debian.mirror.localhost/repo_bin/dists/sid/Release (invalid since 14h 31min 45s)` », qui est levée si le fichier _Release_, présent à la racine du dépôt, n'est pas à jour. Ce fichier _Release_ permet de vérifier l'intégrité des paquets téléchargés sur le dépôt.

Si vous n'avez pas la main sur le miroir, mais que vous lui faites quand même confiance et que souhaitez tout de même installer vos paquets depuis cette source, vous pouvez demander à _apt_ de ne pas vérifier la validité du fichier _Release_ : 

	:::zsh
	$ apt-get -o Acquire::Check-Valid-Until=false update

Si vous avez accès à un shell sur la machine qui gère les miroirs, à priori c'est plutôt simple de regénérer le fichier _Release_, il suffit de recréer le miroir avec un `debmirror`, mais je n'ai jamais tenté.

<div align="center" style="color:#888;">☠</div> &nbsp;

[Via StackExchange Unix](http://unix.stackexchange.com/questions/2544/how-to-work-around-apts-release-file-expired-problem-on-a-local-mirror "Stack Exchange Unix - « how to work around APT's 'Release file expired' problem on a local mirror »")