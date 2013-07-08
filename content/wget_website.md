Title: Crawler un site Web avec wget
Date: 2013-07-03 14:11
Author: Quack1
Category: Linux
Slug: wget_website
Tags: Wget, Crawl, tips, Linux, planet-libre, planet-ubuntu
Summary: Je n'arrive jamais à me souvenir de la commande pour crawler récursivement un site web avec wget donc je note la commande ici.

Billet totalement inutile puisqu'on pourrait me répondre "RTFM" à la question "Comment aspirer récursivement un site Web avec wget tout en ré-écrivant les liens en adresses locales", mais je préfère la noter ici pour savoir directement où chercher la prochaine fois que j'en aurais besoin!

	:::zsh
	wget -rkpE <uri>

- `-r` : récursif
- `-k` : converti les liens en liens locaux
- `-p` : télécharge tous les fichiers nécéssaires à l'affichage de la page en local
- `-E` : modifie les extensions des pages Web en `.html`
