Title: Le client Twitter Corebird (clone de Tweetbot) disponible sur Ubuntu
Date: 2014-10-30 12:34
Author: Quack1
Category: Ubuntu
Tags: planet-libre, planet-ubuntu, Twitter, Corebird
Slug: corebird_ubuntu_14
Summary: Un dépôt PPA est désormais disponible pour Corebird sur Ubuntu
Lang: fr

&nbsp;
<div align=center><img src="/upload/corebird_logo.png" widht="100" align="center"/></div>

L'écosystème des [clients Twitter](https://about.twitter.com/products/list) est assez bien fourni pour Windows et pour Mac, mais assez pauvre pour les systèmes Linux. J'utilisais [hotot](http://www.hotot.org/) qui n'est plus mis à jour depuis un moment, mais qui fonctionnais encore à peu près sur Ubuntu. Par contre, depuis la mise à jour en [14.10](http://releases.ubuntu.com/14.10/), hotot est quasiment inutilisable.

Pour le remplacer, j'ai trouvé rapidement [Birdie](http://birdieapp.github.io/) et [Turpial](http://turpial.org.ve/), mais qui ne me convenaient pas pour plusieurs raisons. J'avais trouvé [Corebird](http://corebird.baedert.org/) il y a un moment, mais il ne fonctionnait que sur ArchLinux. J'avais bien essayé de le compiler à la main mais il nécessitait plusieurs bibliothèques dans des versions qui n'étaient pas supportées par Ubuntu.

Mais depuis la version 14.10 tout fonctionne et un [dépôt PPA est même disponible](http://ubuntuhandbook.org/index.php/2014/07/install-corebird-ubuntu-ppa/) :)

On peut donc l'installer et profiter d'un très bon client Twitter !

    :::bash
    sudo add-apt-repository ppa:ubuntuhandbook1/corebird
    sudo apt-get update
    sudo apt-get install corebird

<div align=center><a href="/upload/corebird_ubuntu.png"><img src="/upload/corebird_ubuntu.png" widht="300" align="center"/></a></div>
