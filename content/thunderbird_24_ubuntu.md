Title: Installer et utiliser la bêta de Thunderbird 24 sur Ubuntu
Date: 2013-09-02 16:40
Author: Quack1
Category: Ubuntu
Tags: Ubuntu, planet-libre, planet-ubuntu, Mozilla, Thunderbird, Unity
Slug: thunderbird_24_ubuntu
Summary: 

&nbsp;
<div align=center><img src="http://farm3.staticflickr.com/2247/2435710014_72832fb0e9_b.jpg" height="250" align=center /></div>

En début de mois dernier, Mozilla a lancé [la phase de tests pour la prochiane mouture de son client mail](http://blogzinet.free.fr/blog/index.php?post/2013/08/16/Semaine-de-tests-%3A-Mozilla-Thunderbird-24-beta-%28prochaine-version-ESR%29) Thunderbird.

Cette prochaine version majeure (qui doit remplacer la version 17 actuellement packagée dans les dépôts d'Ubuntu,si je ne m'abuse) sortira le 17 septembre et apportera énormément de nouvelles fonctionnalités ainsi que des corrections de bugs.

L'installation sur Ubuntu est simple : télécharger l'[archive correspondant à votre langue](http://www.mozilla.org/en-US/thunderbird/all-beta.html), puis extraire les fichiers. Chez moi, cette nouvelle version est dans `/opt/thunderbird`.

Le problème que j'ai est que pour le lancer, je dois taper dans un terminal :

	:::zsh
	╭────<quack@spiderman >───<  ~ > 
	╰───[15:10:11] $ /opt/thunderbird/thunderbird &

Et quand je clique sur l'icône de Thunderbird dans le dock, la version 17 est lancée. Ce serait plus simple que le clic que l'icône du Dash lance la version bêta, plutôt que l'ancienne version.

Pour cela, il faut modifier le fichier `*.desktop` qui permet de créer ces raccourcis dans le Dash.

Celui de Thunderbird se trouve dans : 

	:::zsh
	╭────<quack@spiderman >───<  ~ > 
	╰───[15:40:05] $ locate thunderbird.desktop
	/usr/share/applications/thunderbird.desktop

On le modifie, en changeant toutes les variables `Exec=XXX`, qui contiennent le chemin de l'ancien exécutable, vers le chemin d'accès à l'exécutable de la version bêta!

	:::ini
	[Desktop Entry]
	...
	Exec=/opt/thunderbird/thunderbird %u
	...

	[Desktop Action Compose]
	...
	Exec=/opt/thunderbird/thunderbird -compose
	...

	[Desktop Action Contacts]
	...
	Exec=/opt/thunderbird/thunderbird -addressbook
	...

Et désormais, le lanceur d'applications du Dash d'Ubuntu lancera la version bêta de Thunderbird au lieu de la version installée par défaut sur Ubuntu.

[Image source](http://www.flickr.com/photos/hmclin/2435710014/)