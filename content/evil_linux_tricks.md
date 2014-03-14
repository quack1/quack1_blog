Title: Petits challenges Unix entre amis
Date: 2014-03-14 20:45
Author: Quack1
Category: Linux
Tags: Linux, Cli, planet-libre
Slug: evil_linux_tricks
Summary: Envie de vous challenger sur vos connaissances Linux/Unix ? C'est quelques challenges sont pour vous.
Lang: fr

Début février un post nommé « Evil Linux Instructor Tricks - Or how to torture students for fun and profit » a été posté sur [Reddit[en]](http://www.reddit.com/r/linuxadmin/comments/1x8s0b/evil_linux_instructor_tricks_or_how_to_torture/). Son contenu ? 5 challenges lancés par un formateur Red Hat a certains de ses étudiants qui finissaient trop vite ces exercices.

Les 5 challenges sont souvent assez simple pour ceux qui connaissent un peu la ligne de commande et qui sont déjà tombé sur ce genre de problèmes, sinon ils demandent un peu de recherche.

Voici la liste des _colles_ posées par [_TriggerTX_](http://www.reddit.com/user/TriggerTX).

<div align="center" style="color:#ccc;">☠</div>

## Challenge 1

> Un pirate s'est introduit sur votre serveur Web et a remplacé votre homepage. Remettez la vraie page en ligne.

La manip' effectuée par le formateur a été de _backuper_ `/var/www/index.html`, de modifier l'original, puis d'enlever tous les droits sur le fichier original avec un `chattr +i /var/www/index.html`.

Il mentionne que plus de quatre ans il a lancé ce challenge à plusieurs douzaines d'étudiants, et un seul l'a résolu en temps raisonnable.

## Challenge 2

> Quelqu'un a lancé un `chmod -x /bin/chmod`. Redonnez les bons droits au binaire sans réinstaller le paquet.

## Challenge 3

> Envoyez moi l'output de `ls /etc/` sur votre serveur.

Avant cela, on rajoute à la fin du `.bashrc`  les quelques lignes suivantes : 

	:::bash
	alias ls="echo \"I'm sorry, Dave. I can't do that.\"";
	alias alias="echo \"I'm sorry, Dave. I can't do that.\"";
	alias unalias="echo \"I'm sorry, Dave. I can't do that.\""'

## Challenge 4

Celui-ci n'est pas vraiment un challenge.

Lors des formations, ils essayent de donner l'habitude aux étudiants d'utiliser vi ou vim. Ceux qui sont surpris en train d'utiliser nano se mangent un `mv /bin/nano /bin/nano.nono; ln -s /usr/bin/vim /bin/nano`.

## Challenge 5

> Votre système ne démarre plus. Trouvez pourquoi et réparez-le.

On déplace simplement `/bin/bash` dans `/bin/bash.gotcha`. Si les étudiants demandent un CD de _rescue_, le formateur leur en fournit un.

<div align="center" style="color:#ccc;">☠</div>

## Solutions (ultra) rapides

1. `lsattr` puis `chattr -i`
2. `cp /bin/cpio /tmp; cat /bin/chmod > /bin/cpio; /bin/cpio +x /bin/chmod; cp /tmp/cpio /bin; chmod +x /bin/cpio`[^1]
3. `builtin unalias unalias`[^2][^3]
4. `rm -f /bin/nano; mv /bin/nano.nono /bin/nano`
5. À partir du CD de rescue, il faut farfouiller un peu partout (dans les logs principalement) sur le disque système, pour finalement tomber sur le binaire de bash qui a été renommé.

<div align="center" style="color:#ccc;">☠</div>

Les solutions complètes sont [disponibles sur Reddit[en]](http://www.reddit.com/r/linuxadmin/comments/1x8s0b/evil_linux_instructor_tricks_or_how_to_torture/). Les commentaires contiennent beaucoup de solutions alternatives et sûrement des nouveaux challenges (perso, j'ai pas tout lu).

Si vous avez quelques petits trucs de ce goût là que vous vous lancez entre collègues, n'hésitez pas à les laisser ici en commentaires ;)

[^1]: On backup un binaire qui a les droits d’exécution, on remplace son contenu par celui de _chmod_, on l'utilise pour redonner les droits à _chmod_, et enfin on remet le binaire original en place à partir du backup.
[^2]: On utilise la fonction `builtin` pour demander à bash d'utiliser la fonction `unalias` qu'il intègre par défaut.
[^3]: Perso mon premier réflexe aurait été de regarder dans mon `.bashrc`^W`.zshrc`.