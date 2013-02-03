Title: Libérer la mémoire inutilisée de votre système GNU/Linux
Date: 2013-01-23 09:13
Author: Quack1
Category: Linux
Slug: free_unused_memory_linux
Tags: libérer, RAM, Linux, planet-libre

<div align=center><img src="static/upload/clean_memory.png" width="600" height="250" align=center /></div>

Article rapide aujourd'hui pour me souvenir d'une comamnde qui permet de libérer la mémoire inutilisée et non libérée par votre système, et en particulier par le kernel GNU/Linux.

Pas de logiciel à installer, ni de choses tordues et incompréhensibles à faire, juste une commande standard d'administration à lancer : 

	quack@spiderman:$ sysctl -w vm.drop_caches=3

Cela va demander au kernel de vider toutes ses pages de cache qui contiennent des données non utilisés.

C'est assez impressionant, et ça permet de libérer dans certains cas beaucoup de RAM. On peut voir ici qu'au moment du lancement de la commande, la quantité de mémoire (physique et virtuelle (SWAP)) utilisée diminue "fortement".

<div align=center><a href="static/upload/clean_memory_3.png"><img src="static/upload/clean_memory_3.png" align="center"/></a></div>

Screencast pris à l'arrache de l'éxecution de la commande sur mon système : 
<div align=center><iframe width="560" height="315" src="http://www.youtube.com/embed/atgL9clQcBc" frameborder="0" allowfullscreen></iframe></div>

Pour automatiser le processus, on peut rajouter la commande dans une tâche cron qui sera appelée toutes les heures, comme ici : 

	0 * 	* * * 	root	/sbin/sysctl -w vm.drop_caches=3 > /dev/null 2>&1

[Source](http://www.upubuntu.com/2013/01/how-to-free-up-unused-memory-in.html)
