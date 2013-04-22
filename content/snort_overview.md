Title: Snort : Présentation rapide de l'IDS
Date: 2013-03-13 14:21
Author: Quack1
Category: Securité
Slug: snort_overview
Tags: Snort, IDS, Stage, Détection d'Intrusion
Summary: Présentation rapide du Système de Détection d'Intrusion Snort.

<div align=center><img src="static/upload/snort.png" width="600" height="250" align=center /></div>

_DISCLAIMER : Depuis peu de temps je suis en stage dans une boîte de sécu/audit, avec comme sujet de stage "_ Scénarios d'attaque et Détection d'Intrusion _". En gros, cela consiste à définir des scénarios ou des outils utilisés par des attaquants/auditeurs, lancer ces outils/scénarios sur des environnements de test puis mettre en place des règles de détection dans des (N)IDS._

_À terme, on souhaite pouvoir corréler les diverses règles définies afin de les généraliser au maximum pour détecter plus que des outils lancés individuellement._

_À terme (bis), pourquoi pas réussir à détecter et remonter un_ flow _d'attaque complet simplement en voyant passer des évenements sur un réseau ? À voir..._

_Bref, pour finir cette intro "chiante" et rentrer dans le vif du sujet, je souhaitais simplement vous préciser ici que je vais sûrement écrire au cours de ce stage plusieurs articles concernant ce sur quoi je travaille, pour deux raisons simples :_

1. _Je pense que cela peut vous intéresser et donc je les partage avec vous ;_
2. _Cela me permettra de m'avancer sur la rédaction du rapport de stage ;-) ._

_Entrons donc dans le vif du sujet._




# IDS ? _Wat is dat_ ?


## Intrusions informatiques

Le milieu de la sécurité informatique se décompose, caricaturalement, en deux groupes : 

1. Les **attaquants** qui vont, comme leur nom l'indique, lancer des attaques contre le système ;
2. Les **responsables informatiques** (ou la DSI), qui doivent défendre leur système face aux attaques.

La DSI doit donc mettre des techniques en place afin de bloquer les attaques lancées contre son système. On peut par exemple citer les _firewalls_ (réseaux et/ou applicatifs), des applications sécurisées, etc...

