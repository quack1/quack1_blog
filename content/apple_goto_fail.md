Title: Apple &#35;gotofail : Explications simples et détaillées de la faille (FR et EN)
Date: 2014-02-24 14:58
Author: Quack1
Category: Securité
Tags: Securité, Apple, Fail, GotoFail, planet-libre
Slug: apple_goto_fail
Summary: 
Lang: fr

&nbsp;

<div align=center><a href="/upload/apple_goto_fail.png"><img src="/upload/apple_goto_fail.png" width="600" height="250" align=center /></a></div>

[Stephane Bortzmeyer](https://twitter.com/bortzmeyer) a publié sur [SeenThis](http://seenthis.net/messages/230904) un post dans lequel il présente de façon simple la faille « Goto Fail » qui a été découverte sur les systèmes d'exploitation Apple en fin de semaine dernière, et référencée dans la [CVE-2014-1266](http://support.apple.com/kb/HT6147)

Pour les anglophones, un très bon article (un peu plus technique) est [disponible ici](https://www.imperialviolet.org/2014/02/22/applebug.html).

En gros, techiquement, ce qu'il se passe c'est que lors de l'établissement d'une connexion TLS, le serveur échange dans un [Diffie-Hellman](http://fr.wikipedia.org/wiki/Diffie-Hellman) une clé de session qui permettra de chiffrer les connexions. Cette clé est _signée_ par le certificat du serveur. Le problème, c'est qu'une bogue dans le code source a planté la vérification de cette signature par le client. Ce qui permet à un attaquant de réaliser un [_Man-In-The-Middle_] sans que le client ne s'en apercoive.

Si vous utilisez des produits Apple, vous pouvez tester votre système sur [gotofail.com](https://gotofail.com/).

Le code-source est public et disponible sur [les dépots ouverts d'Apple](http://opensource.apple.com/source/Security/Security-55471/libsecurity_ssl/lib/sslKeyExchange.c).
