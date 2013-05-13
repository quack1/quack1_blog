Title: MAO : Monter son (petit) home-studio sous Linux
Date: 2012-04-05 21:18
Author: Quack1
Category: Musique
Tags: ardour, guitare, guitarix, home studio, jackd, mao, musique, rakarrack, ubuntu, ubuntu studio, planet-libre, planet-ubuntu
Summary: Installation des logiciels nécéssaires pour monter un home-studio sur un système GNU/Linux.

![Home Studio](static/upload/homestudio.png "Home Studio")

Jusqu'alors, le seul moyen pour les musiciens, et en particulier les
guitaristes, de pouvoir s'enregistrer et rajouter quelques effets sur
leur son était d'avoir un Mac et de s'acheter un logiciel de MAO très
couteux, type Cubase, ou autre. Bref, il fallait un assez gros budget,
et ça pouvait décourager plus d'un musicien amateur qui aurait eu envie
de se lancer dans la prod'.

Et là, MonSeigneur du Logiciel Libre arrive sur son grand cheval blanc,
et nous donne plusieurs excellent logiciels qui permettent de simuler
ampli et effets pour sa guitare, pour ensuite l'enregistrer dans un
éditeur multi-pistes. En plus de ça, on peut rajouter une batterie grâce
à une boite à rythme, brancher un clavier, bref, faire tout ce qu'on
fait dans un vrai studio, mais avec un simple ordinateur sur Linux :D

Je vais ici vous présenter ma configuration, vous verrez en lisant ceci
que vous n'aurez aucune limite... Avant de tout détailler, je vais vous
présenter rapidement les choses, avec un petit schéma pour faire plus
simple :-)

<div align=center><a href="static/upload/serveurjack.png"><img src="static/upload/serveurjack.png" width="400" align=center /></a></div>

Votre instrument est branché sur une carte son, elle-même reliée à votre
machine. Cette carte va envoyer le son qu'elle reçoit à un *serveur de
son* qui va gérer toutes les entrées et sorties de son du système (on
verra ça en détail plus tard). Ce logiciel va connecter l'entrée
physique (la guitare) à notre logiciel de simulation d'ampli, connecter
ce logiciel à celui de simulation d'effets, puis connecter sa sortie à
la sortie physique, soit nos enceintes.

Tout ceci se fera très facilement sous Linux, sans ligne de commande,
bref, que des choses qui sont à la portée d'un ingé son!!

Pour commencer, il faut du (bon) matos...
-----------------------------------------

</p>
Dans la partie "hardware" de ce tutoriel, il y a essentiellement 2
choses auxquelles faire attention, les deux *bouts* du schéma : la carte
son en entrée, et les enceintes en sortie. En fait, ça fera 3, si on
prend en compte la machine en elle même.

Ici, je ne pense pas que je pourrais être d'une grande aide pour vous,
puisque j'utilise simplement mon laptop. Je n'ai pas monté de machine
uniquement dédiée à la MAO, et je n'ai pas racheté de carte son. Je
branche ma guitare en direct sur la prise mini-jack de mon pc portable.
Si vous voulez montez votre machine pour faire principalement de la MAO,
privilégiez un bon processeur et de la RAM, utile pour gérer le signal
en temps réel et stocker vos enregistrements. Pour la carte son, et tout
le reste en général, vous pouvez vous rendre sur [linuxMao][], référence
en matière de MAO sous linux. Il faut bien faire attention d'en choisir
une qui soit compatible avec les pilotes Linux ainsi qu'avec notre
serveur de son.

