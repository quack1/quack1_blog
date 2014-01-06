Title: Publier automatiquement ses nouveaux articles sur le moteur de blog Pelican avec Git
Date: 2013-11-05 18:43 
Author: Quack1
Category: Blog
Tags: Blog, Pelican, Python, Git, planet-libre, planet-ubuntu, pelican_auto_tweet
Slug: git_hooks_pelican
Summary: 

<a href="https://github.com/quack1/pelican_auto_tweet"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_right_darkblue_121621.png" alt="Fork me on GitHub"></a>

&nbsp;
<div align=center><img src="http://blog.quack1.me/upload/pelican_auto_tweet.png" width="600" height="250" align=center /></div>

J'ai parlé récemment d'un [script qui permet de poster automatiquement un tweet]({filename}/pelican_auto_tweet.md "Moteur de blog Pelican : twitter un lien automatique vers son dernier article") quand je publie un nouvel article sur le blog.

Ce script a été un peu modifié puisqu'il fait aujourd'hui 4 choses : 

1. Il vérifie si un nouvel article a été écrit (en cherchant la présence du message `[POST]` au début du message de _commit_ [Git](http://blog.quack1.me/tag/git.html "Blog Quack1 - Tag « Git »")) ;
2. Dans ce cas, il envoie les nouveaux _commits_ sur [le dépôt Git défini par défaut]({filename}/git_push_multiple_remote.md "Git : Pusher ses modifications sur plusieurs dépôts en une seule commande") ;
3. Il met à jour le blog sur le serveur via SSH (commande `make ssh_upload` pour les _Pelican-eux_) ;
4. Il envoie un tweet.

Tout ça c'est sympa, mais c'est un peu con d'automatiser toutes ces étapes si il faut au final lancer le script à la main. La magie de Git fait qu'on peut automatiser tout ça en utilisant les [_hooks_ de Git](http://www.johan.me/utilisez-hooks-git "Utilisez les hooks de Git").

Ces _[hooks](http://git-scm.com/book/en/Customizing-Git-Git-Hooks "Customizing Git Hooks")_ sont des scripts que Git lance après (ou avant) certaines étapes de son processus. Ils sont listés dans le répertoire `.git/hooks/` : 

	:::zsh
	╭────<quack@spiderman >───<  ~/Documents/writing/blog/quack1_pelican >  ‹master*› 
	╰───[18:52:40] $ ls .git/hooks 
	applypatch-msg.sample  post-commit         pre-applypatch.sample  prepare-commit-msg.sample  update.sample
	commit-msg.sample      post-update.sample  pre-commit.sample      pre-rebase.sample

Je ne vais pas tous les faire, les noms sont assez explicites, mais par exemple `pre-commit` est lancé avant le _commit_.

Mon script a besoin que le _commit_ soit terminé, donc j'ai fait pointer le fichier `.git/hooks/post-commit` sur le script. Toute la configuration nécessaire est placée dans le fichier de conf, donc le script se lance sans souci : 

	:::zsh
	╭────<quack@spiderman >───<  ~/Documents/writing/blog/quack1_pelican >  ‹master*› 
	╰───[18:53:14] $ ln -s ~/work/workspace/python/pelican_auto_tweet/pelican_auto_tweet.py .git/hooks/post-commit

Désormais dès que vous ferez un commit dans ce dépôt Git, le script se lancera et si toutes les conditions sont réunies, votre blog se mettra à jour, et un tweet sera posté !

<div align="center" style="color:#ccc;">☠</div> &nbsp;

_Le dépôt [GitHub](https://github.com/quack1/pelican_auto_tweet "Github : Quack1 - Pelican_Auto_Tweet") du projet est à jour, et possède déjà quelques_ issues _que j'avais trouvé sur les scripts et que je dois corriger. Si vous utilisez les scripts, et que vous trouvez des bugs, n'hésitez pas à me les remonter, je corrigerais ça rapidement !_

