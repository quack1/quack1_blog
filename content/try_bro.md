Title: Essayez l'IDS Bro en ligne
Date: 2014-09-07 15:19
Author: Quack1
Category: Sécurité
Tags: Sécurité, IDS, Bro, planet-libre
Slug: try_bro
Summary: L'équipe de Bro a mis en ligne [cette semaine](http://blog.bro.org/2014/09/announcing-trybro.html) un site web qui permet de tester l'IDS Bro en ligne.
Lang: fr

&nbsp;

<div align=center><a href="/upload/bro_logo.png"><img src="/upload/bro_logo.png" width="600" height="250" align=center /></a></div>
 
​Bro est un [NIDS](https://fr.wikipedia.org/wiki/Syst%C3%A8me_de_d%C3%A9tection_d%27intrusion#NIDS_.28IDS_r.C3.A9seau.29) qui permet d'analyser le trafic réseau de façon sensiblement différente de [Snort](https://www.snort.org/) ou [Suricata](http://suricata-ids.org/). 

> Bro provides a comprehensive pl​atform for network traffic analysis, with a particular focus on semantic security monitoring at scale. While often compared to classic intrusion detection/prevention systems, Bro takes a quite different approach by providing users with a flexible framework that facilitates customized, in-depth monitoring far beyond the capabilities of traditional systems. With initial versions in operational deployment during the mid ‘90s already, Bro finds itself grounded in more than 15 years of research. For more information, see the [Bro Overview](http://www.bro.org/sphinx/intro/index.html).

Il analyse de façon protocolaire le trafic et génère plusieurs fichiers de logs contenant des _metadata_ sur le trafic (hôtes contactés, requêtes HTTP, requêtes DNS, certificats x.509, sessions SMTP, etc.)

> Bro is a passive, open-source network traffic analyzer. It is primarily a security monitor that inspects all traffic on a link in depth for signs of suspicious activity. More generally, however, Bro supports a wide range of traffic analysis tasks even outside of the security domain, including performance measurements and helping with trouble-shooting.

L'équipe de Bro a mis en ligne [cette semaine](http://blog.bro.org/2014/09/announcing-trybro.html) un site web qui permet de tester Bro en ligne.

Le site dispose d'un jeu de règles et pcap permettant de voir le fonctionnement de l'outil, mais on peut également ajouter nos propres règles et pcap. L'outil permet aussi de partager ses règles et pcap.

Pour le tester → ​ [Try.Bro](http://try.bro.org)