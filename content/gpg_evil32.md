Title: Des collisions trouvées pour tous les ID (32bits) de clés GPG
Date: 2014-12-01 20:23
Author: Quack1
Category: Sécurité
Tags: Sécurité, GPG, planet-libre
Slug: gpg_evil32
Summary: 
Lang: fr

Deux chercheurs (Richard Klafter et Eric Swanson) ont, grâce à des cartes GPU, pu générer des [clés gpg qui possèdent exactement les même _Key ID_ 32bits que de nombreuses clés](https://evil32.com/), comme par exemple celles disponibles dans la base du _[Web of Trust](https://en.wikipedia.org/Web_of_trust)_.

Ils peuvent donc vous fournir, si votre _Key ID_ est `10000001`, une autre clé gpg, radicalement différente, dont le _Key ID_ sera également `10000001`. Leur [outil baptisé Scallion](https://github.com/lachesis/scallion) peut générer une clé en 4 secondes.

Il faut donc faire attention lorsque vous importez une clé gpg dans votre trousseau à ce qu'elle soit bien celle de votre destinataire, notamment en comparant l'empreinte **complète** et pas seulement le _Key ID_ raccourci.

<div align="center" style="color:#ccc;">☠</div>

Attention, cette faille n'est toutefois pas une faille présente dans gpg, mais plutôt dans les algorithmes de hachage utilisés pour générer les empreintes des clés (notamment MD5 et SHA) qui permet de générer des collisions. Le deuxième problème vient du fait que les _Key Server_ ne vérifient pas, quand ils importent une clé, si une autre clé avec le même _Key ID_ existe déjà dans leur base.

<div align="center" style="color:#ccc;">☠</div>

_Enfin bon, comme gpg n'est utilisé par personne, il n'y a pas trop de risque ;)_