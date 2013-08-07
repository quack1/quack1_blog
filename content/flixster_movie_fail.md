Title: Téléchargement légal de films achetés en DVD ? C'est pas pour tout de suite...
Date: 2013-08-07 13:47
Author: Quack1
Category: Geek
Tags: VOD, Flixster, planet-libre
Slug: flixster_movie_fail
Summary: 

&nbsp;
<div align=center><img src="static/upload/hobbit_large.png" align=center height="250"/></div>

Quand j'ai eu mon DVD du [Hobbit](http://fr.wikipedia.org/wiki/Le_Hobbit_%28films_de_Peter_Jackson%29), j'ai pu y découvrir un petit papier avec un code pour que je puisse bénéficier du film en version numérique à télécharger et regarder partout, c'est à dire sur mon smartphone, ma tablette, mon ordinateur, etc...

J'ai bien kiffé ça pour 2 raisons : 

1. Ça fait du bien de voir que les producteurs s'intéressent (enfin) au numérique, et fournissent une version dématérialisée pour tout achat d'un DVD ;
2. J'ai un [Raspberry Pi](http://quack1.me/tag/raspberry-pi.html) qui me sert de Media Center. Quand je veux regarder un DVD, je trouve chiant de devoir brancher un PC en HDMI sur la télé, alors que j'ai mon raspi qui est, à la base, là pour ça. 

Du coup, télécharger une vidéo et la balancer sur le disque dur du Raspberry pour pouvoir regarder légalement mon film sur ma télé, c'est quand même pas mal.

Me voilà donc embarqué dans un _voyage innatendu_.

&nbsp;

Première chose à faire, me rendre sur [flixster.com](http://www.flixster.com), et y créer un compte. Ceci fait, je peux ajouter &laquo;Le Hobbit&raquo; à ma collection de vidéos en tapant le code obtenu dans la boîte du DVD.

Problème, le site bugue dans Firefox (pourtant en Nightly, c'est à dire la version 25). Obligé de passer sur Chromium pour utiliser le site. Premier mauvais point. Mais bon, j'ai quand même envie d'avoir le film, donc je continue.

Je navigue dans les différents menus, j'arrive jusqu'à la page du film, je clique sur &laquo;Téléchargement&raquo;, et là, c'est le drame.

<div align=center><a href="static/upload/flixster_adobe_air.png"><img src="static/upload/flixster_adobe_air.png" width="600" align=center /></a></div>

C'est pas possible d'avoir juste un lien de téléchargement depuis leur [CDN](http://fr.wikipedia.org/wiki/Content_Delivery_Network) pour avoir mon film ?

Bon, là, vous devez commencer à vous douter que j'ai commencé à en avoir marre. Mais j'avais aussi **vraiment** envie d'avoir mon petit film. Après tout, j'installe Adobe Air (qui n'est plus supporté pour Linux depuis 3 ans...) et leur appli pourrie, je télécharge un `.avi`, et basta!, je désinstalle tout après.

Bon, sauf qu'en fait, non, ce serait trop facile.

La vidéo que j'ai téléchargé fait 2,5Go. Niveau qualité ça doit être pas mal, sûrement de la HD. Je note quand même un truc bizarre. L'application ne me demande pas où je veux sauvegarder le fichier. 

Là, je me dis qu'il doit vouloir que je passe obligatoirement par leur soft pour la visionner. Qu'à cela ne tienne, un petit `find ~ -type f -name '*HOBBIT*'` me renvoie un fichier dans le répertoire local de Flixster : `/home/quack/.appdata/com.wb.DC2/Local Store/`

Le fichier se nomme `1375380298181DC2_UV_E06349FR_HOBBIT_THE_FRENCH_main_FAXS_2000k_dl.mp4`. On dirait presque le nom d'un rip sur [The Pirate Bay](thepiratebay.sx).

J'attend patiemment la fin du téléchargement, et j'essaye de lire le fichier avec VLC, et impossible de voir la vidéo. 

Je fais quelques recherches sur Internet, et je me rend compte qu'en fait ma vidéo est [équipée de DRM qui limite son visionnage](http://arstechnica.com/gadgets/2011/11/your-movie-on-every-platform-sort-of-for-a-while-how-the-new-ultraviolet-drm-fails/). 

En définitive, je ne peux visionner le film qu'à partir de l'application Flixster. C'est mort pour que je puisse la visionner depuis mon Raspberry Pi qui n'a pas d'interface graphique.

&nbsp;

Finalement, ça me fait quand même un peu chier de pas avoir pu acquérir **légalement** une copie de mon film. Je vais devoir choper un rip de Blu-Ray ou de DVD en [P2P](http://quack1.me/tag/p2p.html) pour pouvoir le voir sur mon Raspberry Pi.

Pourtant l'initiative était super bonne. Je suis à fond pour ce genre de pratique. Filer une version numérique pour tout achat d'une version physique, c'est méga bon pour le confort de l'utilisateur, et ça donne envie de revenir acheter. Personnellement je télécharge en partie parce que les DVD sont chers, et en partie parce que ça me casse les couilles de ripper 24 épisodes de séries un par un pour pouvoir les matter sur ma télé depuis un mini ordinateur à 35 balles.

Si j'avais accès facilement à la version numérique **sans DRM** de ce que j'achète, je le ferais beaucoup plus souvent.

Donc, en conclusion, acheter des DVD, c'est bien, mais ça ne nous empêchera pas de télécharger. Il faut que tout le monde, y compris les producteurs/vendeurs y mettent du leur!