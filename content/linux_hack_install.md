Title: Modifier le programme d'installation d'une distribution GNU/Linux
Date: 2013-08-08 10:06
Author: Quack1
Category: Linux
Tags: Linux, Debian, planet-libre, Job, Stage
Slug: linux_hack_install
Summary: J'ai récémment dû modifier l'installeur d'une distribution basée sur Debian pour rajouter le menu de modification du partitionnement des disques. J'en ai fait un post pour me souvenir de la méthode.

Dans le cadre de mes activités professionnelles, nous avons récemment dû installer la distribution [OSSIM](http://www.alienvault.com/open-threat-exchange/projects) (basée sur une Debian 6) sur un serveur équipé d'un RAID 0 de 2 x 146GB. L'installation se passe généralement sans aucun souci, sauf cette fois là, où au moment de l'installation, l'installeur ne reconnaissait pas notre grappe de disques.

Une légère investigation m'a permis de voir qu'en fait nous n'avions aucun accès à l'assistant de partitionnement des disques, normalement présent par défaut sur cet installateur (lancez une installation de Debian pour voir ;-) ).

<div align=center><a href="https://picasaweb.google.com/lh/photo/ovE8cLFJGe5z-nBHDa3q6NMTjNZETYmyPJy0liipFm0?feat=embedwebsite"><img src="https://lh5.googleusercontent.com/-xJ7QVlTwPk4/UezkMPHI0PI/AAAAAAAAQ-I/uU7v_ZjXagk/s800/003.png" align="center" width="250" style=""/></a><br />Le menu de partitionnement ressemble (en gros) à ça.</div>

Ce menu étant complètement désactivé dans l'installeur présent dans l'ISO, les étapes pour le retrouver sont : 

2. Désarchiver l'ISO
3. Trouver le bon fichier
4. Modifier ce fichier
5. Recréer l'ISO

_La méthode donnée ici est spécifique à OSSIM et au menu de partitionnement, mais sera sûrement adaptable à toutes les distributions qui utilisent cet installeur._

# Accéder aux fichier de l'image ISO

Pour pouvoir "désarchiver" une image ISO, la meilleur technique que j'ai trouvé est de la monter sur le système, puis de copier tous les fichiers : 

	:::zsh
	cd working_directory/
	mkdir iso
	mkdir /tmp/iso
	sudo mount -o loop ~/work/iso/AlienVault_OSSIM_64Bits_4.2.iso /tmp/iso
	sudo cp -a /tmp/iso iso/

J'ai lu dans certains articles qu'on pouvait remplacer `cp` par `rsync`. C'est sûrement mieux, mais moi ça a marché du premier coup avec `cp`, donc j'ai pas cherché plus loin.

# Trouver le fichier qui gère l'installation

Pour ça, il faut y aller au petit bonheur la chance. Moi j'ai parcouru les répertoires jusqu'à trouver un fichier qui me semblait pas mal.

Et j'ai trouvé mon bonheur dans `simple-cdd/`. 

Ce dossier contient plusieurs fichiers `.preseed`, qui contiennent le déroulement de la procédure d'installation.

La partie sur le partitionnement débute par 

	:::zsh
	### Partitioning.

Et elles contient des trucs de ce genre : 

	:::zsh
	d-i partman-auto/disk string /dev/sda
	d-i partman-auto/method string regular
	d-i partman-auto/purge_lvm_from_device boolean true
	d-i partman-lvm/device_remove_lvm boolean true
	d-i partman-md/device_remove_md boolean true
	d-i partman-lvm/confirm boolean true
	d-i partman-auto/choose_recipe select atomic
	#d-i partman-auto/expert_recipe string                         \
	#      boot-root ::                                            \
	#              40 50 100 ext4                                  \
	#                      $primary{ } $bootable{ }                \
	#                      method{ format } format{ }              \
	#                      use_filesystem{ } filesystem{ ext3 }    \
	#                      mountpoint{ /boot }                     \
	#              .                                               \
	#              500 10000 1000000000 ext4                       \
	#                      method{ format } format{ }              \
	#                      use_filesystem{ } filesystem{ ext3 }    \
	#                      mountpoint{ / }                         \
	#              .                                               \
	#              64 512 300% linux-swap                          \
	#                      method{ swap } format{ }                \
	#              .

En gros, elle dit que tout est fait automatiquement, en choisissant les bons disques, en les reformatant, et en recréant des partitions.

Pour rajouter le choix manuel, j'ai commenté toute la partie sur la partitionnement, que j'ai remplacé par ceci : 

	:::zsh
	d-i partman-auto/choose_recipe select All files in one partition (recommended for new users)
	d-i partman-auto/choose_recipe select Desktop machine
	d-i partman-auto/choose_recipe select Multi-user workstation

## Recréer l'ISO

Pour ré-empaqueter nos fichiers dans notre image ISO, la commande suivante tirée de la doc Debian fait l'affaire : 

	:::zsh
	sudo mkisofs -o ossim_parted.iso -r -J -no-emul-boot -boot-load-size 4 -boot-info-table -b isolinux/isolinux.bin -c isolinux/boot.cat iso

&nbsp;

C'est très spécifique à mon problème, je suis pas sûr que ça puisse vous aider, ou même vous être un jour utile, mais au cas où, la [doc Debian](https://wiki.debian.org/DebianInstaller/Modify/CD "Debian Installer - Modify CD") est pas mal, sinon j'ai aussi pompé 2-3 trucs [ici](http://support.ironsystems.com/index.php?/Knowledgebase/Article/View/7/3/how-to-modify-debian-installer "How to modify Debian Installer")