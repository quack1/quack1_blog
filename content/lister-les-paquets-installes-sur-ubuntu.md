Title: Lister les paquets installés sur Ubuntu
Date: 2012-03-28 17:18
Author: Quack1
Category: Ubuntu
Tags: dpkg, installés, lister, packages, ubuntu, planet-libre, planet-ubuntu
Summary: Lister les paquets installés sur une distribution GNU/Linux.

<div align=center><img src="static/upload/listpackages.png" height="250" align=center /></div>

Petite commande utile, pour voir quels sont les packages qui sont
installés sur votre machine, pour générer un script de réinstall à
l'arrache par exemple, ou pour avoir une base.

On va utiliser la commande *dpkg-query*, qui permet d'interroger la base
de données des paquetages installés.

<pre>
sudo dpkg-query -Wf '${Installed-Size} - ${Package} n' | sort -n
</pre>
On prend tous les paquets installés, en filtrant la sortie avec un
format, qui n'affichera que la taille installée, ainsi que le nom. Le
*sort* permet de trier par ordre croissant de taille.

[Source][]

  [Source]: http://thecybergal.blogspot.fr/2012/03/list-installed-packages-in-ubuntu.html?utm_source=twitterfeed&utm_medium=twitter "http://thecybergal.blogspot.fr/2012/03/list-installed-packages-in-ubuntu.html?utm_source=twitterfeed&utm_medium=twitter"
