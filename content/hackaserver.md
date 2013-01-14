Title: S'initier au pentest sur hackaserver.com
Date: 2013-01-14 01:23
Author: Quack1
Category: Pentest
Slug: hackaserver
Tags: pentest, initiation, audit, sécurité

<div align=center><img src="static/upload/hackaserver.png" width="600" align=center /></div>

Une des choses les plus complexes lorsque l'on s'intéresse aux tests d'intrusion, c'est de pouvoir mettre en pratique tout ce qu'on lit un peu partout sur Internet ou dans des bouquins.

Pour cela, la meilleure solution qui s'offre à vous est celle-ci : utiliser des **machines virtuelles**. Grâce à la simplicité d'utilisation de vmWare, Qemu et autres VirtualBox, vous pouvez en quelques clics installer des systèmes complets sur son ordinateur.

Par contre, plusieurs problèmes surviennent : 

- Il est très difficile et cher d'obtenir des OS et des logiciels propriétaires pour tester leurs vulnérabilités ;
- En parlant de vulnérabilités, installer le dernier Apache sur une Ubuntu 12.10 ne vous laissera aucune marche de manoeuvre pour trouver et exploiter des vulnérabilités. Il faudra donc choisir des versions vulnérables des logiciels que vous installerez. De fait, vous connaitrez les failles et saurez donc où chercher.
- Enfin, c'est assez souvent la combinaison de plusieurs applications installées côte à côte sur un serveur, ainsi que des défauts dans leur configuration qui amènera des failles.

Il devient donc assez complexe et très coûteux en temps de se monter des machines virtuelles dédiées à l'apprentissage du pentest.

C'est donc pour combler ce manque qu'un nouveau service, [Hack-A-Server](https://hackaserver.com "Hack-A-Server"), a été lancé. Il vous propose de nombreuses machines vulnérables hébergées "dans le cloud", accessibles gratuitement.

Pour y accéder, vous n'avez qu'à vous inscrire (étape nécéssaire, puisque le service vous fournira un certificat OpenVPN afin de pouvoir monter un VPN vers leur plate-forme afin d'accéder aux VM).

Passée cette étape, vous accéderez à [près de 50 machines virtuelles](https://hackaserver.com/arena/training) prêtes à être pownées par vos soins.

Si vous désirez plus de machines virtuelles et de choses avec lesquelles jouer, sachez que le service vous propose également une "Playground Arena". Cette partie possède une double utilité. Des entreprises peuvent y déposer des copies de leurs serveurs, afin qu'ils soient audités par les utilisateurs. Ils appellent ça une **"Crowd Source Audit Platform"**. Vous découvrez des failles dans l'application, son propriétaire paye uniquement pour les failles découvertes (au plus 500$ par faille) et vous êtes rémunérées pour ces découvertes.

Sachez néanmoins qu'avant d'y avoir accès, vous devrez passer par l'**Exam Arena**, où vous devrez auditer une application, puis soumettre à l'équipe de _Hack A Server_ un rapport d'audit détaillé, sur lequel ils jugeront de votre habilité (ou non) d'accès aux audits "réels". Afin de vous aider, leur blog propose également un [tutorial sur la rédaction d'un rapport de test d'intrusion](http://blog.hackaserver.com/howto-complete-a-penetration-test-report-guideline/), et vous avez également [ma série sur le pentest](./tag/serie_pentest.html "Tag : serie_pentest") qui est en cours d'écriture pour avoir plus d'infos sur l'audit!

Voilà, moi je suis très intéressé par ce système, je compte m'y pencher plus en détails une fois que la fac me laissera un peu de temps! ;-)

Enjoy!

[Source](https://community.rapid7.com/community/metasploit/blog/2013/01/08/free-metasploit-penetration-testing-lab-in-the-cloud?goback=.gde_100569_member_202314374 "Source")
