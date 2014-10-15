Title: Vulnérabilité Poodle sur SSLv3 : liens en vrac
Date: 2014-10-15 10:16
Author: Quack1
Category: Sécurité
Tags: Sécurité, SSL, TLS, Poodle, planet-libre
Slug: poodle
Summary: 
Lang: fr

Une vulnérabilité critique sur SSLv3 — qui devait ne plus être utilisé depuis longtemps — a été découverte par les équipes sécurité de Google.

Je passe les détails techniques, l'important est qu'elle permet à un attaquant de déchiffrer le trafic en injectant du padding dans certains paquets.

Le workaround pour cette vulnérabilité : désactiver totalement le support de SSLv3 dans la configuration des serveurs (ce qui devrait normalement déjà être le cas).

Pour voir si les serveurs sont vulnérables, il suffit simplement d'essayer de se connecter au serveur en utilisant SSLv3 :

    :::bash
    $ openssl s_client -connect <server>:<port> -ssl3​

Quelques liens en vrac :

- Tester si le client est « vulnérable » (ie. s'il supporte SSLv3) : <https://www.poodletest.com/> ;
- Tester si le serveur est « vulnérable » (ie. s'il supporte SSLv3) : <https://www.ssllabs.com/ssltest/> ;
- L'annonce officielle de Google : <http://googleonlinesecurity.blogspot.co.uk/2014/10/this-poodle-bites-exploiting-ssl-30.html> ;
- L'annonce officielle et technique de Google : <https://www.openssl.org/~bodo/ssl-poodle.pdf> ;
- Une deuxième annonce sur le sujet : <https://isc.sans.edu/diary/OpenSSL%3A+SSLv3+POODLE+Vulnerability+Official+Release/18827> ;
- Le billet de Mozilla qui annonce l'arrêt du support de SSLv3 dans Firefox dès Firefox 34 : <https://blog.mozilla.org/security/2014/10/14/the-poodle-attack-and-the-end-of-ssl-3-0/​> ;