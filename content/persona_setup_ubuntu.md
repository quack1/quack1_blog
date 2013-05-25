Title: Mettre en place un Environnement de Développement pour Mozilla Persona
Date: 2013-05-24 21:37
Author: Quack1
Category: Mozilla
Slug: persona_setup_ubuntu
Tags: Linux, Ubuntu, Mozilla, Persona, Dev, Nodejs, planet-libre, planet-ubuntu
Summary: Étapes permettant de mettre en place facilement un environnement de développement pour contribuer au projet Mozilla Persona (browserid) sur Ubuntu 13.04
Lang: fr

&nbsp;
<div align=center><img src="static/upload/persona.png" align=center /></div>

Depuis plusieurs années, j'ai envie de contribuer à un projet Open-Source. Aujourd'hui, les choses commencent à devenir réalité. J'ai trouvé **le** projet que je veux aider : [Mozilla Persona](https://login.persona.org/about "Mozilla Persona About Page"). Mais je fais les choses dans le désordre puisque j'écrirais bientôt un article pour vous le présenter un peu mieux.

Ici, je vais détailler les étapes pour se monter un environnement de développement complet sur un système GNU/Linux, et plus précisément sur Ubuntu 13.04.

# Devenir pote avec GitHub

La première chose à faire avant de contribuer est de s'inscrire sur [GitHub](https://github.com "Github.com"), et forker le projet, disponible à [https://github.com/mozilla/browserid](https://github.com/mozilla/browserid "GitHub Mozilla/browserid").

Quand vous avez fait ça, clonez le répertoire sur votre machine :

	:::zsh
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla >
	╰───[18:11:29] $ git clone https://github.com/quack1/browserid.git

Puis, rendez vous dans ce répertoire pour y rajouter un nouveau _remote_. Celui-ci sera le _repository_ _"officiel"_ à partir duquel on récupérera les mises à jour du code : 

	:::zsh
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla >
	╰───[18:13:49] $ cd browserid 
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev› 
	╰───[18:13:55] $ git remote add mozilla https://github.com/mozilla/browserid.git

De cette façon, pour se mettre à jour, on fera simplement : 

	:::zsh
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev› 
	╰───[18:14:12] $ git pull mozilla dev

Et, pour pousser nos modifications sur notre dépôt :

	:::zsh
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev› 
	╰───[18:14:20] $ git push origin dev

On proposera nos commits à l'équipe de développement au travers du système de Pull Request inclut dans GitHub.

# Travailler avec Nodejs

Persona étant écrit en [Node.js](http://nodejs.org/ "Node.js Website") pour les parties serveur, on doit l'installer pour pouvoir tester notre code.

Cependant, avant cela, on doit installer quelques autres outils : 

	:::zsh
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev› 
	╰───[18:15:02] $ sudo apt-get install python-software-properties git-core libgmp3-dev g++ libssl-dev

Maintenant, on peut donc installer NodeJs. Mais surtout, n'installez **pas** nodejs directement depuis les depôts d'Ubuntu ou depuis les sources du site officiel, puisque la version currente est en 0.10.*, et Persona n'est compatible qu'avec les 0.8.* pour le moment.

La meilleure façon de faire m'a été donnée par [Shane Tomlinson](https://twitter.com/Shane_Tomlinson "Shane Tomlinson Twitter Page"), et elle consiste à déléguer la gestion des versions de Node.js installées sur le système à un simple programme : **nvm**. Ce dernier peut installer plusieurs versions de Node, et il est ensuite possible de lui préciser quelle version utiliser.

Pour l'installer, suivez les [instructions disponibles sur le site officiel](https://github.com/creationix/nvm/). Pour faire simple, voici les commandes à taper :  

	:::zsh
	╭────<quack@spiderman >───<  ~/work/softs > 
	╰───[18:17:47] $ git clone http://github.com/creationix/nvm.git nvm
	╭────<quack@spiderman >───<  ~/work/softs > 
	╰───[18:17:58] $ echo '. /home/quack/work/softs/nvm/nvm.sh' > ~/.zshrc

N'oubliez pas de modifier la dernière commande pour coller à l'emplacement où vous avez cloné les sources et à l'emplacement du fichier de configuration de votre shell (par défaut, sur Ubuntu, c'est `~/.bashrc`). Démarrez un nouveau terminal et la commande `nvm` devrait marcher.

