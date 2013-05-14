Title: Git : Pusher ses modifications sur plusieurs dépôts en une seule commande
Date: 2013-05-14 19:12
Author: Quack1
Category: Geek
Slug: git_push_multiple_remote
Tags: Dev, Git, planet-libre
Summary: Pusher ses modifications sur plusieurs repositories git distants en une seule commande.

Si, pour des questions de résilience et de backup, vous avez plusieurs dépôts distants configurés dans votre projet git, vous devez lancer plusieurs commandes pour pousser vos modifications sur chacun de ses dépôts.

	:::bash
	quack@spiderman $ git push # Depot "master"
	quack@spiderman $ git push remote2 master
	quack@spiderman $ git push remote3 master

J'ai trouvé ce matin l'astuce pour pusher automatiquement sur plusieurs _remotes_. Prenons le cas où j'ai 2 dépôts distants configurés : `http://remote1` et `git@remote2:depot.git`. On va

1. Créer un nouveau _remote_ avec la première url
2. Ajouter une url au _remote_ nouvellement créé
3. Repeter l'étape 2 pour tous les dépôts distants à rajouter

Ce qui nous donne : 

	:::bash
	quack@spiderman $ git remote add multiple http://remote1
	quack@spiderman $ git remote set-url --add multiple git@remote2:depot.git

Ensuite, pour pusher les modifications : 

	:::bash
	quack@spiderman $ git push multiple master

Et si vous voulez pouvoir pusher automatiquement sur ce nouveau _remote_ simplement par un git push : 
	
	:::bash
	quack@spiderman $ git push -u multiple master

[Source](http://stackoverflow.com/questions/5785549/able-to-push-to-all-git-remotes-with-the-one-command)