Title: Intégration de sous-titres sur une vidéo sous Ubuntu/Linux
Date: 2011-11-25 17:39
Author: Quack1
Category: Ubuntu
Tags: ffmpeg, mencoder, sous-titres, ubuntu, video, planet-libre
Summary: Intégrer facilement des sous-titres sur une vidéo depuis un système GNU/Linux avec ffmpeg

Petit billet pour voir comment intégrer des sous titres sur une vidéo
sur Ubuntu.

Nous allons utiliser un petit logiciel en ligne de commande, mencoder,
qui est inclut dans le logiciel mplayer (qui, lui, permet de lire des
vidéos directement depuis la ligne de commande). On peut installer
mencoder directement depuis apt [ici][].

De plus, le logiciel ffmpeg est assez utile, pour récupérer des
informations sur la vidéo, et il est aussi indispensable à mencoder.

Pour installer les deux logiciels depuis la ligne de commande, tapez :

<pre>
sudo apt-get install ffmpeg mencoder
</pre>

L'utilisation de mencoder est très simple. Il suffit de lui passer en
argument la vidéo originale, le fichier de sous-titres et le nom du
fichier à créer. On peut également rajouter quelques options concernant
l'encodage de la vidéo, du son, ainsi que des options concernant le
format du sous titre.

Voici la ligne de commande que j'utilise :

<pre>
mencoder video_originale.avi -sub fichier_sous_titre.srt -fontconfig -font Arial -subfont-text-scale 4 -utf8 -oac mp3lame -lameopts br=128 -ovc xvid -xvidencopts bitrate=1200 -o video_sous_titrée.avi
</pre>

Il ne reste plus qu'à faire *Entrée* et le tour est joué ;) 

Voici le détail des options (vous trouverez plus d'infos dans la page de
manuel ou sur [le net][]). Je rappelle que ce sont les options que
j'utilise personnellement. Beaucoup d'autres sont dispo dans le manuel
;) :

<pre>
-fontconfig -font Arial
</pre>

On donne ici la police de caractères à utiliser. Dans ce cas, Arial. (Ca
reste quelque chose de basique, mais ça rend très bien pour des
sous-titres :P)

<pre>
-subfont-text-scale 4
</pre>

On défini ici la taille des sous-titres. Attention, cela correspond au
pourcentage de la taille de l'écran. Dans mon cas, les lettres feront 4%
de la taille de la vidéo.

<pre>
-utf8
</pre>

Le format d'encodage des caractères, pour éviter d'avoir des mauvaises
surprises sur la vidéo finale.

<pre>
-oac mp3lame
</pre>
Ici, on défini l'*Output Audio Codec* : donc Lame, implémentation
open-source du format MP3.

<pre>
-lameopts br=128
</pre>

Les options spécifiques à Lame : je donne juste le *bitrate* que je
souhaite avoir, soit 128kbps.

<pre>
-ovc xvid
</pre>

Ici, c'est comme plus haut, sauf que cela concerne la vidéo (*Output
Video Codec*). Du Xvid, ça rest standard pour des bonnes vidéos ;)

<pre>
-xvidencopts bitrate=1200
</pre>

Et maintenant les options spécifiques à Xvid. Comme pour Lame, je donne
juste le *bitr
ate* de ma vidéo : 1200kbps.
 
Et voilà, vous êtes prêt à intégrer vos sous titres sur vos vidéos!! Si
vous souhaitez éditer facilement vos sous-titres, en voyant votre vidéo
en même temps pour avoir un meilleur rendu, vous pouvez utiliser
[Gnome-Subtitles][](comme son nom l'indique, il est fait pour Gnome,
mais il devrait sûrement fonctionner sur Kde ou Xfce ;) )

  [ici]: apt://mencoder "ici"
  [le net]: http://doc.ubuntu-fr.org/mencoder "le net"
  [Gnome-Subtitles]: http://doc.ubuntu-fr.org/gnome-subtitles "Gnome-Subtitles"
