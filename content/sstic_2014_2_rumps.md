Title: &#35;SSTIC 2014 - Rumps
Date: 2014-06-08 22:40
Author: Quack1
Category: Sécurité
Tags: Sécurité, SSTIC, SSTIC 2014, Job, planet-libre, Rumps
Slug: sstic_2014_2_rumps
Summary: #SSTIC 2014, deuxième jour. Résumé des rumps !
Lang: fr

# Let's rump

Benjamin Morin, comme chaque année, présente la première rump au nom du CO du SSTIC. Cette année, les 450 places se sont vendues en 8 minutes (nouveau record) ce qui a un peu augmenté la trésorerie de l'association.

Le mode de soumission des conférences a changé cette année, c'est désormais « soumission libre » (au lieu de l'article de 10 pages minimum des années précédentes), et pourtant les actes ont battu des records cette année : 450 pages au total (ça fait lourd dans le sac 😉).

L'organisation des rumps a également été un peu modifiée : chaque rump dure 3 minutes et, si le public veut que l'orateur continue, il ne doit pas applaudir. Si au contraire le public veut que l'orateur s'arrête, il doit applaudir et un applaudimètre couplé à un petit lance-missile tire une flechette en mousse sur le _speaker_ !

# Tuto Miasm par Serpi (Fabrice Desclaux)

Il paraît que [miasm](https://code.google.com/p/miasm) est dur à installer. Serpi reçoit souvent (je cite) des mails lui disant que « Installer miasm c'est pire que de se mettre des caillous dans le c.l ».

Il montre en 2 slides et trois commandes qu'en fait, c'est pas si compliqué :]

# Cloud ISO 14001 (v2) par Arnaud Ebalard

L'année dernière, en rump, Arnaud Ebalard montrait comment se créer son petit cloud perso pas cher et conforme à la norme ISO 14001. Il a poursuivi l'expérience en développant les patchs nécessaires pour faire tourner des Linux sur des NAS Netgear.

