Title: Analysez vos configurations firewall avec #Springbok
Date: 2014-06-12 20:36
Author: Quack1
Category: Sécurité
Tags: Sécurité, Job, Firewall, Springbok
Slug: springbok
Summary: Springbok est un outil tout juste sorti qui permet d'analyser les configurations de vos _firewall_.
Lang: fr

Springbok est un outil tout juste sorti qui permet d'analyser les configurations de vos _firewall_.

Après avoir chargé le fichier de configuration dans l'outil, il est possible d'afficher un graphe du réseau sur lequel sont représentés les pares-feux ainsi que les machines et groupes de machines.

<div align=center><a href="/upload/springbok_query_path.png"><img src="/upload/springbok_query_path.png" align="center" height="400" /></a></div>

On peut ensuite utiliser l'outil pour « interroger » la configuration pour vérifier que la configuration est correcte et détecter des anomalies. Par exemple :

- Chercher tous les chemins entre un _subnet_ (ou une IP) et un autre, sur des ports source et destinations donnés (voir l'image plus haut) ;
- Détecter les anomalies dans la configuration, et notamment les règles qui se surchargent entre elles. Deux mécanismes de détection sont possibles : 
  - Détection « centralisée » : on cherche toutes les anomalies dans une ACL ;
  - Détection « décentralisée » : l'outil cherche toutes les anomalies dans tous les réseaux et chemins disponibles.

L'outil est pour le moment en version _alpha_ et son code est ouvert[^1] et disponible sur [Github](https://github.com/conix-security/springbok). Pour l'instant, les seuls firewall supportés sont Cisco ASA, Fortigate et Juniper Netscreen[^2]

Si vous le testez (j'espère que oui !), n'hésitez pas à reporter des bugs ou des idées de fonctionnalités sur Github pour que l'outil parvienne vite à une version stable et complète ! :)

Quelques screenshots pour vous donner une idée de l'outil :

&nbsp;

<div align=center><a href="/upload/springbok_result_query_path1.png"><img src="/upload/springbok_result_query_path1.png" align="center" height="400" /></a><br/>Recherche des chemins entre 192.168.0.42 et 192.168.1.43 sur le port tcp/3700</div>

&nbsp;

<div align=center><a href="/upload/springbok_result_query_path2.png"><img src="/upload/springbok_result_query_path2.png" align="center" height="400" /></a><br/>Résultat de la recherche. Les chemins trouvés sont listés à droite</div>

&nbsp;

<div align=center><a href="/upload/springbok_detection_intra_fw.png"><img src="/upload/springbok_detection_intra_fw.png" align="center" height="150" /></a><br/>Détection d'anomalies dans la configuration</div>

&nbsp;

<div align=center><a href="/upload/springbok_result_acl.png"><img src="/upload/springbok_result_acl.png" align="center" height="150" /></a><br/>Affichage des règles d'un ACL</div>

&nbsp;

<div align=center><a href="/upload/springbok_result_conf_error.png"><img src="/upload/springbok_result_conf_error.png" align="center" height="150" /></a><br/>Objets définis mais non utilisés</div>

&nbsp;

<div align=center><a href="/upload/springbok_result_inter_detect.png"><img src="/upload/springbok_result_inter_detect.png" align="center" height="60" /></a><br/>Détection « centralisée » : Anomalies dans une ACL</div>

&nbsp;

<div align=center><a href="/upload/springbok_result_intra_detect.png"><img src="/upload/springbok_result_intra_detect.png" align="center" height="170" /></a><br/>Détection « décentralisée » : Anomalies dans tous les chemins</div>

Et en plus, c'est fait dans [ma boîte](http://blog.conixsecurity.fr), si c'est pas beau ça[^3] !

[^1]: Il n'y a pas de licence clairement définie, il faudra que je fasse corriger ça.
[^2]: Je pense que les fichiers de règles _iptables_ et _pf_ ne devraient pas tarder à être supportés.
[^3]: Oui, je fais de la pub, et alors ?!