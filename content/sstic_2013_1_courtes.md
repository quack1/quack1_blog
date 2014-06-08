Title: SSTIC 2013 Jour #1 : Présentations courtes
Date: 2013-06-05 20:01
Author: Quack1
Category: Securité
Slug: sstic_2013_1_courtes
Tags: SSTIC, SSTIC 2013, Sécurité, planet-libre, planet-ubuntu, Job, Stage
Summary:  SSTIC 2013 : Présentations courtes
Lang: fr

# Parsifal, ou comment écrire des parsers résistants (par O. Levillain)

[Slides](https://www.sstic.org/media/SSTIC2013/SSTIC-actes/parsifal/SSTIC2013-Slides-parsifal-levillain.pdf) & [Sources](https://t.co/ZGw0dwxaVL)

Cette présentation courte veut combler le problème des parsers de protocoles comme ceux intégrés à Wireshark ou Scapy. 

Au lieu d'écrire des fichiers complexes pour parser un protocole simple, Persifal utilise des fichier OCaml concis. On a donc a définir simplement une structure qui réprésente le protocole et le _framework_ Persifal va intégrer le tout et créer un _parser_ complet.

# _nftables_ (bien plus qu'iptables) (par E. Leblond)

[Slides](https://www.sstic.org/media/SSTIC2013/SSTIC-actes/nftable/SSTIC2013-Slides-nftable-leblond.pdf).

Cette dernière présentation courte a été donnée par un des membres de la _coreteam_ d'iptables. C'est donc un bonhomme qui maitrise bien le firewall-ing!

Il nous a présenté _nftables_, le futur remplacant d'iptables, qui est actuellement développé activement par l'équipe d'iptables. Le but ? Supprimer le fonctionnement un peu archaïque de l'ajout ou de la modification des règles (syntaxe pas très claire et mise à jour des règles chargées dans le noyau trop coûteuse).

Ici, la nouvelle syntaxe sera beaucoup plus _sexy_, la mise à jour des règles dans le noyau sera faite via _Netlink_, qui est un système qui envoie des messages au noyau, qui se charge de gérer les règles dans son coin.

Et bien sûr, une rétro-compatibilité avec Netfilter/iptables sera assurée!

Un [_Quick and Dirty_ Howto](https://t.co/cM4zogob8t) est aussi disponible.