Title: Corriger le bug de l'icone de Gimp 2.8 perdue dans le Launcher d'Unity
Date: 2012-05-20 22:04
Author: Quack1
Category: Ubuntu
Tags: Gimp, Icone, Ubuntu, Unity, planet-libre, planet-ubuntu
Summary: Retrouver l'icône de la dernière version de Gimp dans le Launcher d'Unity.

![Gimp](static/upload/gimp.png "Gimp")

J'ai récemment fait la mise à jour de Gimp 2.8 grâce au PPA des
développeurs. Je vais faire l'impasse sur les nouveautés de cette
version, je ne suis pas assez bon graphiste pour voir les différences
avec l'ancienne ;-)

Une des différences que j'ai par contre pu observer, c'est que j'avais
perdu l'icône de Gimp dans le Launcher d'Unity quand je lançais Gimp. Le
bug viendrait (semble-t-il) d'un conflit entre les deux versions (2.6 et
2.8 qui cohabitent sur mon système).

Le bug aurait été signalé au développeurs, mais voici quand même une
solution pour le corriger avant la mise à jour du logiciel.

Modifiez le fichier /usr/share/applications/gimp.desktop :

<pre>
    gksudo gedit /usr/share/applications/gimp.desktop
</pre>

et remplacez tout son contenu par :

<pre>
     [Desktop Entry] Version=1.0 Type=Application Name=Gimp 2.8 Comment=Create images and edit photographs Exec=/usr/bin/gimp-2.8 %U TryExec=/usr/bin/gimp-2.8 Icon=gimp Terminal=false Categories=Graphics;2DGraphics;RasterGraphics;GTK; X-GNOME-Bugzilla-Bugzilla=GNOME X-GNOME-Bugzilla-Product=GIMP X-GNOME-Bugzilla-Component=General X-GNOME-Bugzilla-Version=2.8.0 X-GNOME-Bugzilla-OtherBinaries=gimp-2.8 MimeType=application/postscript;application/pdf;image/bmp;image/g3fax;image/gif;image/x-fits;image/pcx;image/x-portable-anymap;image/x-portable-bitmap;image/x-portable-graymap;image/x-portable-pixmap;image/x-psd;image/x-sgi;image/x-tga;image/x-xbitmap;image/x-xwindowdump;image/x-xcf;image/x-compressed-xcf;image/x-gimp-gbr;image/x-gimp-pat;image/x-gimp-gih;image/tiff;image/jpeg;image/x-psp;image/png;image/x-icon;image/x-xpixmap;image/svg+xml;application/pdf;image/x-wmf;image/jp2;image/jpeg2000;image/jpx;image/x-xcursor;
</pre>

Et normalement, vous retrouverez l'icône dans le dock ;-)

[Source](http://www.taltan.fr/post/2012/05/19/Regler-le-bug-de-l-icone-Gimp-invisible-dans-le-lanceur-lateral-sous-Ubuntu-12.04 "Icone Gimp")
