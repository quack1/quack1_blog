Title: Tunneliser GPG dans un proxy SOCKS
Date: 2013-05-24 09:12
Author: Quack1
Category: Linux
Slug: gpg_proxy_socks
Tags: Linux, GPG, SOCKS, planet-libre, planet-ubuntu
Summary: Options à ajouter à GPG pour faire passer le trafic par son proxy SOCKS.
Lang: fr

&nbsp;
<div align=center><img src="static/upload/matrix.png" width="600" height="250" align=center /></div>

Au travail, ne me demandez pas pourquoi, le firewall bloque par défaut le port dédié à _hkp_ (11371/tcp), utilisé notamment pour récupérer des clés GPG. (Bon, par contre, on peut accéder à Mega... :sifflote:). Bref, c'est un peu casse-bonbons pour fetcher des clés et surtout mettre à jour des listes de paquets sur mon Ubuntu, puisqu'_apt_ a besoin des clés GPG pour authentifier les serveurs.

La solution à laquelle j'ai pensé est de faire passer les communications de _gpg_ dans mon proxy SOCKS (monté par _ssh_, plus d'[infos pour monter le proxy ici](http://artisan.karma-lab.net/faire-passer-trafic-tunnel-ssh)). Pour cela, on rajoute une simple option _gpg_ pour définir l'URI du proxy socks : 

	:::zsh
	╭────<quack@spiderman >───< ~ >  
	╰───[17:13:13] $ gpg --keyserver-options http-proxy=socks5-hostname://127.0.0.1:1080

Et, pour revenir au problème initial, pour ajouter une clé _gpg_ pour _apt_, on rajoute la même option que pour _gpg_ :

	::zsh
	╭────<quack@spiderman >───<  /etc/apt/sources.list.d >  
	╰───[17:25:35] $ sudo apt-key adv --keyserver-options http-proxy=socks5-hostname://127.0.0.1:1080 --keyserver keyserver.ubuntu.com --recv-keys C383CF524EE6B458

[Source](http://lists.gnupg.org/pipermail/gnupg-devel/2012-September/026930.html)