Moi, pour l'instant, je ne fais pas beaucoup de musique, et je ne
cherche pas à avoir un rendu professionnel, donc mon matos est (pour
l'instant) suffisant.

En matière d'enceintes, je pense qu'il faudrait que je commence à
investir. Je n'ai que des petites enceintes du bureau, et ça devient
vraiment limite quand je pousse un peu sur les effets. Il me faudrait au
moins du 5.1, avec un caisson de basses et un peu plus de watts....

Donc pour débuter, vous pourrez sûrement faire avec le matériel que vous
avez déjà!! Il faut juste vérifier que vous recevez bien du son depuis
votre guitare. Pour se faire, branchez là sur votre ordinateur, puis
sous Ubuntu lancez le gestionnaire de son (allez dans les paramètres
systèmes, puis "Son", puis onglet "Entrée"). Montez le volume d'entrée,
puis grattez les cordes. Vous devriez normalement voir la barre de
niveau bouger, signe que du son arrive sur la carte.

<div align=center><a href="static/upload/param_entree_son.png"><img src="static/upload/param_entree_son.png" width="300"/></a></div>

Si vous n'avez pas de son, je ne vais pas trop pouvoir vous aider,
puisque chez moi tout à marché du premier coup... Je pense que le mieux
sera de mettre à jour vos pilotes, puis d'aller faire un tour sur
Google.... Sinon, vous pouvez aussi tenter d'avancer dans les étapes
suivantes. L'installation de logiciels tels que le serveur de son
pourrait peut être installer d'autres pilotes et composants qui feront
marcher le bazar.... bref, j'espère que tout aura marché pour vous ;-)

Dans tous les cas, remettez le volume d'entrée au minimum, c'est à dire
au niveau du premier petit trait vertical sur la gauche, pour avoir un
son "pur", c'est à dire qui ne sera pas modifié par le système.
L'amplification arrivera par la suite...

Et si on *apt-get*-ais un peu ?
-------------------------------

</p>
Maintenant que votre matériel est fonctionnel, passons aux logiciels
nécessaires. Vous avez deux solutions.

Si vous souhaitez la solution "clés en main", ou si vous voulez avoir
une machine et surtout un système qui ne fait que ça, je vous conseille
d'installer une nouvelle distribution Linux, à savoir [Ubuntu Studio][].
Cette dérivée d'Ubuntu est dédiée à tout ce qui touche aux médias et à
la création multimédia. Ce système à 4 pré-configurations que vous
pouvez mixer/installer, à savoir : audio, vidéo, graphisme 2D/3D &
développement de greffons audios. Dans notre cas, seul le premier nous
intéresse.

Le processus d'installation est très simple et basé sur celui d'Ubuntu.
Vous devriez facilement pouvoir vous en sortir, la seule différence est
qu'il n'y a pas d'interface graphique, vous devrez tout faire au clavier
mais ça reste très simple. Je ne fais pas de tuto, vous en avez un bon
[ici][].Au moment de l'étape *Software Selection*, ne sélectionnez QUE
*Audio Creation and Editing Suite*. Si vous en prenez d'autres, ou pas
celui-ci, vous n'aurez pas le support du noyau temps-réel. Suite à
l'installation, vous aurez un système très complet pour faire de la MAO
sous Linux!

Si vous souhaitez garder votre système Linux traditionnel et installer
en plus les bons logiciels, voici comment faire. Il nous faut 4 choses :
le serveur de son : **Jackd**, le simulateur d'ampli : **Guitarix**,le
simulateur d'effets : **Rakarrack** et notre enregistreur multi-pistes :
**Ardour**. Normalement, les paquets devraient être présents dans les
dépôts de votre distribution. Pour Ubuntu, voici la commande pour tout
installer d'un coup :

<pre>
    sudo apt-get install jackd qjackctl guitarix rakarrack ardour
</pre>

Le seul paquet inconnu ici est *qjackctl*, qui est une interface
graphique pour Jackd.

Comme je l'ai dit plus haut, les logiciels que nous venons d'installer
n'aurons pas de priorité temps-réel, puisque nous n'avons pas de noyau
qui supporte le temps-réel. Vous pouvez suivre [les explications de la
doc d'Ubuntu][] pour l'installer, puis donner les bonnes priorités aux
bons utilisateurs. Personnellement, je ne l'ai pas fait. Encore une
fois, pour ce que je fais, j'ai assez avec mon noyau standard :-P

Ces paquets sont le minimum syndical à avoir pour pouvoir commencer à
bidouiller et s'enregistrer. Notez que si vous avez déjà ampli/effets,
et un moyen de les brancher à votre ordi, vous devriez pouvoir vous
passer de guitarix et rakarrack... Cependant, en plus de ceux-ci,
d'autres petits logiciels peuvent être intéressants à avoir,
principalement pour les guitaristes. Petite liste (non exhaustive) :

-   Audacity : Autre enregistreur et mixeur de son. Je ne suis pas sûr
    qu'il tourne avec Jack.... Mais peut être utile pour de la post-prod
    sur un fichier son....
-   Hydrogen : Boite à rythmes, sympa pour rajouter une batterie sur vos
    compos ;)
-   Lingot : Accordeur
-   TuxGuitar : Éditeur de tablatures, équivalent de GuitarPro 5 en
    version libre. Indispensable pour les guitaristes :-P

</p>

Au fait, on peut faire quoi avec tout ça ?
------------------------------------------

</p>
Et bien, on peut faire plein de choses!! Comme je le disais plus haut,
on va pouvoir simuler notre ampli, notre rack d'effets, puis enregistrer
le tout.

### Le serveur de son : Jackd

</p>
Avant de faire de la MAO sous Linux, il faut une bonne brique de départ.
Cette brique va recevoir le son, et c'est elle qui va choisir quoi en
faire. Cette brique, c'est Jackd, notre serveur de son. Nous l'avons
installé plus haut, ainsi qu'un interface graphique pour le piloter
(qjackctl). Lancez ce dernier programme (normalement, Applications \>
Multimédia \> QJackCtl). Il faudra toujours le lancer avant de faire de
la MAO. En effet, c'est lui qui gère tout le son qui transitera sur
votre machine. Sans lui, aucun des logiciels suivants ne fonctionnera.

<div align=center><a href="static/upload/jack.png"><img src="static/upload/jack.png" width="400" align=center /></a></div>

Cette interface est extrêmement simple. On ne se sert que de 4 boutons :
"Démarrer", "Arrêter", "Connecter" et "Quitter". "Démarrer " va lancer
le serveur, "Arrêter" va le stopper, "Quitter" quitte l'appli, et
"Connecter" et bien.... c'est plus complexe ;)

Comme son rôle l'indique, Jackd est un **serveur**. Cela sous-entend
donc qu'a un moment ou un autre, on aura des **clients**. Ce sont ses
clients que l'on va connecter entre eux. Nous aurons deux types de
clients :

1.  Les clients en lecture (ou ports de sortie) : les clients sur
    lesquels on va pouvoir lire, ceux qui nous enverrons du son.
2.  Les clients en écriture (ou ports d'entrée) : les clients sur
    lesquels on va écrire, ceux à qui on va envoyer du son.

</p>
Le rôle de notre bouton "Connecter", c'est ça : connecter les sorties
des uns, sur les entrées des autres. Voici ci dessous la configuration
que j'utilise le plus souvent. Vous voyez à gauche la colonne des
clients en lecture et à droite celle des clients en écriture. Vous
pouvez voir que je connecte la sortie du rack d'effets (rakarrack) sur
l'entrée d'*ardour*, mon enregistreur multi-pistes. Cela signifie que
tout le son qui aura été traité par rakarrack ira directement en entrée
d'ardour.

<div align=center><a href="static/upload/jack_connexions.png"><img src="static/upload/jack_connexions.png" width="400" align=center /></a></div>

Il y a deux clients spéciaux là dedans. *system*. Ce sont les clients
qui représentent votre carte physique. À gauche, l'entrée (ou notre
guitare) et à droite notre sortie (les enceintes).

### Le simulateur d'ampli : Guitarix

</p>
Guitarix est un bon simulateur d'ampli pour Linux. Il est découpé en
deux parties. La tête, et les effets. Personnellement, j'utilise très
peu les effets intégrés, je préfère utiliser ceux de Rakarrack.
L'avantage c'est que ça permet, quand on veux tester deux trois accords,
de ne pas avoir à lancer notre rakarrack ;-) Les deux parties (tête et
effets) sont deux clients séparés dans Jack. Le premier sera
*gx\_head\_amp* et le second *gx\_head\_fx*. Ce que je fais, c'est que
je connecte tout dans ce sens : *system --\> gx\_head\_amp --\>
gx\_head\_fx --\> ...*