Il a mis en ligne sur [natisbad.org](http://natisbad.org/NAS) les images du kernel Linux pour 6 NAS différents (il remercie d'ailleurs Netgear pour lui avoir filé du matos). Son prochain gros travail est le développement d'un [SoC](https://fr.wikipedia.org/wiki/Syst%C3%A8me_sur_une_puce) securisé.

# SELKS par Eric Leblond

[Slides](https://home.regit.org/2014/06/lets-talk-about-selks/)

Eric Leblond, membre de la _core team_ de Suricata déplore que tous les trucs un peu sexy en infosec soient tournés sur l'offensif. Il essaye de corriger ça en nous montrant une brique orientée défense : [SELKS](https://github.com/StamusNetworks/SELKS).

SELKS, pour « Suricata - ElastikSearch - Logstash - Kibana - Scirius », est une distribution basée sur Debian qui embarque Suricata 2 et tout ce qu'il faut pour avoir une interface Web un peu classe pour visualiser les évènements et surtout créer des règles qui vont lancer des actions en fonction des _events_ reçus.

Par exemple, si un client SSH ne me plaît pas je le bloque, etc.

# Kerby@parsifal par Olivier Levillain

Olivier Levillain avait présenté l'an dernier dans [une présentation courte](/sstic_2013_1.html#parsifal-ou-comment-ecrire-des-parsers-resistants-par-o-levillain) [Parsifal](https://github.com/ANSSI-FR/parsifal), un outil qui permettait d'écrire très rapidement des parseurs pour des protocoles réseaux.

Il a refait une démo, cette fois-ci en prenant comme exemple les requêtes Kerberos envoyées par Aurélien Bordès dans [sa présentation](/sstic_2014_1.html#secrets-dauthentification-episode-ii-kerberos-contre-attaque-par-aurelien-bordes).

# ssticy par Pierre Bienaimé

ssticy est un «truc poisseux en python » pour faciliter la résolution des challenges. C'est un framework à la Scapy, avec plusieurs modules (crypto, useful, useless, network, etc), autocomplétion et tout ce qu'il faut.

Pas de code source public, mais un bon conseil donné : écrire ses propres outils c'est pas compliqué et c'est très formateur.

Sinon, en marge de ça, j'avais trouvé [pwntools](https://github.com/pwnies/pwntools), dans le numéro 73 de [MISC](http://www.unixgarden.com/index.php/category/misc), qui fait la même chose.

# J'ai cru voir un grosminet par P.M. Ricordel & P. Capillon

Cette rump était indéniablement une des plus intéressantes ! Quand les machines infectées sont isolées du réseau ou que, plus généralement, l'exfiltration de données est impossible, une autre solution existe : faire fuiter des informations à travers des ultrasons.

Un programme C encode les informations à exfiltrer (texte ou images) dans des ultrasons et, comme par magie, les informations deviendront visibles quand on écoutera le son ambiant dans Audacity.

Une configuration spéciale est à appliquer dans Audacity :

<div align=center><a href="/upload/sstic_ultrasons_conf_0.png"><img src="/upload/sstic_ultrasons_conf_0.png" align=center width="250"/></a>  <a href="/upload/sstic_ultrasons_conf_1.png"><img src="/upload/sstic_ultrasons_conf_1.png" align=center width="250"/></a></div>

En lisant le fichier son avec un iPhone, on peut s'écarter d'une bonne dizaine de mètres et recevoir les infos encore proprement sur un Mac Book Pro. Avec des enceintes correctes, on doit pouvoir aller vachement plus loin.

Il est donc possible d'envoyer des petits chats dans des ultrasons \o/

<blockquote class="twitter-tweet" lang="fr"><p>My prefered rump at <a href="https://twitter.com/search?q=%23SSTIC&amp;src=hash">#SSTIC</a>: kittens transmitted over ultrasound from a smartphone and displayed as a FFT in auhacity <a href="http://t.co/dx2L8WaGfn">pic.twitter.com/dx2L8WaGfn</a></p>&mdash; Aurélien Francillon (@aurelsec) <a href="https://twitter.com/aurelsec/statuses/474819511389274112">6 Juin 2014</a></blockquote>
<script async src="//platform.twitter.com/widgets.js" charset="utf-8"></script>

Les sources ne sont pas encore disponible sur Github, mais elles peuvent être émises dans un .wav d'1h26 et de quelques Go 😉 Et oui, ça a effectivement été développé avec l'argent de vos impôts (les orateurs sont de l'ANSSI).

# L'obfuscation dont vous êtes le héros par Serge Guelton

Jeu de rôle rapide en quelques slides basé sur les _Livres dont vous êtes le héros_ où un code source a été obscurssi suivant les choix du public.

# Mind your languages par Pierre Chifflier (@pollux)

Écrire du code sécurisé c'est bien, mais attention aux petites erreurs de conception intrinsèques aux languages utilisés. Exemples en vrac :

Les égalités en Javascript sont complètement tordues : 

	:::javascript
	{} + {} // NaN
	[] + {} // "[object Object]"
	{} + [] // 0
	({} + {}) // "[object Object][object Object]

En Java, dans certaines égalités, les nombres inférieurs à 128 sont tous égaux.

En PHP, tous les hashs calculés débuteront par un certains nombres de 0, puis un e, puis une suite de chiffres, et seront tous égaux dans les égalités en `==`.

La présentation complète, _Mind your languages_, est déjà dispo sur le site de « L'Agence » : [http://www.ssi.gouv.fr/fr/anssi/publications/publications-scientifiques/articles-de-conferences/mind-your-languages-nouvel-article-sur-l-importance-des-langages-pour-la.html](http://www.ssi.gouv.fr/fr/anssi/publications/publications-scientifiques/articles-de-conferences/mind-your-languages-nouvel-article-sur-l-importance-des-langages-pour-la.html)

# Sécurité des ADSL exotiques par Nicolas Ruff

En Suisse, les immigrés ne peuvent pas avoir de l'ADSL sans quelques recherches approfondies. Nicolas Ruff a donc pu jouer pendant 3 semaines avec son modem Swisscom avant d'avoir accès à Internet.

Quelques vulnérabilités trouvées. 

Les _credentials_ sont `admin`:`admin` (ou `admin`:`1234`). 

Depuis la ligne de commande on a accès à quelques commandes, dont le ping. Du coup, on peut très vite arriver à d'autres infos à base de : `ping 8.8.8.8; head /etc/passwd`, les process tournent en `root`, etc

Bonne nouvelle par contre, leur OpenSSL n'est pas vulnérable à la faille Heartbleed. Bon, c'est parce qu'il est trop vieux, mais au moins il n'y a pas de faille ! :p

Il s'est même permis un[^1] petit troll sur sa dernière slide : « _ _ _ _ _ _ recrute » qui se transforme en un « Google recrute », petite dédicace aux slides de l'an dernier de l'ANSSI et de la DGA.

# Private meeting par Aurélien Bordes

Une des forces d'Outlook c'est son calendrier intégré. Le problème, c'est que quand on partage son calendrier, tout les évènements deviennent publics, exit les rendez-vous privés. Outlook a donc ajouté une option « Privé » sur les évènements.

Problème, ces évènements ne sont pas réélement privés, ils disposent simplement d'un flag de sensibilité qui est positionné sur « Private ». Et comme EWS est requêtable en HTTP, n'importe qui peut y accéder.

Tout ceci est documenté dans MSDN, donc Microsoft ne le considère pas comme une vulnérabilité et l'affichage ou non de ces évènements reste à la discrétion des clients Exchange.

# From NAND till dump

Pour éviter de devoir déssouder des composants électroniques trop chiants à manipuler, l'orateur à passé sa carte aux rayons X, à repéré les pistes électroniques puis a découpé au laser certains parties pour isoler le composant. Il a ensuite dumpé la flash comme ça, puis à ressoudé le tout pour que la carte refonctionne.

# x86 anti decode (PoC) par Axel Tillequin (@bdcht)

_Too much reverse, too much assembly_, j'ai décroché...

# Stopper l'attaque DDoS de Bryan

Une boîte qui fait de l'_advertising_ via des cookies a subi une attaque DDoS par un méchant <s>Kevin</s>^WBryan. Pour éviter de pommer trop de sous, ils se sont mis derrière plusieurs reverse proxys, puis on regardé d'un peu plus près l'attaque.

Pour remonter à Bryan, ils ont décidé de placer un cookie spécial sur son navigateur dès sa prochaine attaque pour pouvoir le suivre sur tous les sites sur lesquels ils ont des pubs, et donc remonter jusqu'à lui.

Sauf qu'il fallait qu'il relance une attaque. Et c'est là que les marketeux entrent en jeu. Comme des grands, sans rien demander à l'IT, ils ont lancé une campagne de _mass mailing_ en disant qu'ils savaient gérer ce genre d'attaque et qu'ils n'étaient pas impactés.

Le gentil Bryan, touché dans son orgeuil, à relancé l'attaque, ce qui a permis aux équipes IT de lui envoyer le gentil cookie et de s'apercevoir que Bryan avait un compte chez eux. Ils ont fermé son compte et, depuis, plus aucune attaque.

# jpg or mp4, pourquoi choisir ? par Christophe Grenier

Pas de rump sur [photorec](http://www.cgsecurity.org/wiki/PhotoRec_FR) cette année, mais sur une technique permettant de créer un fichier polyglotte contenant du Jpg et du MP4.

# TCP Fast Open par Synactiv

[Slides](http://www.synacktiv.com/ressources/tcp_fast_open_sstic_2014_en.pdf)

TFO est une amélioration de TCP massivement poussée par Gogole qui permet de réduire le temps d'établissement des sessions TCP. Comme généralement tout se passe bien, avec TFO on commence à envoyer de la data dès le premier SYN. Sauf que les IDS attendent d'avoir un ` SYN - SYNACK - ACK` pour détecter des attaques. 

Si on commence à envoyer des patterns malicieux dans le premier SYN, on peut pouttrer Snort et Suricata _finger in the nose_.

[Eric Leblond](https://twitter.com/regiteric) attend donc le patch des ingé de Synactiv pour intégrer cette détection dans Suricata 😉

Pour info, TFO est supporté par le kernel Linux depuis la 3.6 et est activé par défaut depuis la 3.13. Il est aussi activé dans Chrome et peut l'être sur nginx (mais pas Apache pour le moment).

# REbus

REbus est un bus de communication entre plusieurs outils pour faciliter le reverse des malwares. On peut ainsi coupler une analyse statique, des AV, IDA ou des analyses dynamiques pour obtenir des infos sur des malwares.

# Classif

Avec toutes les informations obtenues avec REbus, il est donc possible de classer les malwares dans des grandes familles puis de générer des graphes pour visualiser les liens entre malwares.

# La résolution du fameux challenge web100

Troll sur la déclaration d'impôts en ligne. Il manquait certains champs dans le formulaire en ligne. En les rajoutant à la mano dans le code HTML, l'orateur a pu déclarer toutes ses ressources et dépenses et économiser 900€ sur sa déclaration !

# IRMA

_Incident Response & Malware Analysis_ est un outil en ligne qui permet de combiner plusieurs moteurs d'analyse de fichiers pour obtenir plus d'informations, et des informations plus précises. On peut combiner des analyses anti-virus, Hashdb, des analyses statiques, des sandbox, etc

C'est disponible sous licence Apache 2.0, en ligne sur les dépôts GitHub de Quarkslab (quarkslab@github/irma-*) et <s>une version de test est en ligne : [http://frontend.irma.qb](http://frontend.irma.qb)</s> il n'y a pas encore de version de test en ligne.

# Android 0dayz hunting, again

J'ai pas trop suivi...

# Actes epub

Yves-Alexis Perez cherche des solutions pour transformer facilement et rapidement les actes du SSTIC qui sont au format LaTeX en fichiers epub. Pour l'instant, hormis MathML et les graphes Tikz, tout fonctionne.

Et c'est [déjà en ligne](http://static.sstic.org/epub/2014/).

# ???

# Nodescan

Comment scanner Internet très simplement et avec peu de moyens. J'ai pas noté plus :/

# Promo NSC

La NoSuchCon se déroulera du 19 au 21 Novembre 2014. Le CFP se termine fin septembre : [http://www.nosuchcon.org/#cfp](http://www.nosuchcon.org/#cfp).

100% en anglais, 0% Bullshit (ou pas).

# Do not make your own crypto

Une application française permettant de chiffrer ses sms utilise une crypto toute pourrie, du coup en peu de temps on a accès à tout.

# A large scale analysis of the Security of Embedded Firmwares

Les orateurs ont scanné Internet pour obtenir des infos sur les firmwares utilisés sur les box, caméra IP, etc.

Encore une fois, on découvre des jolis bugs, comme la même clé **privée** utilisée pour toutes les caméras IP chez **plusieurs** fabricants, des firmwares vulnérables à des CVE connues depuis des années, etc


[^1]: Je vous rassure, ce n'était pas le seul troll ;)