Title: Édition vidéo — Formats et conversion de Pitivi à Lightworks
Date: 2014-12-01 00:23
Author: Quack1
Category: Geek
Tags: Vidéo, Pitivi, Lightworks, planet-libre
Slug: video_pitivi_lightworks
Summary: 
Lang: fr

J'ai commencé à monter quelques vidéos donc certaines sont [sur ce blog](/tag/video.html) et j'ai été vite limité par les outils libres disponibles.

J'avais testé [OpenShot](http://www.openshot.org/), sans succès, puis [PiTiVi]({filename}/pitivi_crowdfunding.md), que j'ai d'ailleurs soutenu, qui ne disposait pas de fonctions permettant d'accélérer ou ralentir des vidéos.

J'utilise donc désormais [Lightworks](http://www.lwks.com/) qui n'est pas libre mais qui propose une version Linux.

Je réalise tout de même certaines petites choses dans PiTiVi, c'est pourquoi je vais détailler ici les formats que j'utilise lors de l'export des vidéos dans PiTiVi, puis comment les convertir pour Lightworks.

# Création du projet

Je crée par défaut tous mes projets avec la plus grande résolution possible. Tant qu'à faire, autant faire les choses bien et à fond.

<div align=center><a href="/upload/pitivi_projet_video.png"><img src="/upload/pitivi_projet_video.png" align="center" height="250" /></a></div>

Je prend le preset `1080p24` que je modifie pour avoir du _120fps_ sur une résolution de 1920x1080 (ce dernier choix est par défaut).

<div align=center><a href="/upload/pitivi_projet_audio.png"><img src="/upload/pitivi_projet_audio.png" align="center" height="250" /></a></div>

Pas de changements sur la partie audio, je vérifie juste que le taux d’échantillonnage est également le plus élevé (en ce moment, c'est du 44.1kHz[^1])

# Le rendu

Quand j'exporte la vidéo, je modifie également légèrement les formats et codecs utilisés.

<div align=center><a href="/upload/pitivi_export_general.png"><img src="/upload/pitivi_export_general.png" align="center" height="250" /></a></div>

Je choisis un conteneur `Avi`, jusqu'ici c'est simple ;)

<div align=center><a href="/upload/pitivi_export_video.png"><img src="/upload/pitivi_export_video.png" align="center" height="250" /></a></div>

Ici aussi je vérifie bien que PiTiVi a gardé mon réglage en 120fps, puis je choisis le codex `x264enc`. Je ne sais pas vraiment pourquoi j'ai pris celui là plutôt qu'un autre, disons juste que la qualité de la vidéo n'est pas dégueulasse pour une taille de fichier assez light.

<div align=center><a href="/upload/pitivi_export_audio.png"><img src="/upload/pitivi_export_audio.png" align="center" height="250" /></a></div>

Pour l'audio, je le laisse en 44.1kHz avec le codec `A Law`.

# Conversion pour Lightworks

Tout aurait pu très bien se passer sauf que Lightworks ne reconnaît pas complètement les vidéos exportées par PiTiVi dans ce format. J'ai soit du son et pas de vidéo, soit de la vidéo mais pas de son. _FYI_, Lightworks reconnaît nativement [ces formats](http://lightworks.wikidot.com/formats).

J'utilise donc `avconv(1)` sur Linux et la ligne de commande suivante pour convertir les vidéos exportées par PiTiVi dans un format reconnu par LightWorks : 

	:::bash
	avconv -i {VIDEO_PITIVI} -c:v mpeg2video -pix_fmt yuv422p -g:v 1 -q:v 1 -qmin:v 1 -c:a mp2 -r:a 48000 -b:a 384k {VIDEO_OUTPUT}

Le détail des options est donné dans [cet article](http://www.dototot.com/convert-videos-for-import-into-lightworks-with-avconv/) sur lequel j'ai trouvé cette commande miracle :)

Et donc là, ça marche :)

_Pour ceux qui voudraient se lâcher dans les commentaires sur « faudrait utiliser ce logiciel plutôt que ça ou ça », je vous laisse vous amuser entre vous ;)_

[^1]: Avec la version 0.94 de PiTiVi