Title: Désactiver l'arrêt du son avec lightlocker sur XUbuntu 14.04
Date: 2014-09-29 10:22
Author: Quack1
Category: Ubuntu
Tags: Ubuntu, XUbuntu, Lightlocker, planet-libre, planet-ubuntu
Slug: lightlocker_sound
Summary: 
Lang: fr

Depuis la version 14.04, [XUbuntu](http://xubuntu.org) utilise un nouvel outil de verrouillage d'écran : [LightLocker](xubuntu.org/news/screen-locking-in-xubuntu-14-04/).

LightLocker marche plutôt bien mais a un défaut assez gênant. Quand l'écran est verrouillé, le son qui tournait en fond est stoppé. L'équipe d'XUbuntu a une — bonne ? — raison à cela : 

> Currently, when locking, it is assumed you are either:
>
>   in a public space of sorts (the desktop at home hardly needs locking) and have walked away from the machine
>   using a system with more than one user

En gros, si votre session se verrouille, c'est qu'il y a de fortes chances que vous soyez dans un endroit public et donc il est préférable de couper le son. L'idée n'est pas trop con mais moi, je bosse pas toujours sur mon PC. Par contre, j'écoute quasiment toujours de la musique dessus. Donc couper la musique dès que l'écran se verrouille c'est un peu chiant.

Heureusement, une solution « officielle » est fournie sur le blog d'XUbuntu !

On peut, au choix :

- Demander à lightlocker de ne verrouiller la session que lorsque « l'écran de veille est désactivé » ;
- Désactiver lightlicker pour repasser sur _xscreensaver_ ;
- Ajouter son utilisateur au groupe _audio_.

<div align=center><a href="/upload/lightlocker.png"><img src="/upload/lightlocker.png" align="center" /></a> <br /> « Paramètres de Lightlocker » puis « Automatically lock the session when... »</div>

J'ai utilisé les deux premières solutions. Je ne sais pas trop les retombées de la première niveau sécurité (de ce que je comprend, l'écran est simplement noir mais pas verrouillé, et ne se verrouille que lorsque l'écran de veille s'arrête..), mais pour le moment ça fait le job :)


