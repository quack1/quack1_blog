Title: Guitare électrique « homemade » – Partie 2
Date: 2014-05-06 21:05
Author: Quack1
Category: DIY
Tags: DIY, Guitare, Lutherie, I Make
Slug: homemade_guitar_2
Summary: À la fin du [premier article]({filename}/homemade_guitar_1.md) de [cette série]({filename}/homemade_guitar.md), on a normalement préparé toute la fabrication de notre guitare. On sait quel modèle on va fabriquer, quelles seront les pièces que l'on y mettra (on a pour cela réalisé un plan 1:1 de la guitare), les pièces et le bois sont achetées, on a réuni pas mal d'outils, on est donc près à commencer !
Lang: fr

À la fin du [premier article]({filename}/homemade_guitar_1.md) de [cette série]({filename}/homemade_guitar.md), on a normalement préparé toute la fabrication de notre guitare. On sait quel modèle on va fabriquer, quelles seront les pièces que l'on y mettra (on a pour cela réalisé un plan 1:1 de la guitare), les pièces et le bois sont achetées, on a réuni pas mal d'outils, on est donc près à commencer !

Pour vous donner une idée de mon projet, j'étais parti sur une guitare type [Les Paul Junior], en _grande_ taille. La longueur totale de la guitare (du bas du corps à la tête) dépassait le mètre 10, pour avoir plus d'aigus le diapason prévu mesure 774mm[^2] (sur une Les Paul Junior standard c'est 625mm[^1]), et au niveau de l'électronique un seul micro humbucker ([EMG H4](http://fr.audiofanzine.com/micro-guitare/emg/Hz-H4/avis/)) est commandé, et deux potentiomètres seront utilisés : un volume et une tonalité.

# Préparation du bois

La première étape est de reporter toutes les indications présentes sur votre plan sur le bois, pour avoir une vue d'ensemble de la future réalisation.

Vous pouvez donc maintenant procéder au collage des différentes pièces. Dans le cas d'un manche traversant (le cas dont je parlerais dans cet article), on colle donc le manche et les deux pièces du corps, et pour un manche vissé ou collé, on colle les deux parties du corps ensemble.

Avant le collage, pensez à deux dernières choses.

Vos micros devront être reliés à vos potentiomètres, il font donc prévoir un passage pour les câbles. Si vous êtes sur du type Fender, vous avez (normalement) dû prévoir un pickguard, et donc vous n'avez rien à faire pour le moment. Dans le cas d'un type Les Paul, la table n'est pas protégée par un pickguard, il faut donc percer le corps de la guitare entre l'espace réservé au micro et celui réservé à l'électronique. Pour rendre les choses plus simples, le mieux est de percer cette « gaine » avant le collage. Il faut également penser à percer un deuxième passage pour relier la masse des potentiomtres au chevalet.

Deuxième point, essayez de tailler la forme du manche avant le collage, notamment donnez sa forme à la tête et dégrossissez le manche. C'est toujours plus facile à faire quand la pièce de bois que l'on travaille est plus petite ;)

<div align=center><a href="/upload/homemade_guitar_degrossissage_tete_HD.png"><img src="/upload/homemade_guitar_degrossissage_tete.png" align="center" width="650" /></a></div>

&nbsp;

Pour le collage à proprement dit, rien de particulier ici. Un rainurage de toutes les parties à coller permettra une meilleure adhérance de la colle, mettez autant de serres-joints que vous pouvez, et attendez deux à trois bons jours que la colle prenne et sèche.

<div align=center><a href="/upload/homemade_guitar_collage_HD.png"><img src="/upload/homemade_guitar_collage.png" align="center" width="650" /></a></div>

# Pendant que ça sèche...

Normalement, si vous avez bien fait votre plan, vous connaissez **exactement** le diapason qu'aura votre guitare. Pour rappel, le diapason est la longueur de corde qui vibrera dans la corde sera grattée « à vide ». C'est donc la longueur de corde entre le sillet de tête et le chevalet.

Donc, si vous connaissez votre diapason, vous pouvez calculer l'emplacement des frettes et préparer la touche.

_À ce niveau là, j'ai l'impression qu'il y a deux techniques qui s'opposent. La première consiste à préparer la touche avant, puis la coller sur le manche de la guitare, tandis que la seconde vise à coller la touche brute sur le manche, puis de la travailler._

J'avais utilisé une technique un peu différente, puisque j'avais préparé la touche presque totalement, et je m'était arrêté juste avant de poser les frettes. Je n'ai posé celles-ci qu'une fois que la touche était collée.

Pour reprendre les étapes dans l'ordre : 

J'ai découpé la touche à ses dimensions finales, en gardant un poil de marge sur la largeur pour l'adapter ensuite parfaitement au manche. La longueur est sa longueur définitive, à noter que la longueur inclut un demi à un centimètre pour la pose du sillet.

Une fois que la touche est à la bonne taille, on la ponce à fond pour la rendre la plus lisse possible, puis on forme le [radius](http://fr.wikipedia.org/wiki/Touche_%28lutherie%29#Courbure) de la touche avec — idéalement — une cale à radius, sinon c'est à la ponceuse ou à la rape, en contrôlant régulièrement que l'on n'est pas allé trop loin. Pour vérifier ça, [ces gabarits à imprimer](http://www.pickguardian.com/pickguardian/Images/Pickguardian%20Neck%20Radius%20Gauges.pdf) sont parfaits[^3].

Quand votre touche est prête, il devient nécéssaire de préparer la pose des frettes. Pour cela, on va calculer les emplacements de celles-ci au moyen d'une formule compliquée : 

> Pour chaque frette _n_ (le sillet étant la frette 0), la distance _Ln_ entre cette frette et le chevalet est égale à la division du diapason _L_ par 2 à la puissance _n_ divisé par 12.

Donc, de manière plus claire (ou pas) :

<div align=center><img src="/upload/frettage_distance_from_chevalet.png" align="center" height="150"/></div>

> Et donc, on obtient facilement la distance _L - Ln_, distance qui sépare une frette _n_ du sillet : 

<div align=center><img src="/upload/frettage_distance_from_sillet.png" align="center" height="150" /></div>

Bon, arrêtons les blagues, si vous voulez en savoir un peu plus sur la théorie du frettage, je vous laisse lire la [page Wikipédia dédié à la gamme tempérée](http://fr.wikipedia.org/wiki/Gamme_temp%C3%A9r%C3%A9e). Pour calculer plus simplement l'emplacement des frettes, rendez-vous [ici](http://pueyoguitar.free.fr/outils/calcfrettes.htm), entrez votre diapason, et vous aurez la liste prête à être imprimée :)[^4].

&nbsp;

Quand votre liste est prête, tracez les emplacements des frettes **avec une grande précision** sur la touche de la guitare. Vous pouvez désormais préparer les [inlays](http://en.wikipedia.org/wiki/Inlay_%28guitar%29) qui permettront de vous repérer sur le manche. C'est purement de la déco, donc je vous laisse choisir le motif : [rond](http://en.wikipedia.org/wiki/File:Ibanez440rs6.jpg), en [triangle](http://www.monsonguitars.com/images/800_Varikill_9-02.jpg), en [trapèze](http://en.wikipedia.org/wiki/File:Fretboard_trapezoids.jpg) à la Gibson, ou si vous avez des talents d'ébéniste, vous pouvez tenter les inlays à la Joe Bonamassa sur sa Gibson ES335[^5].

Moi je suis resté dans du traditionnel, inlays ronds et noirs, taillés dans une baguette de 10mm de diamètre. Pour les insérer, on perce la touche (pas trop profond), on met de la colle, on insère les inlays, et on presse pendant une bonne nuit le temps que la colle prenne.

Le lendemain, on reponce un bon coup histoire de rattraper le radius et d'obtenir une touche bien lisse.

<div align=center><a href="/upload/homemade_guitar_inlays_HD.png"><img src="/upload/homemade_guitar_inlays.png" align="center" width="650" /></a></div>

Ensuite, un des moments les plus délicats arrive : il faut inciser le bois pour créer des emplacements pour les frettes.

Plusieurs techniques : le faire avec une [scie japonaise](http://fr.wikipedia.org/wiki/Scie_japonaise), [scie à onglet](http://fr.wikipedia.org/wiki/Scie_%C3%A0_onglet) montée avec une lame fine, ou bien (technique du pauvre) avec une petite scie à métaux.

L'important, quelle que soit la scie utilisée, c'est de bien la caler pour être sûr de scier **sur** la marque de la frette. Le moindre écart, à n'importe quel moment du processus, va influer sur la justesse de la guitare.

<div align=center><a href="/upload/homemade_guitar_frettage_HD.png"><img src="/upload/homemade_guitar_frettage.png" align="center" width="650" /></a></div>

Enfin, récapitulatif de l'article :

- Vous avez collé le bois nécessaire à votre corps et le manche est « pré-taillé » ;
- La colle a séché ;) ;
- La touche est quasiment prête : 
	- Elle est prédécoupée ;
	- Le radius est ajusté et la touche est poncée ;
	- Les emplacements de vos frettes sont taillés ;
	- Les inlays sont en place.

Dans le prochain article (#teasing), je vous parlerais de la découpe du corps et des différentes défonces pour les micros et autres parties électroniques. Stay Tuned ;)

[^2]: On est assez proche du diapason d'une basse.
[^1]: Chez Fender, on est dans les 650mm.
[^3]: Attention au moment de l'impression, il faut que la barre noire en haut de la feuille mesure 1 pouce une fois imprimée (soit 2,5nd4cm).
[^4]: Les plus geeks comme moi auront sorti leur plus bel éditeur de code et auront écrit le programme qui calcule ça tout seul ;)
[^5]: Désolé, je n'ai pas trouvé de photos...