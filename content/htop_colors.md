Title: Signification des couleurs dans htop
Date: 2014-01-06 13:08
Author: Quack1
Category: Ubuntu
Tags: Linux, Ubuntu, Sysdamin, Htop, Supervision, planet-libre, planet-ubuntu
Slug: htop_colors
Summary: 
Lang: fr
Status: draft

C'est tout bête, mais quand on ne le sait pas on se retrouve un peu comme un con devant son écran quand on supervise une de ses machines. [Htop](http://htop.sourceforge.net/), le célèbre programme en ligne de commande permettant de superviser les ressources d'une machine Linux affiche en haut de sa « fenêtre » des barres qui affichent le pourcentage des ressources utilisées sur le système. 

<div align=center><a href="/upload/htop_bars.png"><img src="/upload/htop_bars.png" align="center" width="372" height="118" /></a></div>

Pour cela, il utilise plusieurs couleurs, notamment le vert et le rouge. Au début, je pensais que la barre devenait rouge quand un des coeurs du CPU était trop utilisé, ou avait un _load average_ trop important.

En fait, pas du tout. En cherchant un peu sur le net, je suis tombé sur [ce post de Server Fault](http://serverfault.com/questions/180711/what-exactly-do-the-colors-in-htop-status-bars-mean) et en fait les couleurs ne correspondent pas **du tout** à ça : 

Pour le CPU, 3 couleurs sont utilisées : 

- Le bleu pour les threads à faible priorité ;
- Le vert pour les threads normaux ;
- Le rouge pour les threads du kernel.

Du coup, plus vous avez de vert, plus il y a de threads _normaux_ qui tournent sur un CPU. Idem pour la mémoire et la swap utilisée. 

Et, comme htop est pas con, une aide est disponible en appuyant sur `h` : 

<div align=center><a href="/upload/htop_help.png"><img src="/upload/htop_help.png" align="center" width="471" height="85" /></a></div>

Voilà, c'est tout con comme truc, mais quand tu le sais pas tu te sens un peu con devant ton écran !