<div align=center><a href="static/upload/guitarix.png"><img src="static/upload/guitarix.png" width="400" align=center /></a></div>

Pour obtenir la même vue que moi du logiciel, il faut activer la vue des
plugins (Greffons \> Show Plugin Bar), celle du rack d'effets (Greffons
\> Show Rack), puis l'accordeur (Options \> Tuner). Les plugins sont
simplement les effets que vous rajoutez dans le rack. Vous les ajoutez
en cliquant dessus dans le menu en haut à gauche. Je n'en ai pas ajouté
beaucoup, juste le "Rack Mono", la "Distorsion Multibande", le
"Compresseur", l'"Overdrive", le "Rack Stéréo" et l'équaliseur "3 Band
EQ".

C'est une config parmi d'autres. Je ne l'utilise pas beaucoup, c'est
tout ce que je pourrais vous dire dessus...

### Le rack d'effets : Rakarrack

</p>
C'est là que les choses deviennent drôles.

<div align=center><a href="static/upload/rakarrack.png"><img src="static/upload/rakarrack.png" width="400" align=center /></a></div>

Ce rack d'effets est vraiment très complet. Il dispose de nombreux
effets que vous pouvez organiser dans des racks. Je n'ai pas encore
regardé comment tout ça fonctionnait, comment on créait ses propres
racks en agençant ses effets, et pour cause, le logiciel possède déjà
une banque de racks (menu "Bank") très très complète, et pour l'instant
j'ai simplement utilisé ceux-ci, en modifiant deux-trois réglages de
pédales de temps en temps pour obtenir un truc plus à mon goût.

