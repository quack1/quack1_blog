Title: Un Rapsberry Pi comme homeserver, bonne idée ?
Date: 2013-08-29 10:27
Author: Quack1
Category: Linux
Tags: Raspberry Pi, Linux, Serveur, Retour d'expérience, planet-libre
Slug: rex_raspi
Summary: Cela fait 6 mois que j'utilise un Raspberry Pi comme _homeserver_. Est-ce vraiment une bonne idée, ou vaut-il mieux louer un serveur dans un DC ? Retour d'expérience...

Depuis début Mars, et notamment la [V3 du blog](|filename|/blog_v3.md "Quack1 : Nouvelle version du blog!"), je m'auto-héberge sur un Raspberry Pi, branché au cul de ma box OVH. 

Ce Raspi héberge : 

- Mon blog sur un serveur nginx (en html pur, sans php ni Mysql) ;
- Un serveur de mail (avec le combo postfix/dovecot) ;
- Un serveur OpenVPN.

Depuis peu j'ai également un deuxième Raspberry Pi, qui lui propulse un OpenElec pour faire office de _mediacenter_, mais ça ne rentre pas vraiment dans le cadre de l'auto-hébergement.

Mais la question qui est au coeur de cet article est _Est-il vraiment judicieux d'utiliser un Raspberry Pi, chez soi derrière une box ADSL, pour héberger ses services Internet ?_

TL;DR; Personnellement je dirais oui! Je suis très content de mon Raspberry et ça réagit plutôt bien et rapidement.

Le Raspberry Pi étant (très) petit, il se glisse n'importe où. Chez moi, les deux machines sont derrière ma télé, juste à côté de ma Box, et tout tient sans trop de problème avec nos 2 disques durs externes. Le seul problème, c'est la quantité de câbles...[1]

Au niveau du système, je suis content de Raspbian et le Raspberry répond bien. Quand on doit générer des clés OpenVPN c'est un peu plus long, mais sinon ça roule bien. Même en étant derrière une box ADSL, les temps de réponse sur le blog sont corrects, et l'envoi/réception des mails est bon également.

Je peux même me fendre de l'utilisation d'un VPN ou d'un tunnel SOCKS et regarder des vidéos sur Youtube (en _low quality_) sans que ça coupe.

La charge de l'OS est faible, puisque les seuls services qui tournent (web, mail) sont en attente des connexions externes, et aucun gros traitement n'est effectué par ceux-ci.

&nbsp;

Le Raspberry me permet de reprendre la main sur mes services en étant **vraiment** décentralisé. Tant que je ne génère pas beaucoup de trafic sur le blog ça passe avec ma connexion ADSL, mais si un jour ça augmente beaucoup je devrais passer à une meilleure connexion Internet.

En conclusion : OUI!, vous pouvez vous auto-héberger chez vous sur un Raspberry Pi, même si ça demande un peu de temps quand même pour tout mettre en place ;)

&nbsp;

[1] Si quelqu'un a une solution, [DIY](/tag/diy.html "Quack1 : Tag - DIY") de préférence, pour ranger/trier les câbles, je suis preneur ;)