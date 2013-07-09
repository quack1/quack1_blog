Title: SSTIC 2013 Jour #2 : Sécurité des applications Android constructeurs et backdoors sans permissions
Date: 2013-06-06 20:02
Author: Quack1
Category: Securité
Slug: sstic_2013_2_secu_android
Tags: SSTIC, SSTIC 2013, Sécurité, planet-libre, planet-ubuntu
Summary:  SSTIC 2013 : Sécurité des applications Android constructeurs et backdoors sans permissions
Lang: fr

_(par A. Moulu)_

[Slides](https://www.sstic.org/media/SSTIC2013/SSTIC-actes/securite_applications_android_constructeurs_et_rea/SSTIC2013-Slides-securite_applications_android_constructeurs_et_realisation_de_backdoors_sans_permission-moulu.pdf)

Cette présentation s'attardait sur la sécurité des systèmes Android, et plus précisément aux surcouches opérateurs. 

En soit, le système de base est plutôt bien sécurisé (un peu comme tout système informatique). Pour accéder à certains composants _sensibles_ du téléphone, comme les contacts, les données de la carte SD, etc... il faut que l'application demande des permissions au système, et au cours de l'installation l'utilisateur doit choisir s'il accepte (ou non) de donner ses autorisations à l'app. qu'il installe.

L'objectif de la présentation était de montrer qu'il existait sur un Samsung Galaxy S3 (sous ROM Stock, en prendant l'hypothèse que l'utilisateur est sensibilisé à la sécurité, aux permissions, et qu'il utilise le market officiel) des backdoors et plusieurs vulnérabilités accessibles depuis le _userland_ (c'est à dire depuis des applications lancées par l'utilisateur, contrairement aux applications en _kernel-land_ lancée par le noyau).

Tout d'abord, il a observé que le téléphone neuf possède (si je me souviens bien), plus de 160 applications installées (apps de base d'Android + applications tierces installées par Samsung). Pour comparaison, un Nexus 4 n'en a que 90.

Dans sa présentation il détaille plusieurs attaques possibles sur Android depuis une application installable par l'utilisateur.

Par exemple, sur les versions du SDK d'Android inférieures à la v3 (Android 4.2.2 est aux alentours de la 15-16 je crois) le système donne un accès complet à la carte SD en lecture et écriture par défaut aux apps. C'est à dire que l'on n'a même pas à demander de permissions. Ainsi, si on configure son application pour utiliser cette version du SDK (1 ligne de configuration dans le code source), on aura un accès total à la carte SD, et de fait, aux données qui y sont stockées par les autres applications.

Il est également possible, entre autres choses, d'envoyer des données en HTTP (pour faire du _leak_ d'informations), d'élever ses privilèges, ou d'envoyer des SMS sans demander de permissions. Vous retrouverez plus de détails dans le _white paper_ et dans les slides de la conf.