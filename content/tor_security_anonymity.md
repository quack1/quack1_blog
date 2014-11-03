Title: Ne vous croyez pas trop en sécurité avec Tor...
Date: 2014-10-24 10:52
Author: Quack1
Category: Sécurité
Tags: Sécurité, Tor, planet-libre, anonymat
Slug: tor_security_anonymity
Summary: La société Leviathan Security a publié [un article de blog](http://www.leviathansecurity.com/blog/the-case-of-the-modified-binaries/ "The Case of the Modified Binaries") présentant les résultats de certains de leurs tests qui ont permis de montrer que certains nœuds de sortie Tor modifiaient les exécutables téléchargés par les utilisateurs. Quelques lignes pour rappeler que Tor ne fait que de l'anonymat et ne garantie pas votre sécurité.
Lang: fr

[Tor](https://www.torproject.org/ "Tor Project: Anonymity Online") est un logiciel bien connu permettant d'anonymiser votre trafic Internet en le relayant à travers 3 machines du réseau Tor (un nœud d'entrée, un nœud relai puis enfin un nœud de sortie). À aucun moment un nœud du réseau ne peut savoir, **simultanément**, qui vous êtes et à qui vous parlez.

Tor est donc un outil incroyable puisqu'il permet à de nombreuses personnes, dans des pays pas toujours amis des libertés sur Internet, d'accéder à un Internet non-filtré sans danger.

Hier, la société Leviathan Security a publié [un article de blog](http://www.leviathansecurity.com/blog/the-case-of-the-modified-binaries/ "The Case of the Modified Binaries") présentant les résultats de certains de leurs tests qui ont permis de montrer que certains nœuds de sortie (1 seul, dans ce cas précis) modifiaient les exécutables téléchargés par les utilisateurs.

Ce n'est pas une pratique qui a l'air trop répandu, mais il est tout de même bon de rappeler que Tor ne vous apporte que de l'**anonymat**. Utiliser Tor pour naviguer sur Internet ne vous assure pas une entière sécurité. Votre trafic est conditionné par la bonne foi des administrateurs de tous les nœuds Tor.

Ils ont accès à tout votre trafic, ce qui leur permet d'interagir avec vous, même sans savoir qui vous êtes. Ils peuvent absolument **tout** faire avec votre trafic réseau. 

On peut par exemple citer [cet article](http://arxiv.org/abs/1208.2877 "Torinj : Automated Exploitation Malware Targeting Tor Users")[^1] de 2012 qui montrait comment il était possible d'infecter les utilisateurs de Tor si on contrôlait un nœud de sortie.

On pourra également rappeler que fin Juillet le réseau Tor a [exclu un groupe de nœuds qui avaient été utilisés pour désanonymiser, entre Janvier et Juillet, de nombreux utilisateurs](https://blog.torproject.org/blog/tor-security-advisory-relay-early-traffic-confirmation-attack "Tor security advisory: "relay early" traffic confirmation attack").

[Cet article de CryptoMe de mi-Juillet](http://cryptome.org/2014/07/trusting-tor-not.pdf "Question: Should You Trust Tor?") répond aux même questions que celui-ci. « _Should you trust Tor ? Not If Your Life Is At Stake._ »

&nbsp;

Cet article enfonce peut-être des portes ouvertes, mais il me paraissait important de faire ces rappels.

Tor vous anonymise. Point.

Le serveur que vous contactez peut quand même vous envoyer de la merde. Votre poste est peut-être déjà infecté. Les intermédiaires sur le réseau (votre FAI, les nœuds Tor, les FAI entre l'_exit node_ et le serveur) peuvent être compromis ou malveillants.

Tor n'apporte **en rien** une sécurité supplémentaire autre que votre anonymat.

Donc faites attention à ce que vous faites sur Internet et utilisez le chiffrement au maximum pour vous protéger, au moins, des intermédiaires.

&nbsp;

Et si vous voulez aider à la mise en place de nœuds de sortie Tor corrects, vous pouvez aller jeter un œil à l'association française [Nos Oignons](https://nos-oignons.net/ "Nœuds de sortie Tor financés par la communauté. ") qui gère plusieurs nœuds Tor.

[^1]: par Gerard Wagener, Alexandre Dulaunoy et Radu State, publié le 14 Août 2012.
