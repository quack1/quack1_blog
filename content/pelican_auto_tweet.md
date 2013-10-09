Title: Moteur de blog Pelican : twitter un lien automatique vers son dernier article
Date: 2013-10-09 10:17
Author: Quack1
Category: Blog
Tags: planet-libre, Blog, Pelican, Python
Slug: pelican_auto_tweet
Lang: fr
Summary: Ce qu'il manque au moteur de blog de Pelican, c'est l'envoi automatique de tweets dès qu'on publie un nouvel article. Et bien désormais, il y a un script Python pour ça! :)

Le moteur de blog que j'utilise sur [ce blog]({filename}/blog_v3.md) est [Pelican](http://getpelican.com).

Je ne vais pas reventer encore une fois ses qualités, d'autres l'ont déjà bien fait avant moi. Je vais juste rappeler que j'aime bien pouvoir écrire directement mes articles en Markdown, pouvoir les versionner avec Git, et les publier en SSH sur mon serveur.

Il ne lui manque qu'une chose par rapport au blog que j'avait précédemment sur Wordpress : l'envoi automatique de [tweets](https://twitter.com/_Quack1) dès que je poste un nouveau billet.

Pour remédier à ce problème, j'ai développé [un petit script](https://github.com/quack1/pelican_auto_tweet) qui permet de faire ça rapidement.

Son fonctionnement est simple. Il récupère le dernier log Git du répertoire du projet. Si le message du commit commence par `[POST]` (c'est la convention que j'utilise pour mes messages de commit quand je publie un nouvel article), alors le script poste un tweet. Il récupère pour cela le titre de l'article et le lien dans le fichier source de l'article, lui même récupéré dans le commit.

Pour avoir plus d'infos sur la façon de l'installer, le lancer, etc, le mieux est d'aller lire le [README](https://github.com/quack1/pelican_auto_tweet) sur Github ;).

Les scripts sont diffusés sous licence BSD, disponibles sur [Github](https://github.com/quack1/pelican_auto_tweet), et j'attend vos remarques/corrections/_improvements_ ;-)

\#Teasing : Je publierais bientôt un article sur le second script présent dans le dépôt Git, et sur un moyen d'automatiser le lancement du script avec Git.