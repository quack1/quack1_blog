Title: Moteur de blog Pelican : twitter un lien automatique vers son dernier article
Date: 2013-10-09 10:17
Author: Quack1
Category: Blog
Tags: planet-libre, Blog, Pelican, Python
Slug: pelican_auto_tweet
Lang: fr
Summary: Ce qu'il manque au moteur de blog de Pelican, c'est l'envoi automatique de tweets dès qu'on publie un nouvel article. Et bien désormais, il y a un script Python pour ça! :)

<a href="https://github.com/quack1/pelican_auto_tweet"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_right_darkblue_121621.png" alt="Fork me on GitHub"></a>

Le moteur de blog que j'utilise sur [ce blog]({filename}/blog_v3.md) est [Pelican](http://getpelican.com).

Je ne vais pas revanter encore une fois ses qualités, d'autres l'ont déjà bien fait avant moi. Je vais juste rappeler que j'aime bien pouvoir écrire directement mes articles en Markdown, pouvoir les versionner avec Git, et les publier en SSH sur mon serveur.

Il ne lui manque qu'une chose par rapport au blog que j'avais précédemment sur Wordpress : l'envoi automatique de [tweets](https://twitter.com/_Quack1) dès que je poste un nouveau billet.

Pour remédier à ce problème, j'ai développé [un petit script](https://github.com/quack1/pelican_auto_tweet) qui permet de faire ça rapidement.

Son fonctionnement est simple. Il récupère le dernier log Git du répertoire du projet. Si le message du commit commence par `[POST]` (c'est la convention que j'utilise pour mes messages de commit quand je publie un nouvel article), alors le script poste un tweet. Il récupère pour cela le titre de l'article et le lien dans le fichier source de l'article, lui même récupéré dans le commit.

En détails, il fait ça : 

1. Il vérifie si un nouvel article a été écrit (en cherchant la présence du message `[POST]` au début du message de _commit_ [Git](http://blog.quack1.me/tag/git.html "Blog Quack1 - Tag « Git »")) ;
2. Dans ce cas, il envoie les nouveaux _commits_ sur [le dépôt Git défini par défaut]({filename}/git_push_multiple_remote.md "Git : Pusher ses modifications sur plusieurs dépôts en une seule commande") ;
3. Il met à jour le blog sur le serveur via SSH (command `make ssh_upload` pour les _Pelican-eux_) ;
4. Il envoie un tweet.

Pour avoir plus d'infos sur la façon de l'installer, le lancer, etc, le mieux est d'aller lire le [README](https://github.com/quack1/pelican_auto_tweet) sur Github ;).

Les scripts sont diffusés sous licence BSD, disponibles sur [Github](https://github.com/quack1/pelican_auto_tweet), et j'attend vos remarques/corrections/_improvements_ ;-)

\#Teasing : Je publierais bientôt un article sur le second script présent dans le dépôt Git, et sur un moyen d'automatiser le lancement du script avec Git.

<div align="center" style="color:#ccc;">☠</div> &nbsp;

**EDIT :** Nouvel article, qui explique comment [automatiser le lancement du script lors des _commits_]({filename}/git_hooks_pelican.md "Publier automatiquement ses nouveaux articles sur le moteur de blog Pelican avec Git").