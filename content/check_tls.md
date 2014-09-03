Title: [Note] Vérifier la configuration TLS/SSL de vos services réseaux
Date: 2014-08-27 19:57
Author: Quack1
Category: Sécurité
Tags: Note, Sécurité, Linux, TLS, Web, Jabber, Mail, SMTP, planet-libre
Slug: check_tls
Summary: Note rapide pour me souvenir de trois services permettant de tester des configurations SSL/TLS.
Lang: fr

_Note pour ne pas perdre ces quelques liens._

Trois services en ligne permettent de vérifier que la configuration SSL/TLS de vos services est bonne. Ces sites vous donnent une note permettant de voir de façon rapide où vous en êtes.

- Web → [SSL Labs](https://www.ssllabs.com/ssltest/ "Qualys SSL Labs - Projects SSL Server Test") ;
- Jabber/XMPP → [IM Observatory](https://xmpp.net/index.php "IM Observatory") ;
- Starttls sur SMTP → [STARTTLS.info](https://starttls.info/ "STARTTLS.info").

Si vous en connaissez d'autres, je suis preneur :)

Et si vous voulez tester vos configurations SSL hors-ligne, l'outil [sslscan](http://sourceforge.net/projects/sslscan "SSLScan - Fast SSL Scanner | SourceForge.net") dispose d'une _checklist_ assez complète.

Enfin, pour avoir quelques bonnes pratiques sur SSL/TLS ainsi que des connaissances théoriques sur le sujet, la conférence de [Benjamin Sonntag](https://twitter.com/vincib "@vincib sur Twitter") au cours d'[Il était une fois Internet](http://www.iletaitunefoisinternet.fr/ "Il était une fois internet") est très complète ! Voir la vidéo et les slides [ici](http://www.iletaitunefoisinternet.fr/lemail-par-benjamin-sonntag/ "L'email, Benjamin Sonntag").

========

EDIT : 27/08/2014 22:16 — [Aeris](https://twitter.com/aeris22 "@aeris22 sur Twitter") me signale aussi [SSL Tools](https://ssl-tools.net/ "SSL, STARTTLS and certificate tester") qui permet de tester la sécurité de serveurs Web, mails, et de vos certificats X.509.
