Title: SSTIC 2013 Jour #2 : Présentations courtes
Date: 2013-06-06 20:01
Author: Quack1
Category: Securité
Slug: sstic_2013_2_courtes
Tags: SSTIC, SSTIC 2013, planet-libre, planet-ubuntu
Summary:  SSTIC 2013 Jour 2 : Présentations courtes
Lang: fr

Au cours de la deuxième journée de conférences, nous avons pu assister à 3 présentations courtes, sur des sujets aussi variés que la sécurité d'Android, la VOIP Cisco ou encore la résilience d'Internet

# Hacking d'Android/Samsung (par E. Comet)

Cette présentation c'est penchée sur les vecteurs d'attaque possibles pour une application Android. Les principaux vecteurs sont : 

- Par un **accès physique**, en modifiant le bootloader, ou directement par USB
- À **distance**, en utilisant des failles dans les navigateurs Web, dans des protocoles de communication utilisés ou des applications malveillantes
- Ou encore, le point le plus développé dans la conférence, avec un **accès local** au téléphone, on peut accéder à beaucoup plus de privilèges. Les solutions les plus évidentes sont d'utiliser des applications malveillantes, des failles dans les surcouches opérateur, ou encore des attaques sur le noyau.

Le noyau est plus vulnérable puisque la surface d'attaque est plus grande. Basé sur un kernel GNU/Linux, les patchs de celui-ci ne sont pas appliqués sur les smartphones puisque peu d'entre eux reçoivent des MAJ des constructeurs. De plus, le kernel est compilé pour une plateforme ARM, beaucoup moins auditée que la plateforme x86 traditionnelle.

Enfin les applications constructeurs ou les surcouches opérateurs intègrent parfois (et même souvent) des modifications du noyau ce qui offre beaucoup de nouvelles possibilités d'attaques.

# Compromission d'un environnement de VOIP Cisco (Exploitation du Call Manager) (par Francisco)

Un système de VOIP Cisco est basé sur un réseau en étoile, avec en périphérie les équipements de type téléphone/softphone, et au centre un Call Manager. (ou _CM_)

Ce CM reçoit les demandes d'appel, contacte le numéro demandé, et quand une liaison est établie, renvoie la communication à l'appelant. 

L'orateur nous a présenté ici plusieurs failles de type _0-day_ (c'est à dire jamais publiées) sur ce Call Manager, qui permettent en quelques étapes de _p0wner_ tout le système de VOIP.

En executant une injection SQL, puis en utilisant des failles de type _Remote Code Execution_ permettant d'exécuter du code sur l'hôte distant, on peut arriver avec quelques étapes supplémentaires à obtenir un compte root sur le Call Manager.

Le seul point négatif est que l'entreprise n'a pas contacté l'éditeur, ce qui se fait généralement avant de publier des failles aussi critiques sur des systèmes massivement déployés en production.

# Observatoire de la résilience de l'Internet Français (par G. Valadon)

Cette dernière présentation courte était consacrée à une action menée conjointement par l'ANSSI et l'AFNIC (association française qui gère les noms de domaines rattachés à la France (le _.fr_, et dérivés)). Cette enquête réalisée sur plusieurs années a permis d'obtenir de nombreuses statistiques concernant l'internet français.

Notamment, on apprend que certains préfixes IP appartenant à des opérateurs français sont parfois usurpés par d'autres AS en utilisant des annonces BGP, on peut également obtenir le taux de pénétration d'IPv6 en France, ou également avoir une carte des AS français et la répartition des sites Web dans ces AS.