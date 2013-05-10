Title: Nouvelle version du blog!
Date: 2013-05-07 17:15
Author: Quack1
Category: blog
Slug: blog_v3
Tags: Blog, Pelican, Notebook, planet-libre, v3
Summary: Présentation de la v3 (?) du blog!

&nbsp;
<div align=center><img src="static/upload/blog_v3_header.png" width="600" height="250" align=center /></div>

Vous l'avez sûrement remarqué, depuis quelques semaines, le blog a changé de peau! L'occasion pour faire la présentation officielle de cette nouvelle version, précédée d'un petit historique.

# La v1 : wordpress.com

J'ai ouvert ce blog, à l'origine sur wordpress.com, en 2011. Le premier date d'ailleurs du [25 novembre 2011](|filename|/hello-world.md)! C'est pour moi la **v1** du blog. Il aura vu la publication des 43 premiers billets, à un rythme plutôt régulier au début, et quelques très belles réussites en terme de visites (surtout dûes à l'[effet Korben](http://www.youtube.com/watch?v=_7p7fTsgsE4 "Effet Korben par @jcfrog") et à d'autres, comme [@jcfrog](http://twitter.com/jcfrog) ou [Crazy Ws](http://twitter.com/crazyws)) : 

- [The Pirate Bay hebergé dans l'espace](/the-pirate-bay-heberge-dans-lespace.html) : 8k vues
- [Ubuntu : Unity vs Gnome-Shell : Avis (non) objectif](/ubuntu-unity-vs-gnome-shell-avis-non-objectif.html) : 2k vues
- [MAO : Monter son (petit) home-studio sous Linux](/mao-monter-son-petit-home-studio-sous-linux.html) : 1,7k vues


Il aura duré un bon moment, jusqu'en Octobre 2012. Grâce à la magie (ou pas) de Google, les stats de visite sont stables et tournent autour de 10/15 visiteurs uniques journaliers. Malheureusement, malgré la présence d'un lien en début de chaque article qui mène à ce nouveau blog, je récupère très peu de visites (seulement 247 clics vers mon nouveau domaine depuis Octobre 2012). Je songe d'ailleurs à mettre en place une solution radicale à ce sujet. Mais bref, ce n'est pas le propos de l'article!

# On grandit, et on s'auto héberge!

Je dois le reconnaitre, j'étais très bien chez wordpress.com. Je n'avais pas à me soucier des mises à jour du serveur, ni de mon instance de Wordpress, pas de base de données à gérer, bref, c'était la belle vie!

Jusqu'au jour où j'ai voulu deux choses : 

- Toucher un peu au design du blog
- Récupérer mon indépendance et avoir un peu plus de services disponibles.

J'ai donc décidé de m'auto-héberger. Avoir mon petit serveur à moi, pouvoir faire du ssh dessus, avoir des dépôts [git](http://doc.ubuntu-fr.org/git "Doc Ubuntu−Fr : git"), avoir autant de sites que je voulais, etc. J'ai donc un temps pensé à louer une machine chez une hébergeur, genre OVH ou Online, mais le souci du coût m'a un peu rebuté. _Mais ils ont des offres à 5€/mois ?_ Ah, oui. Donc nouvelle excuse. L'auto-hébergement c'est bien. Quitter des services centralisés appartenant à des boites américaines c'est bien, mais se re-centraliser derrière pour qu'on finisse tous chez Ovh ou Online, je trouve ça un peu con et pas très décentralisé. Pour moi, le truc, c'est chacun avec son petit serveur chez soi.

J'ai donc décidé de remplacer mon vieux portable qui ne me servait plus pour un faire mon serveur Web^W à tout faire! J'étais donc fièrement auto-hebergé derrière ma ligne ADSL Orange pas top. Mais au moins tout était chez moi!

Ce fût donc la **v2** du blog! Un wordpress installé sur un vieux portable, avec un Apache, PHP, MySQL et tout le toutim. Cependant cette configuration a apporté plusieurs problèmes : un PC sous un bureau c'est gros, ça fait du bruit, ça chauffe, et ça bouffe du courant. Il a donc fallu réduire tout ça, et se mettre au produit à la mode du moment : le **Raspberry Pi**

# Déménagement et minimisation

J'ai dû déménager sur Paris au mois de Mars, j'en ai profité pour migrer le blog petit à petit de Wordpress à [Pelican](http://getpelican.com), un moteur de blog statique écrit en python. La raison était simple : pouvoir modifier le blog **beaucoup** plus facilement (au niveau du _backend_ et du thème), ne pas avoir à faire tourner un serveur LAMP complet (ici pas de Php ni MySQL, et comme on ne sert que des fichiers statiques, exit _Apache_ et bonjour **nginx**). J'ai également découvert un autre avantage à Pelican : pouvoir écrire mes articles n'importe où, n'importe quand. Pas besoin d'être connecté en permanence a Wordpress pour écrire mes articles, je peux le faire offline sur mon téléphone en étant dans les sous-sols de Paris en RER!

La publication est donc également beaucoup plus simple : la totalité du blog est versionnée avec git, et poussée en prod sur le blog via ssh.

Au niveau de la configuration du serveur, on a donc un Raspberry Pi branché derrière une ligne ADSL OVH, et qui tourne sur Raspbian avec simplement un nginx.

# À l'avenir

La première résolution que j'ai décidé de prendre concernant ce blog était d'écrire des articles plus régulièrement, et pour cela d'écrire des articles plus court, plus faciles à lire et à publier.

Je voulais vous parler d'autres petites choses ici, mais l'article commencant à grandir je ferais d'autres articles, notamment sur le nouveau thème du blog développé spécialement par mes soins, et une infographie (ou simplement un article) pour faire un retour sur 1 an et demi de blogging amateur.

À bientôt donc pour de nouvelles aventures ;-)