Title: Du bannissement des IP sur son serveur...
Date: 2013-07-05 11:10
Author: Quack1
Category: Securité
Slug: ban_ip_filtrage
Tags: Sécurité, Filtrage, Firewall, IPS, IDS, planet-libre, planet-ubuntu
Summary: Réflexions à propos du bannissement de certaines adresses IP sources d'attaques sur son serveur, ou encore à propos de l'utilisation de systèmes de prévention d'intrusions (ou IPS).
Lang: fr

&nbsp;
<div align=center><img src="static/upload/404.png" width="600" height="250" align=center /></div>

En début de semaine, un de mes amis Facebook, ancien camarade de Licence en Informatique, a publié un statut qui m'a un peu fait tiqué. J'ai un temps voulu lui répondre directement, puis j'ai attendu quelques jours en réflechissant plus calmement à ma réponse (toujours faire attention à son [esprit d'escalier](http://fr.wikipedia.org/wiki/Esprit_de_l%27escalier "L’Esprit de l’escalier, ou esprit d’escalier : expression française signifiant que l’on pense souvent à ce que l’on aurait pu et dû dire de plus juste, après avoir quitté ses interlocuteurs ; « l’inspiration nous vient en descendant l’escalier de la tribune », mot de Diderot, dans son Paradoxe sur le comédien. [Wikipédia]")), et je me suis dit que finalement c'était mieux de faire un billet afin de mettre à plat mon opinion sur le sujet, pour pouvoir écrire un peu plus que sur un simple commentaire Facebook tout en en faisant profiter mes chers lecteurs!

Le statut en question est celui-ci (le gras est de moi) : 

> Avoir un serveur, c'est passer sa vie à **bannir définitivement** des IP...

Ce qui m'a géné c'est, comme vous l'avez peut-être deviné, le fait de bannir des IP, au prétexte que l'on détecte des "attaques" provenant de celles-ci.

Je trouve ça assez dérangeant, parce qu'aujourd'hui bannir une IP ne signifie pas bannir une personne en particulier. Cela veut dire bannir tout un foyer, qui sort sur Internet derrière une seule frigoBox. Pire, dans certains pays où les FAI branche plusieurs abonnés derrière un seul gros NAT (et donc derrière la même IP publique), on se retrouve à bloquer tous les abonnés d'un FAI au niveau d'une ville ou d'un quartier. De la même façon, l'adresse IP publique bloquée peut être celle d'un VPN ou d'un noeud de sortie TOR. Comme précédemment, on va potentiellement bloquer de nombreuses personnes n'ayant aucun lien entre elles, et leur interdisant ainsi l'accès à un (ou plusieurs) site(s) Web à cause d'un seul petit rigolo.

Mais bien évidemment, le ban d'adresses IP ne se fait pas par pur plaisir (quoi que, peut être que certains le font :p ). Tout ceci vise à augmenter la sécurité de ses applications Web et serveurs en réduisant le nombre d'attaquants potentiels. Je ne pense pas que ce soit la solution à tous les maux.

Non pas que je souhaite que tous les serveurs se fassent p0wner, mais il y a à mon avis d'autres solutions beaucoup plus propres et sécurisantes. Il y a une solution très simple pour contourner ce blocage : changer d'IP. Et pour cela, les solutions VPN et proxys sont disponibles en grande quantité sur le Net. Et les attaques reprendront sans plus de protection. Et si vous êtes vulnérables, vous vous ferez avoir.

Alors que si votre système et vos logiciels sont correctement patchés et configurés, vous n'aurez rien à craindre et donc pas besoin de bannir des addresses. Pour moi la solution est là. Mettez à jour vos systèmes, vos machines, configurez les correctement et vous n'aurez pas besoin d'avoir peur des attaques ni de bannir des addresses.

&nbsp;

J'éprouve les mêmes sentiments vis à vis des IPS (ou systèmes de prévention d'intrusions). Basés sur les signatures des activités malveillantes, ils bloquent tout le trafic anormal en laissant passer le trafic autorisé.

Ces techniques donnent une impression de sécurité, puisqu'ils bloquent tout ce qui est connu comme étant une source d'attaques. Sauf que les attaquants trouveront toujours des manières de bypasser les protections, comme changer d'IP ou modifier le _payload_ envoyé lors de l'attaque. Au premier abord on va croire qu'on se protège de tout, alors que pas du tout, et que l'entretien de règles de cette façon est très long, et qu'il peut provoquer des pertes d'accès pour énormément de personnes bien intentionnées et qui ne sont pas concernées par les attaques lancées.

&nbsp;

En définitive, ne bloquez pas d'IP et ne bloquez pas (à priori) de traffic. Est-ce que les attaques lancées sont vraiment dangereuses ? Est-ce qu'elles peuvent impacter votre image ou la qualité de service ? Si non, laissez tomber et oubliez l'attaque. L'attaquant finira bien par se lasser! Concentrez vous plutôt sur la détection des intrusions. 

À quoi bon vouloir bloquer des attaques qui ne fonctionneront pas de toute façon, si vous ne détectez pas les intrusions effectives. Mettez en place des IDS, remontez vos logs, regardez avec précision les activités suspectes qui témoignent des intrusions. Vous serez beaucoup plus efficaces! 

Ou au pire, appelez des boîtes qui le font très bien, on a besoin de boulot nous aussi ;-)
