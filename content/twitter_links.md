Title: Sauvegarde des liens partagés sur Twitter sur le blog
Date: 2014-01-02 11:59
Author: Quack1
Category: Blog
Tags: Blog, Tweets, Twitter, planet-libre, pelican_auto_tweet
Slug: twitter_links
Summary: Je partage pas mal de liens sur Twitter et parfois, quand on veut en retrouver un en particulier c'est un peu tendu. Du coup, je me suis fais un petit script Python qui va récupérer tous mes tweets contenant des liens pour les centraliser sur [une page de ce blog]({filename}/pages/links.md)
Lang: fr

&nbsp;
<div align=center><img src="/upload/twitter_links.png" width="600" height="250" align=center /></div>

Je partage pas mal de liens sur Twitter et parfois, quand on veut en retrouver un en particulier c'est un peu tendu. Du coup, je me suis fais un petit script Python qui va récupérer tous mes tweets contenant des liens pour les centraliser sur [une page de ce blog]({filename}/pages/links.md)

Le fonctionnement du script est tout bête. Il récupère tous les nouveaux tweets de la veille apparus depuis le dernier lancement, il supprime les retweets, les réponses et les messages automatiques générés par ce blog, puis ajoute le tweet à une page dédiée à cela.

Les derniers tweets sont ajoutés au début de la page, du plus récent au plus ancien. Le format de la page est <s>moche</s> sobre, juste le texte du tweet et les url converties en liens cliquables.

<div align="center" style="color:#ccc;">☠</div>

Bien évidemment, le code est disponibles sous licence BSD et accessible sur [Github](https://github.com/quack1/pelican_auto_tweet/blob/master/pelican_links_summary.py "pelican_auto_tweet/pelican_links_summary.py at master · quack1/pelican_auto_tweet"). La génération des pages est spécifique à [Pelican](/tag/pelican.html), c'est pourquoi il prend place à l'intérieur du projet [pelican_auto_tweet](/tag/pelican_auto_tweet.html).

Un peu de conf est nécéssaire (dans le fichier `conf.py`) : 

- `TWITTER_USERNAME = ""` : Username du compte Twitter pour lesquels on doit récupérer les liens (exemple : "_Quack1") ;
- `PAGE_HEADER = ""` : L'entête à rajouter en haut du fichier source de la page recensant les liens (nécéssaire à Pelican). J'utilise une variable, matérialisée par `%s` qui contiendra la date/heure de mise à jour ;
- `LINKS_OUT_FILE = ""` : Chemin du fichier dans lequel écrire les pages. Si ce fichier contient déjà des liens, je me débrouille pour placer les nouveaux au bon endroit.

Il faut un peu de conf en plus, notamment pour se connecter à l'API Twitter, mais j'en ai [déjà parlé ici](https://github.com/quack1/pelican_auto_tweet/blob/master/README.md#usage "pelican_auto_tweet/README.md at master · quack1/pelican_auto_tweet").

<div align="center" style="color:#ccc;">☠</div>

J'en profite au passage pour présenter mon nouveau [_background_ Twitter](https://twitter.com/_Quack1), basé sur le design de ce blog :)