Title: Obtenir le fingerprint SSH de son serveur
Date: 2013-07-08 20:36
Author: Quack1
Category: Linux
Slug: ssh_fingerprint_server
Tags: Fingerprint, Sécurité, SSH, Linux, tips, planet-libre, planet-ubuntu
Summary: Cette commande est accessible simplement dans Google, mais comme pour wget, j'ai du mal à m'en souvenir et la flemme de devoir faire une recherche sur <s>Google</s> DuckDuckGo pour retrouver comment obtenir le fingerprint de mon serveur ssh, donc je préfère la noter ici!

Pour faire suite à mon article de [la semaine dernière sur le crawling récursif d'un site Web avec wget](|filename|/wget_website.md), je note ici la commande permettant de récupérer le fingerprint d'un serveur ssh.

Pour ceux qui voudraient plus d'infos sur SSH, le fingerprinting et le fingerprinting appliqué à SSH, j'ai fait un petit catch-up plus bas dans l'article ;-)

TL;DR; : La commande en question : 

	:::zsh
	# Pour lister les clés publiques du serveur :
	ls /etc/ssh/*key*.pub
	# Pour obtenir le fingerprint d'une clé :
	ssh-keygen -lf /etc/ssh/ssh_host_ecdsa_key.pub

&nbsp;

# Détails sur ssh, fingerprint et co...

**SSH** est le protocole le plus utilisé permettant de se connecter à distance de façon sécurisée sur une machine Unix. D'ailleurs SSH signifie _Secure SHell_. L'implémentation d'SSH la plus utilisée à ce jour est OpenSSH, présente par défaut sur tous les bons GNU/Linux, ou au moins dans les dépôts officiels des distributions.

Un **fingerprint** est l'empreinte d'un fichier. En somme, c'est une valeur (généralement une chapine de caractères en hexadécimal) qui permet d'identifier de façon unique le fichier. 2 fichier différents auront 2 empreintes différentes. Dans la pratique, ces empreintes sont calculées avec des mécanismes cryptographiques appelés fonctions de hachage, qui vont "hacher" un fichier pour obtenir son empreinte unique.

SSH fonctionne avec des mécanismes de [chiffrement à clés publiques](https://fr.wikipedia.org/wiki/Cryptographie_asym%C3%A9trique). Quand on se connecte, on récupère la clé publique du serveur pour pouvoir chiffrer les communications (en réalité, on envoie au début de l'échange une clé symétrique, chiffrée avec les clés asymétriques. Le chiffrement symétrique étant beaucoup plus rapide que l'asymétrique). Afin de vérifier qu'on dialogue avec le bon serveur SSH, il est important de vérifier l'empreinte de la clé publique reçue pour voir si on ne s'est pas trompé de serveur (un serveur différent aura des clés différentes, qui auront elles-même des fingerprint différents). Le client OpenSSH fera ça tout seul et vous demandera de vérifier l'empreinte de la clé publique reçue en cas de doute.

[Source](http://www.lysium.de/blog/index.php?/archives/186-How-to-get-ssh-server-fingerprint-information.html)