Après ceci, installez la dernière version de Node.js supportée, et définissez la comme version par défaut :

	:::zsh
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev› 
	╰───[18:19:30] $ nvm install 0.8.12
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev› 
	╰───[18:19:49] $ nvm alias default 0.8.12

Maintenant, vous pouvez installez tous les modules Node.JS nécéssaires à Persona. Déplacez vous dans le répertoire racine où vous avez cloné `browserid`, et lancez la commande suivante :

	:::zsh
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev› 
	╰───[18:20:15] $ npm install

Et, normallement, tous les modules sont installés et vous pouvez travailler! Si vous voulez lancer les exemples donnés dans les sources :

	:::zsh
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev› 
	╰───[18:20:20] $ npm start

L'application Web d'exemple est accessible à [http://localhost:10001](http://localhost:10001), et le serveur Browserid est à [http://localhost:10002](http://localhost:10002).

# Mais le module `bcrypt` ne marche pas...

Si, durant le `npm install`, vous avez une erreur du type _"Impossible d'installer le module 'bcrypt'"_, essayez d'importer la bonne version directement : 

	:::zsh
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev› 
	╰───[18:20:20] $ npm install bcrypt@0.7.3

Refaites un `npm install`, et si ça ne marche toujours pas, nous allons essayer de l'installer manuellement.

Pour faire simple, les commandes suivantes vont : cloner les sources, configurer la compilation, compiler les sources, et ré-installer _bcrypt_ avec npm.

	:::zsh
	╭────<quack@spiderman >───<  /tmp > 
	╰───[18:20:20] $ git clone http://github.com/ncb000gt/node.bcrypt.js.git
	╭────<quack@spiderman >───<  /tmp > 
	╰───[18:21:20] $ cd node.bcrypt.js
	╭────<quack@spiderman >───<  /tmp > 
	╰───[18:22:20] $ npm install -g node-gyp
	╭────<quack@spiderman >───<  /tmp > 
	╰───[18:23:20] $ node-gyp configure
	╭────<quack@spiderman >───<  /tmp > 
	╰───[18:24:20] $ node-gyp build
	╭────<quack@spiderman >───<  /tmp > 
	╰───[18:25:20] $ cd ~/work/workspace/mozilla/browserid
	╭────<quack@spiderman >───<  /tmp > 
	╰───[18:25:22] $ rm -rf var node_modules
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev› 
	╰───[18:26:20] $ npm install

Normallement, après cette dernière étape, tout devrait normalement marcher avec un `npm start`.

# Mettre à jour ses sources

Désormais, à chaque fois que vous voudrez mettre à jour vos sources, vous devrez réinstaller les modules Node pour utiliser les dernières versions demandées par Persona.

Le processus de mise à jour sera donc :

	:::zsh
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev›  
	╰───[18:23:20] $ git pull mozilla dev
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev›  
	╰───[18:31:20] $ rm -rf var node_modules
	╭────<quack@spiderman >───<  ~/work/workspace/mozilla/browserid >  ‹dev› 
	╰───[18:32:20] $ npm install

Et voilà, il est temps de travailler sur le code maintenant!

&nbsp;

_ Si vous trouvez quelques fautes, ou si vous voulez plus de précisions, n'hésitez pas à m'envoyer un [email](quack1blog@gmail.com),  me contacter sur [Twitter](http://twitter.com/_Quack1), ou à joindre le canal IRC de l'équipe Identity : [#identity@irc.mozilla.org](irc://irc.mozilla.org/identity). Les mecs qui en font partie et qui travaille sur Persona sont tous supers cools et toujours près à vous aider!_

Un merci tout particulier à [Shane Tomlinson](https://shanetomlinson.com/ "Shane Tomlinson Personal Website") qui a passé tout son samedi après midi sur IRC à m'aider à installer cet environnement!

Pour plus d'infos, vous avez également le [README disponible sur le dépôt GitHub du projet](https://github.com/mozilla/browserid/blob/dev/README.md)