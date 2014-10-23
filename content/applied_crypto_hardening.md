Title: Bonnes pratiques de mise en place de la cryptographie
Date: 2014-10-23 10:18
Author: Quack1
Category: Sécurité
Tags: Sécurité, Crypto
Slug: applied_crypto_hardening
Summary: Le projet [bettercrypto.org](https://bettercrypto.org "BetterCrypto⸱org") a récemment mis en ligne un [long document](https://bettercrypto.org/static/applied-crypto-hardening.pdf "applied-crypto-hardening.pdf") permettant aux adiminstrateurs systèmes de mettre en place de la cryptographie sur les principaux services réseaux, en respectant l'état de l'art des bonnes pratiques.
Lang: fr

&nbsp;

<div align=center><a href="/upload/bettercrypto.org.png"><img src="/upload/bettercrypto.org.png" width="600" align=center /></a></div>

Le projet [bettercrypto.org](https://bettercrypto.org "BetterCrypto⸱org") a récemment mis en ligne un [long document](https://bettercrypto.org/static/applied-crypto-hardening.pdf "applied-crypto-hardening.pdf") permettant aux adiminstrateurs systèmes de mettre en place de la cryptographie sur les principaux services réseaux, en respectant l'état de l'art des bonnes pratiques.

> This guide arose out of the need for system administrators to have an updated, solid, well re-searched and thought-through guide for configuring SSL, PGP, SSH and other cryptographic tools in the post-Snowden age. Triggered by the NSA leaks in the summer of 2013, many system administrators and IT security officers saw the need to strengthen their encryption settings. This guide is specifically written for these systema dministrators.

Le document donne, pour chaque logiciel, des exemples de configurations qui peuvent être directement _copiés/collés_ et utilisés. Cette configuration comprent, généralement, l'activation du support de SSL/TLS, la _cyphersuite_ optimale, la gestion des clés/certificats, etc.

- Webservers
- SSH
- MailServers
- VPN
- PGP/GPG-PrettyGoodPrivacy
- IPMI, ILO and others
- Instant Messaging
- Databases
- Proxys and reverse-proxys
- Kerberos

En plus de cette partie technique, une grande partie théorique termine ce document et explique les raisons des choix des _cyphersuite_ utilisées, le fonctionnement des algorithmes de crypto, etc.

Ce document est versionné avec [git](/tags/git.html "Tag : git") et un miroir est disponible sur [Github](https://github.com/BetterCrypto/Applied-Crypto-Hardening "BetterCrypto/Applied-Crypto-Hardening on GitHub"). Vous pouvez donc le forker et soumettre vos _Pull-Requests_ pour le corriger ou l'amélirer !

Enfin, sachez qu'une initiative similaire et française, lancée par [@vincib](https://twitter.com/vincib) et [@skhaen](https://twitter.com/skhaen), donne aux administrateurs systèmes toute une méthodologie pour mettre en place HTTPS sur leurs sites Web. [JeVeuxHTTPS](https://www.jeveuxhttps.fr/Accueil "JeVeuxHTTPS") est pour le moment en bêta, mais vous pouvez y jeter un œil et y contribuer.
