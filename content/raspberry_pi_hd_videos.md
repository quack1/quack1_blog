Title: Lire des vidéos HD sur un Raspberry Pi
Date: 2013-04-18 17:21
Author: Quack1
Category: Linux
Slug: raspberry_pi_hd_videos
Tags: raspberry pi, video, hd, h264, 720p, omxplayer

Article très court pour partager une astuce que j'ai mis assez longtemps à trouver. Petite mise en situation : j'ai chez moi un [Raspberry Pi modèle B](http://www.kubii.fr/ "Kubii.fr : Acheter un Raspberry Pi") qui fait office de serveur web et me permet d'avoir un proxy SOCKS gratuit et léger chez moi. Pour ces raisons, j'y ai installé [Raspbian](http://www.raspbian.org/ "Site de Raspbian"), en configuration _headless_ (comprenez "sans interface graphique"), afin de gagner en performance.

Je m'en sers également pour regarder des vidéos sur ma télé, branchée au Raspberry en hdmi, depuis mon disque dur externe. La commande pour lire les vidéos est très simple :

	:::bash
	user@jackjack $ omxplayer -o hdmi my_video.avi

Ceci a pour but de lancer la vidéo, en redirigant la sortie audio sur le hdmi.

Seulement un problème se pose lors de la lecture de vidéos en Haute-Définition, notamment les vidéos au format *MKV*, en *h264*, *720p*. Les symptômes sont ceux-ci : 

- La lecture se lance, j'ai du son sur ma télé, mais aucune image à l'écran ;
- Sur les lectures suivantes, je n'ai ni son ni vidéo, _omxplayer_ se termine tout de suite en me souhaitant un _nice day_.

En gros, la commande donne ça : 

	:::bash
	user@jackjack $ omxplayer -o hdmi some_other_video.mkv
	Video codec omx-h264 width 1280 height 720 profile 100 fps 23.976025
		 
	have a nice day ;)


J'ai donc _googleisé_ pendant des jours, en enchainant les mots-clés, "mkv video raspberry", "h264 omxplayer crash", "bug raspberry pi hd video", mais toujours sans succès.

Puis, hier soir, j'ai décidé de poster un message sur le forum officiel [Raspberry Pi](http://www.raspberrypi.org/phpBB3/viewtopic.php?f=26&t=40898). Et là, *hallelujah*! Un sympathique [dom](http://www.raspberrypi.org/phpBB3/memberlist.php?mode=viewprofile&u=754) me répond à peine une heure après, et résoud mon problème!

Le solution est donc celle-ci : Il faut augmenter la taille de la mémoire accordée au GPU en modifiant le fichier de configuration du boot.

Pour cela, on modifie le fichier `/boot/config.txt`, pour modifier la valeur `gpu_mem`, qui par défaut à une valeur de `32`.

	:::bash
	user@jackjack $ grep gpu_mem /boot/config.txt 
	gpu_mem=64

Et normalement tout marche mieux! Notez que si vous avez d'autres soucis, notamment des sous-titres qui ne s'affichent pas, vous pouvez augmenter cette valeur!

Enjoy! ;-)

[Source](http://www.raspberrypi.org/phpBB3/viewtopic.php?f=26&t=40898)
