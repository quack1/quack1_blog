Title: Activer plusieurs comptes mail et une adresse « catchall » dans Postfix
Date: 2013-11-13 19:52
Author: Quack1
Category: Linux
Tags: Linux, MTA, Postfix, Mail, planet-libre
Slug: postfix_aliases_catchall
Summary: Sur mon serveur de mail Postfix, j'ai plusieurs utilisateurs configurés qui peuvent recevoir et envoyer des mails. Certaines adresses sont « virtuelles » et sont en réalité des alias vers d'autres adresses. Rajouter un « catchall » sur mon domaine signifie perdre mes différents utilisateurs. Mais une solution existe.

Sur mon serveur de mail _Postfix_, j'ai plusieurs utilisateurs configurés qui peuvent recevoir et envoyer des mails. Certaines adresses sont « virtuelles » et sont en réalité des alias vers d'autres adresses. Rajouter un « catchall » sur mon domaine signifie perdre mes différents utilisateurs. Mais une solution existe.

Mon serveur postfix autorise l'envoi de mails à des adresses de la forme `<LOGIN>@quack1.me` — `<LOGIN>` étant un nom d'utilisateur sur le système.

Parfois, j'ai voulu que les mails adressés à des adresses différentes arrivent dans la _mailbox_ d'un seul utilisateur. J'ai utilisé le principe des _[alias](https://wiki.archlinux.org/index.php/postfix#Step_4:_.2Fetc.2Fpostfix.2Faliases "Postfix - Step 4: /etc/postfix/aliases ")_ (en les renseignant dans le fichier `/etc/aliases`).

<div align="center" style="color:#ccc;">☠</div>

Ensuite, pour ne pas perdre de _mails_ envoyés à des adresses inconnues de mon système, j'ai rajouté un système de « catchall » à mon _Postfix_.

La [configuration de base que j'ai trouvé sur Internet](http://www.tipcache.com/tip/Create_a_super_%22catch-all%22_email_address_in_Postfix_16.html "Tip: Create a super "catch-all" email address in Postfix") consistait à dire à _Postfix_ de relayer **tous** les mails reçus à une seule adresse. Le problème c'est que du coup, même les mails envoyés aux utilisateurs connus du système sont envoyés à mon _catchall_.

J'ai fouillé un peu plus, et j'ai trouvé une [troisième solution](http://hints.macworld.com/article.php?story=2003110323024816 "Server: Create a postfix catch-all email account") (qui elle me convient).

<div align="center" style="color:#ccc;">☠</div>

On n'utilise plus que le fichier `/etc/postfix/virtual` pour définir les utilisateurs (réels et les alias) et pour le _catchall_.

Première modification, dans le fichier de configuration `/etc/postfix/main.cf` : 

	:::bash
	#alias_maps = hash:/etc/aliases
	#alias_database = hash:/etc/aliases
	virtual_alias_maps = hash:/etc/postfix/virtual
	virtual_alias_domains =

Dans le fichier `/etc/postfix/virtual`, je défini 3 choses : 

1. Les « vrais » adresses, ceux qui ont un compte sur le système ;
2. Les alias, et à quel compte les courriers sont redirigés ;
3. Le _catchall_.

Les deux premiers cas sont identiques en pratique. Je note, sur chaque ligne du fichier, l'adresse à qui le mail est destiné, et à droite le nom du compte qui va recevoir l'adresse.

	:::bash
	# "Real" addresses
	user@domain.com       	user
	girlfriend@domain.com 	girlfriend

	# Aliases
	root@domain.com 		admin+root
	contact@domain.com 	root

_Notes pour ce point : Les adresses définies dans la première colonne sont les adresses_ de base _de remise des mails, donc les délimiteurs (comme le '+' fonctionnent). Si j'envoie un courriel à `root+blog@domain.com`, il sera délivré à `admin+root`. De plus, on peut définir dans la deuxième colonne un alias comme adresse de réception du message._

<div align="center" style="color:#ccc;">☠</div>

Enfin, pour gérer le catchall, on rajoute une ligne en bas du fichier. 

	:::bash
	#################################
	#  Catch-All
	#################################
	@domain.com              catchall

Tous les mails envoyés à `domain.com`, et qui n'auront pas été transmis à partir de la liste des comptes définis plus haut, seront remis dans la _mailbox_ de `catchall`.

&nbsp;

Pour appliquer la configuration, on relance Postfix.

	:::bash
	# postmap /etc/postfix/virtual
	# service postfix reload
<div align="center" style="color:#ccc;">☠</div>

Voilà, il y a peut être des solutions plus propres pour le faire, mais celle-ci fonctionne et elle est assez simple à mettre en place! 😃