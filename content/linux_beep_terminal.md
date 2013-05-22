Title: Activer les notifications sonores dans une config 'irssi-screen-ssh', ou comment réactiver le 'bip' système sur GNU/Linux
Date: 2013-05-23 09:12
Author: Quack1
Category: Linux
Slug: linux_beep_terminal
Tags: Ubuntu, Linux, Beep, Terminal, planet-libre, planet-ubuntu
Summary: Script permettant de réactiver le 'bip' du terminal sur les systèmes GNU/Linux, et en particulier pour Ubuntu.
Lang: fr

&nbsp;
<div align=center><img src="static/upload/.png" width="600" height="250" align=center /></div>

Je vous présentais dans un article précédent [ma configuration IRC](|filename|/irssi-screen.md), composée d'un `irssi` lancé dans un `screen` distant. Je me connecte à mon hôte distant via ssh et je ré-attache ma session `screen`.

Cette configuration est parfaite et je l'utilise quotidiennement, mais j'ai toutefois un souci majeur : quand mon pseudo est mentionné, je ne reçois aucune notification, alors que mon client IRC devrait normalement 'bipper'.

# Irssi - screen - Terminal

Pour activer la notification dans `irssi` c'est très simple, et on retrouve cette configuration un peu partout sur le Ternaite (par exemple dans [la doc officielle](http://www.irssi.org/documentation/tips)).

	/set beep_when_window_active ON
	/set beep_when_away ON
	/set beep_msg_level MSGS NOTICES DCC DCCMSGS HILIGHT
	/set bell_beeps ON

Pour que `screen` active les notifications auditives, on fait des `Ctrl-A Ctrl-G` juqu'à voir s'afficher `Switched to Audible Bell` en bas de sa fenêtre `screen`.

Enfin, on vérifie que son terminal est bien configuré pour émettre des _beep_ auditifs.

- Dans Gnome-Terminal : _Edition_ --> _Préférences du Proil_ --> Cocher _"Bip" du Terminal_
- Dans Terminator : Clic-Droit --> _Preferences_ --> _Profiles_ --> Choisir son profil à gauche, puis --> _General_ --> Cocher _Audible beep_

Et normalement vous devez recevoir des notifications quand on vous mentionne sur IRC. Pour tester que la configuration de votre système **local** est bonne, tapez `echo -e '\a'` dans un shell. Vous devriez entendre le 'bip' défini.

# Et si ça marche pas...

Dans mon cas, ça n'a pas marché. Après beaucoup de recherches, notamment du côté de ma config `irssi/screen/ssh`, je me suis rendu le canal IRC d'`irssi` sur Freenode (#irssi@irc.freenode.net), et après avoir parlé avec plusieurs utilisateurs (poke deadweasel, billnye, Death4Life), j'ai cherché un peu plus du côté du système, et on m'a très justement fait remarquer que depuis une ancienne version d'Ubuntu (on ne sais pas vraiment laquelle), les bips systèmes sont désactivés du noyau, et on ne peut donc pas recevoir les notifications de notre client IRC.

Pour réactiver le module qui est blacklisté du système, un simple `sudo modprobe pcspkr` devrait suffir (je n'ai pas tapé la commande, je ne peux donc rien vous garantir).

Cette solution semblait avoir un gros inconvénient pour moi : les bips ne passaient pas par la carte son et donc n'étaient pas redirigés dans les écouteurs si ceux-ci étaient branchés. (Encore une fois, corrigez moi si je me trompe sur ce point, je n'ai pas testé). Sauf que moi, la journée au travail, j'ai pas vraiment envie que mon PC pousse des grands bips toutes les 5 minutes parce que j'ai été mentionné sur un chan, je préfère que tout ça aille direct dans mes écouteurs.

J'ai donc fouillé un peu plus et je suis tombé sur cette solution, qui consiste en fait à redéfinir au niveau du système le comportement à avoir quand le système doit éxécuter la fonction `Bell()`.

Pour cela, on installe le paquet suivant : 

	:::zsh
	╭────<quack@spiderman >───<  ~ >  
	╰───[18:09:57] $ sudo apt-get install vorbis-tools

Puis on crée le script suivant : 

	:::zsh
	╭────<quack@spiderman >───<  ~ >  
	╰───[18:10:32] $ cat ~/.xkb/xkbevd.cf          
	soundDirectory="/usr/share/sounds/"
	soundCmd="ogg123 -q"
	Bell() "ubuntu/stereo/message-new-instant.ogg"

Ceci signifie que lorsqu'un 'Beep' système devra être lancé, le système éxécutera à la place la commande suivante : 

	:::zsh
	ogg123 -q /usr/share/sounds/ubuntu/stereo/message-new-instant.ogg

Si vous voulez personnaliser le son que vous recevez, il vous suffit de modifier les variables `soundDirectory` et la variable située après le `Bell()` dans le code ;-)

Enfin, on rajoute un programme à lancer lorsque je me connecte (ici j'ai fait ça simplement, en mode graphique).

<div align=center><a href="static/upload/beep_1.png"><img src="static/upload/beep_1.png" align="center" /></a></div>

<div align=center><a href="static/upload/beep_2.png"><img src="static/upload/beep_2.png" align="center" /></a></div>

Pour que les modifications soient effectives sans avoir à vous re-logguer la première fois, lancez : 

	:::zsh
	xkbevd -bg

Et voilà, vous devriez recevoir des 'beeps' dès que votre Terminal envoie un signal auditif, et notamment dans `irssi` ! ;-D