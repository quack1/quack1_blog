Title: Persona - Comment Mozilla est en train de révolutionner l'authentification
Date: 2013-05-28 12:00
Author: Quack1
Category: Mozilla
Slug: persona_presentation
Tags: Mozilla, Persona, Authentification, Cloud, Identité, Mot de passe, planet-libre, planet-ubuntu
Summary: La gestion des mots de passe est très complexe et pose de nombreux problèmes de sécurité. Mozilla, au travers du projet Persona, tente de proposer un nouveau système permettant de simplifier et sécuriser l'authentification des utilisateurs.
Lang: fr

&nbsp;
<div align=center><img src="static/upload/top_worst_password.png" align=center /></div>

Mozilla, au travers du projet **Persona**, veut proposer une solution au problème des mots de passe sur le Web. Je trouve que c'est un très bon projet, c'est justement pour cette raison que je commence à y contribuer, et il mérite que l'on s'y intéresse.

Je vais humblement tenter de vous le présenter pour, je l'espère, que vous le mettiez en place sur votre site!

&nbsp;

L'un des grands problèmes de la sécurité, c'est qu'elle s'accompagne souvent de contraintes vis-à-vis des utilisateurs. Mots de passe longs et complexes. Chiffrement. Changement de mot de passe pour chaque site. Tout ceci, c'est long, c'est chiant. Donc on ne le fait pas et on utilise le même mot de passe partout.

Le problème, c'est que quand des gros sites se font pirater et que les mots de passe sont diffusés (comme [Linkedin](http://www.pcinpact.com/news/71501-linkedin-fuite-mots-de-passe-blocage-comptes.htm "PCInpact - Linkedin Leak") ou [Yahoo!](http://www.zdnet.fr/actualites/piratage-de-mots-de-passe-yahoo-ce-qu-il-faut-savoir-39774139.htm "ZDNet - Yahoo! Leak")), on peut voir son compte se faire compromettre sur d'autres sites si on y utilise le même login/mot de passe que sur le site piraté.

L'autre problème des mots de passe, c'est pour les développeurs, puisqu'il faut les stocker de façon sécurisée pour éviter la perte d'informations pour l'utilisateur.

Des solutions existent, comme s'authentifier en utilisant un service externe, comme Facebook ou Twitter. Cependant, on exporte nos données chez des services tiers, et on ne garde l'accès à notre compte que tant que le tiers est disponible et propose la solution d'authentification.

&nbsp;

La solution est **Persona**. Ce nouveau "service" apporte de la sécurité, de l'indépendance, et une facilité d'installation et d'utilisation. En pratique, comment est-ce que ça marche ?

Dans Persona, vous possédez une (ou plusieurs) identité(s). Cette identité est identifiée par votre adresse email. Au moment de l'authentification, au lieu de devoir donner un mot de passe à chacun des sites Web, le site va, au moyen de Persona, faire une requête à votre _Identity Provider_, le site tiers qui gère votre identité. Ensuite, vous prouvez à ce site que vous êtes bien celui que vous dîtes que vous êtes, et ce dernier va alors annoncer au premier site que vous êtes identifié. 

En pratique, les choses ne se passent pas exactement de cette façon. Je ferais un autre article pour expliquer plus en détail le fonctionnement et la sécurité derrière Persona.

Avec ce système, au lieu de donner le même (ou des différents) mot de passe à 50 sites différents, et ainsi multiplier les risques de fuites de données, vous n'avez qu'un seul mot de passe à retenir. La connexion est aussi beaucoup plus simple. Il suffit de cliquer sur le bouton "Login with Persona", puis sélectionner l'identité avec laquelle vous voulez vous connecter. Ce n'est pas plus compliqué que pour n'importe quel autre système d'authentification.

<p><div align=center><a href="static/upload/persona_signin.png"><img src="static/upload/persona_signin.png" align="center" width="350"/></a></div></p>

Pour les développeurs, les avantages sont multiples : plus besoin de maintenir à jours des politiques de stockage de mots de passe, n'y même de vous demander si l'adresse email qui vous a été donné par l'utilisateur est correcte ou non. Persona, de par son fonctionnement, vous assure que l'adresse email est valide **et** utilisée par l'utilisateur.

&nbsp;

Enfin, on peut noter un autre problème, plutôt d'ordre pratique. Sur chaque site où l'on doit s'enregistrer, on doit ensuite configurer son compte, pour fournir certaines informations, comme son nom, son site Web, son âge, etc... Un des projets qui sera une fonctionnalité future (des gens travaillent actuellement dessus), est Picl (prononcez _Pikeule_), ou _Profile In The Cloud_. Cela permettra, quand vous vous identifiez, de fournir à un site de récupérer automatiquement des informations sur votre compte depuis PiCL plutôt que vous ayez à les saisir.

Ce système est encore en cours de développement et n'arrivera pas avant fin 2013 je pense.

&nbsp;

Pour finir, parlons Vie Privée.

Comme tous les projets Mozilla, Persona est un projet Libre, diffusé sous la [Mozilla Public Licence](https://www.mozilla.org/MPL/ "Mozilla MPL"). Tout le monde peut (et doit! ;)) donc l'utiliser et l'intégrer à son site, pour reprendre le contrôle de ses données et se simplifier la vie, tant côté utilisateur que développeur!

Persona, en plus d'augmenter la sécurité, vous permet de redevenir maître de vos données. Puisque le service n'a pas vocation à être hebergé chez Mozilla. Au contraire, chaque personne (ou organisation) aura son propre _Identity Provider_ chez lui. 

En fait, ce n'est pas vraiment ça. Vous êtes identifié par votre adresse email. C'est donc le service qui vous fournit votre adresse email qui devient votre _Identity Provider_, et c'est chez lui que toutes vos données sont sauvegardées. Donc, si votre adresse est chez GMail, on ne gagne pas grand chose niveau vie privée, si vous avez votre propre serveur de mail, c'est déjà beaucoup mieux puisque vous gérez vous même vos informations.

&nbsp;

À l'heure actuelle, plusieurs sites proposent l'authentification avec Persona, notamment [Jocly](http://www.jocly.com/ "Jocly Home Page"), [site de jeux Html5](|filename|/jocly.md) et la plupart des sites et services de mozilla. 

Au niveau des services qui sont _Identity Providers_, je crois que Yahoo l'est. Je n'ai pas trop d'autres noms en tête, mais n'hésitez pas à demander à votre fournisseur de supporter le service. C'est Open-Source, c'est libre, et c'est sécurisé! Sachez que Mozilla a mis en place un _Identity Provider_ de secours qui vous permet d'utiliser le service même si, dans mon cas par exemple, Google ne gère pas encore Persona.

&nbsp;

[Présentation de François Marier sur Persona](http://www.slideshare.net/fmarier/html5mtl-persona "Slideshare - François Marier : Un Système Ouvert Et Fédéré Pour L'Authentification Des Utilisateurs")
[Image d'en-tête](http://xato.net/passwords/more-top-worst-passwords/ "Top Worst Passwords")