Title: Créer une clé USB de backup sécurisée
Date: 2013-01-21 09:39
Author: Quack1
Category:Securité
Tags: Securité, USB, Backup, 
Slug: secure_backup_key

<div align=center><img src="static/upload/secure_key.png" width="600" align=center /></div>

J'ai sur mon Laptop des fichiers assez "précieux" et "importants", comme des clés de chiffrement GPG, des clés RSA de connexion à des machines distantes, ou des fichiers KeePassX contenant mes mots de passe. Tous ses fichiers sont protégés par des passphrases et mon disque dur est chiffré, ce qui rend leur lecture difficile. Cependant, j'ai également des fichiers dans des formats plus courants et moins protégés, comme du ods, des txt, etc... que je préfèrerais ne pas voir divulgués.

Bien évidemment, tous ces fichiers sont sauvegardés sur un disque dur externe (en attendant d'avoir un petit NAS...), mais deviennent alors facilement lisibles pour quiconque ouvrira ce disque dur.

La première solution à laquelle j'avais pensé était de chiffrer le disque dur entier. 2 problèmes ont survenus :

1. Il fallait le formater pour activer le chiffrement, donc perte des données. À proscrire
2. Je voulais que ce disque dur puisse être ouvert depuis des machines éxecutant des OS non-libres, de façon simple et "native" (ie. sans trop de manipulations) à chaque utilisation. 

La solution consistant à chiffrer le disque dur a donc été rapidement oubliée, pour passer à une solution plus simple et rapide : **Utiliser une clé USB de backup sécurisée, qui ne stockera que les fichiers sensibles**


_DISCLAIMER : Ce "tutorial" n'engage que moi, et je ne peut en rien vous garantir que ce système ne possedera pas de faille de sécurité. Je n'ai pas vu de failles de sécurité, mais je ne suis pas expert en sécurité. Cela ne signifie pas qu'il n'y en a pas._

_Vous pouvez vous servir de la clé USB présentée ici pour stocker des données en vrac, sans les backup-er. Notez que si vous perdez ou oubliez la passphrase de déchiffrement, ces données seront totalement perdues._

_Enfin, j'utilise Ubuntu. Les instructions seront normalement communes à toutes les distributions GNU/Linux mais vous aurez peut être besoin, dans certains cas, de les adapter à votre système._

La clé sera chiffrée en utilisant **LUKS**, qui signifie _Linux Unified Key Setup_. C'est une spécification de chiffrement de disque créé pour Linux, dont les avantages sont multiples : 

- **Indépendant** de la plate-forme, bien qu'initialement créé pour Linux, LUKS est un format standard qui ne s'applique qu'au disque chiffré, sans lien avec l'OS ;
- **Compatibilité** et **Interopérabilité**, puisque totalement documenté ;
- Gestion **sécurisée** des mots de passe dans toutes les applications tierces, puisque l'implémentation de cette gestion est documentée dans [la spécification de LUKS v1.1.1](http://cryptsetup.googlecode.com/svn-history/r42/wiki/LUKS-standard/on-disk-format.pdf)

Sur un système GNU/Linux, l'implémentation de référence de LUKS est basée sur `cryptsetup` et `dm-crypt` en backend, et c'est justement ce que nous allons utiliser pour créer notre clé USB de backup.

La première chose à faire est donc d'installer le paquet [CryptSetup](apt://cryptsetup) depuis les dépôts de votre distrib. 

Ensuite, on va formater notre clé. Perso, j'ai créé dessus 2 partitions :

- Une partition de 100M, en FAT, pour y stocker l'utilitaire Windows d'accès au volume chiffré. Cette partition sera en clair ;
- Une partition d' 1.9G (c'est à dire tout le reste) en FAT, qui sera chiffrée.

Les deux partitions, correspondent sur mon système, respectivement au _path_ `/dev/sdb1` et `/dev/sdb2`. C'est seulement cette dernière que l'on utilisera.


La création d'un périphérique sécurisé "LUKS", chiffré en AES512, est assez simple et ne nécessite qu'une seule commande : 
	
	quack@spiderman$ sudo cryptsetup luksFormat -c aes-xts-plain -s 512 /dev/sdb2

Et voilà!

Notre clé est prête à être utilisée. Ne reste plus qu'à la monter et la démonter sur notre système pour pouvoir l'utiliser. Pour cela, on va : 

1. Ouvrir le périphérique LUKS ;
2. Monter le volume sur notre système dans un répertoire `~/work/secure_backup`.

<pre>quack@spiderman$ sudo cryptsetup luksOpen /dev/sdb2 secure_backup
quack@spiderman$ mkdir ~/work/secure_backup
quack@spiderman$ sudo mount -t vfat -o umask=0 /dev/mapper/secure_backup ~/work/secure_backup</pre>

Pour le démonter, les commandes seront les "mêmes" que pour le montage, mais simplement inversées :-P

	quack@spiderman$ sudo umount ~/work/secure_backup
	quack@spiderman$ sudo cryptsetup luksClose secure_backup

Notez cependant que sur Ubuntu, le système vous proposera graphiquement de saisir la passphrase de déchiffrement de la clé et montera automatiquement les partitions sur votre système.

En parlant de partitions, je vous parlait tout à l'heure d'une deuxième partition de 100M. Celle-ci va servir à y déposer [l'éxecutable Windows FreeOTFE](http://www.freeotfe.org/download.html) qui permettra d'accéder aux volumes chiffrés, et tant qu'à faire, on y rajoutera Putty pour nos connexions ssh en environnement "hostile" ;-)

<div align=center text-align=center><a href="static/upload/secure_key_tools.png"><img src="static/upload/secure_key_tools.png" align="center" /></a><br />Quelques outils utiles pour un Unixien en environnement Windows</div>