Cependant les attaquant vont très probablement (et c'est même sûr) trouver des failles dans les précédents systèmes et vont réussir à rentrer au sein du SI. Il va donc falloir pouvoir détecter leur présence, mais aussi détecter les outils qu'ils pourront lancer depuis notre réseau et sur notre réseau (depuis l'extérieur).


## IDS, NIDS, HIDS, et co

C'est pour réaliser cette tâche qu'entrent en jeu les IDS, ou _Intrusion Detection System_. Afin de simplifier les choses, un IDS est une sonde placée judicieusement sur un réseau ou un système, et qui va repérer les activités douteuses ou anormales sur cette cible et alerter les responsables sécurité. De cette façon, on peut obtenir une connaissance des tentatives réussies (ou non) d'attaque ou d'intrusion sur le système.

On différencie plusieurs types d'IDS, à savoir les **NIDS** (ou _Network Intrusion Detection System_), qui se basent sur des analyses réseau, les **HIDS** (ou _Host Intrusion Detection System_), qui surveillent l'activité d'un hôte, et enfin les IDS **hybrides**, qui combinent HIDS et NIDS.

_Désormais, lorsque je parlerais d'_ IDS _je sous-entendrais_ NIDS_, même si la plupart des principes présentés ici sont communs aux 2 types d'IDS._


## Principe de fonctionnement d'un IDS

Les IDS doivent donc alerter les administrateurs et les reponsables sécurité lorsque des évènements suspects apparaissent. Pour cela, le NIDS fonctionne en 3 temps : 

<div align=center><a href="static/upload/fonctionnement_nids.png"><img src="static/upload/fonctionnement_nids.png" align="center" width="500px"/></a><br/>Fonctionnement d'un NIDS. Source : <a href="https://commons.wikimedia.org/wiki/File:Nids.png">Wikipédia</a>, par Sebastien Tricaud.</div>

&nbsp;

1. Il effectue une **capture** d'un flux réseau, au moyen de sondes, reliées à un agrégateur central. Dans certains cas, notamment pour de petits réseaux, la sonde et l'agrégateur seront une seule et même machine. Pour des réseaux plus importants, on disposera les sondes à des endroits clés du réseau, et l'agrégateur sera un serveur dédié centralisé. Les points de positionnement de ces sondes sont multiples. Généralement placées derrière le firewall, pour ne collecter que les paquets qui seront réellement transmis sur le réseau interne, on pourra également placer une sonde dans chaque sous-réseau (notamment au moyen de [_port mirroring_](https://en.wikipedia.org/wiki/Port_mirroring "<Wikipedia : Port Mirroring>") afin de limiter la charge sur chaque collecteur.
2. Après avoir collecté des paquets, le serveur doit **analyser** les données reçues, afin de détecter les activités anormales. Pour cela, il va se baser sur une bibliothèque de **signatures**, qui contient des éléments permettant d'identifier certains paquets comme suspects. L'inconvénient de cette méthode est qu'il faut constamment maintenir à jour cette base de signatures, et que la détection des nouvelles attaques ou des attaques de type _0day_ sera impossible.
3. Enfin, si un (ou des) paquet(s) sont détectés par l'analyseur, alors le système va alerter les administrateurs. Cela peut se faire de plusieurs façons : soit par l'envoi de mails automatique, la sauvegarde de logs via le protocole [syslog](https://fr.wikipedia.org/wiki/Syslog), ou plus généralement via la sauvegarde de ces logs dans une base de données interne pour une lecture par un _front-end_, ou l'utilisation de ces logs par des applications tierces.


## Correlation d'alertes

On l'a vu plus haut, le moteur complet de détection d'un IDS est basé sur des signatures. Nous le verrons plus loin quand on verra Snort plus en détail, mais ces règles permettent de ne relever que des évènements séparés, comme par exemple la présence de certaines données dans un packet HTTP, ou une réception de plusieurs requêtes HTTP infructueuses par seconde. Alors qu'il pourrait être intéresant de pouvoir corréler ces deux alertes, et de ne lever la deuxième alerte que si la première alerte est également apparue, afin d'identifier des scans massifs par brute-force avec des outils tels que [DirBuster](https://www.owasp.org/index.php/Category:OWASP_DirBuster_Project) ou [BlindElephant](http://blindelephant.sourceforge.net/).

Dans le cas présent les 2 alertes seront levées et rendrons la lecture des logs et des alertes difficile au vu du nombre d'informations à lire. On pourra donc mettre en place un [SIEM](https://fr.wikipedia.org/wiki/Security_Information_Management_System), qui va récupérer les logs des alertes, et va pouvoir corréler les alertes entre elles afin de rassembler les informations et tirer des conclusions plus générales sur ce qui est en cours sur le réseau, au lieu de simplement présenter des logs sans aucun lien entre eux.

La corrélation permettra donc, comme je vous le disais, de détecter des attaques par _brute-force_ ou des scans d'application Web, mais aussi de corréler des évenements plus "intelligement", comme expliqué dans ce [très bon exemple sur Wikipédia](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_d%C3%A9tection_d%27intrusion#La_corr.C3.A9lation) : 

> Par exemple, lorsqu'une personne se connecte en dehors des heures de travail, cela a un impact élevé qui n'aurait pas été en temps normal d'activité.




# Mais c'est quand que tu nous parle de Snort ?


Snort est donc un **NIDS**, un Système de Détection d'Intrusion basé sur le réseau. Il va écouter le réseau, puis analyser les paquets et lever des alertes si des paquets _matchent_ une de ses signatures.

Plus techniquement, Snort est un logiciel libre, diffusé sous licence [GNU GPL](https://fr.wikipedia.org/wiki/Licence_publique_g%C3%A9n%C3%A9rale_GNU), désormais principalement supporté et développé par [SourceFire](http://www.sourcefire.com).

En plus de pouvoir écouter le réseau, son moteur (écrit en [C](https://fr.wikipedia.org/wiki/C_%28langage%29)), peut ré-assembler du traffic IP, TCP, et venant de bien d'autres protocoles, afin de pouvoir analyser la communication entière entre deux machines et d'écrire des règles sur du contenu HTTP, plutôt que sur des paquets TCP segmentés traités séparement.

&nbsp;

Je ne vais pas vous détailler ici l'installation de Snort sur votre machine, la chose étant très bien documentée sur [le site de Snort](https://www.snort.org/docs) pour tout bon système UNIX, et même pour WinCrap. Il existe même un [paquet pour Ubuntu](http://doc.ubuntu-fr.org/snort). De nombreux autres tutoriels sont également disponibles sur Internet.

Je n'ai jamais lancé de Snort de façon "industrielle", c'est à dire lancer Snort sur un serveur et le laisser faire sa vie, en ne regardant que les logs régulièrement. Pour l'instant, je lance simplement snort dans ma console et je lui demande de m'afficher tous ses messages directement dans mon terminal, pour vérifier que mes règles fonctionnent. La doc de Snort étant très bien faite, vous disposez de script de lancement du programme au démarrage du système. Perso, pour démarrer "ponctuellement" mon petit Snort, je lance la commande suivante (qui demande à snort d'afficher les données de la couche _Application_ du réseau (couche 7 du modèle OSI), de stocker ses logs dans `/var/log/snort`, de démarrer en utilisant le fichier de configuration `/etc/snort/snort.conf`, et d'afficher ses alertes dans la console) : 

	:::bash
	$ sudo snort -d -l /var/log/snort -c /etc/snort/snort.conf -A console

Une fois ceci fait, dès que Snort va capturer des paquets qui _matchent_ une de ses règles, il affichera le message d'alerte associé dans le console.




# Règles de Snort

Le plus important dans Snort n'est pas son historique, ni comment le lancer, encore moins de savoir s'il peut détecter qu'il tombera de la neige la semaine prochaine. Non. Le plus important, ce sont ses **règles** de détection. Ce sont en effet celles-ci qui vont définir la façon dont Snort doit se comporter.

Snort vient par défaut avec un petit lot de règles, disponibles sous `/etc/snort/rules` dans ma Ubuntu Server. Elles sont classées dans différents fichiers, chacun correspondant à un type de comportements/intrusions détectés. Si vous souhaitez en rajouter (et c'est ce que vous allez faire, n'est ce pas ;-)) vous pouvez le faire dans le fichier `/etc/snort/rules/local.rules`

Si vous souhaitez rajouter des fichiers de règles, vous pouvez les placer dans ce dossier, puis ajouter une ligne à la fin de votre fichier de configuration (typiquement `/etc/snort/snort.conf`) pour lui demander d'inclure vos règles : 

	::: bash
	include $RULE_PATH/audit.rules

_Je ne vais pas tout détailler l'écriture de règles en détails, mais simplement vous présenter les grandes lignes du fonctionnement de celles-ci. Le meilleur moyen d'en apprendre plus est de lire [le PDF de la doc officielle](http://s3.amazonaws.com/snort-org/www/assets/166/snort_manual.pdf "Users Manual")._


## Variables

Dans Snort, vous pouvez définir des variables, qui s'utiliseront et serviront aux mêmes choses que les variables de n'importe quel langage de programmation.

On distingue 3 types de variables : 

1. Les variables **IP**
2. Les variables **port**
3. Les variables **normales**

Il existe tout d'abord des règles générales à propos des variables : 

- on accède à une variable en préfixant son nom d'un `$`, et en mettant son nom (`<var_name>`) entre parenthèses (ou non) ;
- lors de l'accès à une variable, si l'on est pas sûr qu'elle contient des données, on peut ajouter une valeur qui sera utilisée par défaut : `$(<var_name>:-<valeur_par_default>)` ;
- si on souhaite afficher un message d'erreur plutôt que de remplacer par une valeur par défaut : `$(<var_name>:?<message>)`
- chaque variable peut contenir `any`, qui correspond à toutes les valeurs que peut contenir ce type ;
- elles peuvent contenir des négations : `!$(<var_name>)`

### Adresses IP

Les variables **IP** sont définies de la façon suivante, le nom étant préfixé du mot clé `ipvar`, et peuvent contenir une IP, une liste d'IP, ou un bloc CIDR. On peut bien évidemment combiner le tout dans une seule variable.
	
	:::snort
	ipvar IP_1 192.168.1.1
	ipvar IP_LIST [192.168.1.1 , 192.168.1.2 , 192.168.1.3]
	ipvar IP_CIDR [192.168.1.0/24]
	ipvar IP_MIX [192.168.1.1, 10.100.1.0/24, ![8.8.8.8, 8.8.8.4]]

### Ports

Les variables **ports** fonctionnent sensiblement de la même façon que les variables IP, à la différence qu'on les précède de `portvar`, et elles peuvent contenir un port, une liste de ports ou un intervalle de ports.

	:::snort
	portvar PORT_1 80
	portvar PORT_LIST [80,443]
	portvar PORT_RANGE [80:100]
	portvar PORT_MIX [80, 443, ![81:100]]

### Variables "normales"

Enfin, les variables standard, commencant par `var`, contiennent tout et n'importe quoi, y compris des ports et des IP (cependant, ces 2 derniers cas ne sont conservés dans Snort que par compatibilité avec les précédentes _releases_ et il est conseillé d'utiliser les 2 types mis à votre disposition plutôt que `var`).

	:::snort
	var CONF_FILE /etc/snort/snort.conf
	var HTTP_PORT 80
	var SERV_IP 192.168.1.10


## Écriture de règles

Abordons donc désormais en détail le coeur de Snort : ses règles, et la façon de les écrire. 

Pour présenter une règle synthétiquement, je dirais qu'elle va exécuter une action, si elle trouve des paquets utlisant un protocole venant d'une IP et d'un port donnés, allant vers une IP et un port donnés, et que ces paquets correspondent à une liste de critères définis.

Les règles se présentent sous la forme suivante : 

	:::snort
	<action> <protocol> <ip_src> <port_src> <direction> <ip_dst> <port_dst> (<options>)

Avec : 

- `<action>` : L'action à lever si un évènement est relevé : `alert`, `log`, `pass`, ... ;
- `<protocol>` : Le protocole utilisé : `ip`, `tcp`, `udp` ou `icmp` ;
- `<ip_src>` et `<ip_dst>` : Les adresses IP source et destination ;
- `<port_src>` et `<port_dst>` : Les ports source et destination ;
- `<direction>` : La direction de la règle : `->` de A vers B, ou bien `<>` de A vers B et/ou de B vers A ;
- `<options>` : Puis, entre paranthèses, des options permettant de filtrer les paquets qui vont lever des évènements.

&nbsp;

Avec tout ceci, et la doc officielle, vous pourrez désormais écrire toutes vos règles. Cependant, je vais vous lister quelques options parmi les plus connues, afin que vous puissiez commencer à jouer avec snort sans vous plonger dans 250 pages de documentation en anglais ;-)

&nbsp;

Les options sont à formater de la manière suivante : 

	:::snort
	(key=value;key=value;key=value;)

Avec `key` étant le nom de l'option, et `value` la valeur que vous voulez qu'elle ait. Certaines options filtrent le _payload_ du paquet (ie. le contenu qui est envoyé), d'autres filtres portent sur tout, sauf sur le payload, enfin, des options permettent de faciliter la lecture des logs ou la correlation des alertes.

_Pour rendre la fin de l'article plus clair, je vais simplement lister les différentes options qui me semblent importantes, accompagnées d'un court texte les présentant et d'un exemple._

&nbsp;

- `content` : Doit être contenu dans le paquet. Exemple : `content:"User-Agent: WhatWeb.0.4.8-dev";`
	- `http_method` : Placé directement un `content`, permet de préciser que le filtre `content` précédent ne s'applique qu'à la méthode HTTP employée.
	- `http_uri` : Idem, mais avec l'URI HTTP.
	- `http_cookie` : Idem avec le contenu des cookies.
	- `http_header` : Idem, avec le contenu des headers HTTP.
- `msg` : Le message qui sera affiché dans les logs. Exemple : `msg:"Scan avec WhatWeb";`
- `sid` : L'identifiant de la règle. Exemple : `sid:1337;`
- `pcre` : Identique à `content`, mais avec des Expressions Régulières compatibles Perl ([pcre](http://www.pcre.org/)). Exemple : `pcre:"/GET\s*\/should\/not\/exists\.html/i";`
- `flags` : Valeur des flags TCP. Exemple : `flags:"SA";`
- `flow` : Définit le sens du traffic (depuis le client ou le serveur), si la connexion doit être établie, etc.... Exemple : `flow:established, to_server;`
- `session` : Permet d'afficher le contenu de toute une session TCP, pour par exemple _loguer_ le contenu d'un échange telnet, ou ftp. Sa valeur permet de préciser ce qui doit être affiché (`printable` --> Contenu affiché, `binary` --> Données au format binaire, et `all` qui remplace les caractères non affichables par leur valeur hexadécimale). Exemple : `session:printable;`

Pour que vous puissiez voir un peu mieux à quoi ressemblent des règles snort, en voici quelques unes : 

	:::snort
	alert tcp any any -> $SERV_IP_TEST $HTTP_PORTS_TEST (msg:"AUDIT_TOOLS Possible Dirb Brute-Force attack";content:"GET";detection_filter:track by_src, count 5, seconds 1;flow:established,to_server;sid:9990005;)

	alert tcp any any -> $SERV_IP_TEST $HTTP_PORTS_TEST (msg:"AUDIT_TOOLS DirBuster \"Fail Case\" test";content:"GET";http_method;content"/thereIsNoWayThat-You-CanBeThere/";http_uri;flow:established,to_server;sid:9990006;)
	alert tcp any any -> $SERV_IP_TEST $HTTP_PORTS_TEST (msg:"AUDIT_TOOLS DirBuster User-Agent detected more than 5 times in 2 seconds";content:"Dir";pcre:"/^User-Agent\s*:\s*DirBuster/i";detection_filter:track by_src,count 5,seconds 2;sid:9990007;)

	log tcp any any <> any 23 (session:printable;)

&nbsp;

Et la sortie de Snort : 

	:::bash
	        --== Initialization Complete ==--

	   ,,_     -*> Snort! <*-
	  o"  )~   Version 2.9.2.2 IPv6 GRE (Build 121) 
	   ''''    By Martin Roesch & The Snort Team: http://www.snort.org/snort/snort-team
	           Copyright (C) 1998-2012 Sourcefire, Inc., et al.
	           Using libpcap version 1.3.0
	           Using PCRE version: 8.30 2012-02-04
	           Using ZLIB version: 1.2.7

	           Rules Engine: SF_SNORT_DETECTION_ENGINE  Version 1.15  <Build 18>
	           Preprocessor Object: SF_SDF (IPV6)  Version 1.1  <Build 1>
	           Preprocessor Object: SF_REPUTATION (IPV6)  Version 1.1  <Build 1>
	           Preprocessor Object: SF_SMTP (IPV6)  Version 1.1  <Build 9>
	           Preprocessor Object: SF_DNP3 (IPV6)  Version 1.1  <Build 1>
	           Preprocessor Object: SF_SSH (IPV6)  Version 1.1  <Build 3>
	           Preprocessor Object: SF_SIP (IPV6)  Version 1.1  <Build 1>
	           Preprocessor Object: SF_POP (IPV6)  Version 1.0  <Build 1>
	           Preprocessor Object: SF_GTP (IPV6)  Version 1.1  <Build 1>
	           Preprocessor Object: SF_DNS (IPV6)  Version 1.1  <Build 4>
	           Preprocessor Object: SF_DCERPC2 (IPV6)  Version 1.0  <Build 3>
	           Preprocessor Object: SF_FTPTELNET (IPV6)  Version 1.2  <Build 13>
	           Preprocessor Object: SF_MODBUS (IPV6)  Version 1.1  <Build 1>
	           Preprocessor Object: SF_SSLPP (IPV6)  Version 1.1  <Build 4>
	           Preprocessor Object: SF_IMAP (IPV6)  Version 1.0  <Build 1>
	Commencing packet processing (pid=1656)
	03/13-14:17:31.930128  [**] [1:9990006:0] AUDIT_TOOLS DirBuster "Fail Case" test [**] [Priority: 0] {TCP} 192.168.56.1:33302 -> 192.168.56.101:80
	03/13-14:20:56.800271  [**] [1:9990008:0] AUDIT TOOLS SkipFish User-Agent detected more than 150 times in 60 seconds [**] [Priority: 0] {TCP} 192.168.56.1:53482 -> 192.168.56.101:80

&nbsp;

&nbsp;

Normalement, avec tout ceci vous devriez pouvoir commencer à jouer un peu avec Snort. Pour mes tests, j'ai installé Snort sur une VM Ubuntu Server 12.10, qui écoute sur sa propre interface, et je lance les attaques depuis l'hôte.

Surtout, n'oubliez pas de partager vos règles en commentaires! ;-)

# Liens en vrac

[Guide d'installation officiel de Snort sur Ubuntu 12.04 [en]](http://www.snort.org/assets/158/snortinstallguide293.pdf "Guide Install Ubuntu 12.04")

[Manuel utilisateur officiel de Snort [en]](http://s3.amazonaws.com/snort-org/www/assets/166/snort_manual.pdf "Users Manual")

[Page rassemblant la documentation officielle de Snort [en]](https://www.snort.org/docs "Official Doc Page")

[Systèmes de Détection d'Intrusions sur Wikipédia [fr]](https://fr.wikipedia.org/wiki/Système_de_détection_d'intrusion "Wikipedia IDS")