Pour vous donner un petit avant-goût, voici une petite vidéo trouvée sur
YouTube, où le monsieur présente un peu les possibilités du logiciel :

<div align=center><iframe width="420" height="315" src="http://www.youtube.com/embed/4Jb7BEsHwLc" frameborder="0" allowfullscreen></iframe></div>

Pour les connexions dans Jack : ... --\> gx\_head\_fx --\> rakarrack
--\> ...

### L'enregistreur : Ardour

</p>
Enfin, Ardour est un enregistreur qui permettra d'enregistrer votre son.

<div align=center><a href="static/upload/ardour.png"><img src="static/upload/ardour.png" width="400" align=center /></a></div>

Celui là, je ne l'ai quasiment pas utilisé, j'ai juste la base. On crée
une piste pour la guitare (Clic droit sous la case "Général" \> " New
Track"). Pour la connexion dans Jack, il faut étendre le groupe "Ardour"
des deux côtés (petites flèches à gauche du nom). On connecte ensuite la
sortie de Rakarrack vers l'entrée de cette piste dans Jack. Tous les
clients en sortie d'Ardour doivent être branchés sur "system", pour être
sûr de tout avoir dans les enceintes. On clique sur record (bouton
rouge) sur la piste guitare, idem dans la barre du haut. On fait "Play",
et on joue :-)

Si vous n'avez pas de son, allez dans "Options", puis "Ecoute de
Contrôle", puis sélectionnez "Écoute via Ardour". Normalement ça devrait
marcher ;)

Enfin...
--------

</p>
J'espère qu'avec tout ceci, vous aurez les bases pour bricoler un peu de
MAO sur votre Linux. Encore une fois, ceci n'est pas un tutorial. Juste
une présentation rapide de ce que j'utilise. Si vous en voulez plus,
vous pouvez me répondre en commentaire, via [twitter][], ou jeter un
coup d'oeil aux quelques liens ci dessous ;) Je vais continuer à jouer
un peu plus avec tout ça, et je referais des articles plus détaillés
pour mieux présenter les possibilités de chaque appli :)

*Enjoy, and keep rockin'...*

Liens
-----

</p>
[LinuxMao.org][]

[UbuntuStudio][]

[911 Tabs][] : Moteur de recherche de tablatures

[Image originale][]

  [linuxMao]: http://linuxmao.org/tikiwiki/tiki-index.php "http://linuxmao.org/tikiwiki/tiki-index.php"
  [Ubuntu Studio]: http://ubuntustudio.org/downloads "http://ubuntustudio.org/downloads"
  [ici]: https://help.ubuntu.com/community/Ubuntu%20Studio%20Fresh%20Install "https://help.ubuntu.com/community/Ubuntu%20Studio%20Fresh%20Install"
  [les explications de la doc d'Ubuntu]: http://doc.ubuntu-fr.org/jackd#activer_la_priorite_temps_reel "http://doc.ubuntu-fr.org/jackd#activer_la_priorite_temps_reel"
  [twitter]: http://twitter.com/_Quack1 "http://twitter.com/_Quack1"
  [LinuxMao.org]: http://linuxmao.org "http://linuxmao.org"
  [UbuntuStudio]: http://ubuntustudio.org "http://ubuntustudio.org"
  [911 Tabs]: http://www.911tabs.com/ "http://www.911tabs.com/"
  [Image originale]: https://secure.flickr.com/photos/25242931@N02/5793015653/ "https://secure.flickr.com/photos/25242931@N02/5793015653/"
