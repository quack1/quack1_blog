Title: Les perles de @climagic (et co)
Date: 2012-09-25 21:47
Author: Quack1
Category: Linux
Tags: admin, bash, cli, climagic, command, fun, scripts, tricsks, usefull, planet-libre
Summary: Florilège des commandes partagées par @climagic.

Ça commence à faire un ~~petit~~ bon moment (juste 3 ou 4 mois) que je
n'ai rien publié sur ce blog. Un retour tout en douceur s'impose donc,
et pour cela, je vais faire d'une pierre deux coups, puisque je vais
également vider mes favoris [Twitter][] :-)

En effet, depuis pas mal de temps, je follow le compte [@climagic][],
qui publie plusieurs fois par jour des commandes bash un peu "tunées"
qui permettent de réaliser des actions souvent utiles, parfois drôles,et
de temps en temps totalement inutiles (et de fait, Oh combien
nécessaires dans les alias de tout bon admin système :D ). Et comme je
trouve souvent ces commandes plutôt cools, je les mets dans mes favoris
Twitter pour m'en rappeler et les rajouter dans mes alias par la suite.
Sauf que, comme tout bon g33k qui se respecte, je n'avais encore jamais
fait de tri là dedans et je me retrouve avec une liste de favoris énorme
(CTB, oui, je sais... :P ).

J'ai donc testé tout ce que j'avais, pour ne garder que la crème de la
crème , autant pour vous que pour moi (comme ça, j'en garde une trace!).
~~Et vu que je suis sympa, je vais vous filer un petit script à la fin
qui rajoutera tout ces alias à votre *.bashrc* :-).~~ EDIT : finalement,
j'avais trop de commandes, la flemme de faire un script ce soir, je
verrais plus tard.. :P

**Disclaimer : Les commandes présentées ici sont toutes, sauf mention
contraire, l'oeuvre de [@climagic][] et tous les droits lui reviennent**

**Disclaimer 2 : Certaines des commandes présentées ici sont très
simples et connues de beaucoup de barbus, cependant, elles pourraient
être utiles à des gens qui débutent sous Unix-GNU/Linux et qui ne
connaissent pas tous les rouages de la chose :)**

- <code>$ mkdir -p maildir/{tmp,cur,new}</code> : Utilisation des accolades "{", qui
    permettent d'appeler la commande successivement avec toutes les
    valeurs entre les accolades, séparées par des virgules. En réalité,
    la commande équivaut à <code>mkdir -p maildir/tmp; mkdir -p maildir/cur; mkdir -p maildir/new ;</code>
- <code>$ sed '/\^$/d' prog.c \>
    proc-condensed.c* </code>: Récupère toutes les lignes non vides
    (excodession régulière '\^$/d') du fichier *prog.c* et place le
    résultat dans *prog\_condensed.c ;*
- <code>find . -ls | sort -n -k 7 | tail -5 </code> : Affiche les 5 plus gros
    fichiers présents dans l'arborescence ;
- <code>$ EXTIP=$(curl -s
    "whatismyip.org")</code> : Défini une variable globale qui
    contiendra votre adresse IP publique ;
- <code>$ rev \<\<\< "sentence to
    reverse"</code> : Inverse le sens des lettres de la phrase ;
- <code>$ exiv2 -k -F rename \*.jpg</code>
    : Renomme tous les fichiers *.jpg* du répertoire courant en leur
    donnant un nom de la forme "YYYYMMDD\_HHmmSS.jpg", en récupérant les
    informations de date/heure dans les données EXIF de la photo ;
- <code>$ jp2a ubuntu\_logo.jpg -b
    --color</code> : Converti une image JPEG en ascii art dans votre
    terminal. L'option '--color' active la couleur, le '-b' dessine une
    bordure autour de l'image. Exemple dans l'image plus bas
    :P(nécessite d'avoir activé les dépôts universe (pour Ubuntu et
    dérivés en tout cas...)) ;
- <code>$ dd if=/dev/VG0/var | gzip -c - \>
    /backups/var-image.gz</code> : Crée un backup du répertoire
    */dev/VG0/var ;*
- <code>$ acronym(){ elinks -no-numbering
    -dump "acronymfinder.com/$1.html" |sed -r '/(\*{4,}|This
    definition)/!d'; }</code> : Fonction utile qui recherche sur le Web
    la définition d'un acronyme. Exemple :
    <code>$ acronym HTTP
    </code>
- <code>$ sshfs user@remotehost:/remotedir
    mydir</code> : Monte un répertoire distant comme un répertoire
    local un utilisant FUSE et SSH ;
- <code>$ lsusb -v | egrep
    "(\^Bus|bcdUSB)"</code> : Liste les périphériques USB connectés
    ainsi que la version utilisée (USB2, USB3, ...) ;
- <code>$ openssl s\_client -crlf -quiet
    -connect \<hostname\>:\<port\></code> : Démarre une connexion SSL
    avec la machine donnée sur le port défini, par exemple pour tester
    des protocoles sécurisés comme HTTPS (équivalent à un
    <code>nc</code> mais en sécurisé ;) ) ;
- <code>$ gnutls-cli -s --crlf \<hostname\>
    -p \<port\></code> : Idem que la précédente ;
- <code>$ pdftohtml -stdout my.pdf \>
    my.pdf.html</code> : Exporte un document PDF vers une page HTML ;
- <code>$ mcd() { [[ -n "$1" ]] && mkdir -p
    "$1" && cd "$1"; }</code> : Fonction qui crée un répertoire (
    <code>mkdir</code> ) puis se déplace (
    <code>cd</code> ) dans celui-ci ;
- <code>$ mcd() { mkdir -p "${@}" && cd
    "${1}"; }</code> : Comme la précédente, à la différence que l'on
    peut créer plusieurs répertoires d'un coup, puis se déplacer dans le
    codemier d'entre eux ;
- <code>$ netstat -nape --inet</code> :
    Affiche la liste des connexions actives ;
- <code>$ netstat -lepunt</code>: Affiche la liste des ports TCP et
    UDP qui sont en mode LISTEN et le processus/user associé ;
- <code>$ quvi --exec 'mplayer %u'
    '\<url\>'</code> : Lit une vidéo YouTube dans mplayer sans passer
    par Flash. By [@gordontesos][] ;
- <code>$ getent services
    \<port\_number\></code> : Cherche dans la table locale des services
    celui qui est associé au port donné en paramètre ;
- <code>$ \<command\> ;xmessage -nearmouse
    "DONE"</code> : Après l’exécution de la commande, affiche une boîte
    de dialogue contenant le texte "DONE" près de la souris ;
- <code>$ \<command\> ;zenity --info
    --text="DONE"</code> : La même que précédemment, mais en utilisant
    le programme <code>zenity</code> (fenêtre
    GTK+) ;
- <code>$ for m in {0..200}; do date -d
    "2012-07-13 + $m months";done|grep -i \^Ven</code> : affiche la
    liste des prochains vendredis 13 dans les 200 prochains mois
    (dédicace aux superstitieux comme moi ;) ). Si votre système est en
    anglais, remplacer le "Ven" par "Fri" (pour "Friday") ;
- <code>$ montage -geometry 1280x1024+4+4
    ubuntu.jpg netbsd.jpg debian.jpg backtrack.jpg -tile x2
    distros.jpg</code> : Réalise un montage avec 4 images, de 1280px
    par 1024px, en réalisant 2 lignes de 2 colonnes. (Exemple plus bas)
    ;
- <code>$ sox song.wav -t wav - pitch 1200 |
    play -</code> : Joue la piste audio "song.wav", avec un pitch de
    1200, soit 12 demi-tons au dessus, ou 1 octave plus haut que le
    morceau original. (Paquet "sox" dans les dépôts Universe, installer
    aussi "libsox-fmt-all" pour lire des mp3 ou des ogg) ;
- <code>$ pwd -P</code> : Affiche le
    répertoire courant, en remplaçant les liens symboliques par le
    chemin (P)hysique ;
- <code>$ awk '$9 == "404" {print $7}'
    access.log |sort|uniq -c|sort -rn| head -n 50</code> : Affiche la
    liste des 500 urls menant à des erreurs 404 les plus renvoyées par
    le serveur local Apache (généralement, répertoire
    '/var/log/apache2'). Via [@warzauwynn][]
- <code>$ ps -e -orss=,pid=,args= | sort -b -k1n | pr -TW$COLUMNS</code> : Trie les processus les plus gourmands en mémoire. Via [@Albahtaar][] ;
- <code>$ touch -r origfile newcopy</code>
    : Donne à newcopy le timestamp de origfile ;
- <code>$ aplay /bin/bash</code> : L'alarme
    du pauvre. Lit un fichier quelconque comme s'il était un média audio
    (conseil : baissez le son de votre machine avant de lancer la
    commande ;-) ) ;
- <code>$ trickle -d 50 wget \<url\></code>
    : Utilise <code>trickle</code> pour
    limiter la bande passante descendante d'une commande à 50 kB/s ;
- <code>$ \>file</code> : Crée, ou supprime
    son contenu s'il existe déjà, le fichier 'file' ;
- <code>$ scrot* </code>: Utilitaire
    permettant de faire des captures d'écrans directement depuis un
    terminal ;
- <code>$ rename 's/ /\_/g' \*</code> :
    Renomme tous les fichiers du répertoire courant en remplacant les
    espaces par des underscores '\_' ;
-   Sur un "serveur" : <code>$ nc -l 8765 \<
    video.avi</code>, et sur un "client" :
    <code>$ nc server 8765 \> mplayer -cache
    1000 -</code> : Service de streaming perso. Un serveur streame la
    vidéo, le client récupère le flux et le fait lire par
    <code>mplayer</code> ;
- <code>$ awk -F: {'print $1 ":" $2'}
    messages |uniq -c</code> : Affiche le nombre de messages syslog par
    minutes ;
- <code>$ declare -f func\_name</code> :
    Affiche la définition d'une fonction définie par l'utilisateur ;
- <code>$ for d in {1..5}; do printf
    ${RANDOM: -1:1}; done; echo</code> : Génère un code secret
    "aléatoire" à 5 chiffres ;
- <code>$ find . -empty -type d</code> :
    Liste les sous-répertoires vides. Via [@mariosangiorgio][] ;
- <code>$ ps aux | awk '{if ($8=="Z") {
    print $2 $11}}</code> : Affiche les PID et nom des processus qui
    sont dans l'état 'ZOMBIE' ;
- <code>$ debtree coreutils \> coreutils.dot
    && dot -T png -o coreutils.png coreutils.dot</code> : Crée une
    image contenant le graphe des dépendances du paquet 'coreutils'. Via
    [@fern4lvarez][] ;
- <code>$ ping -i0.2 \<url\>|awk -F[= ]
    '/time=/{t=$(NF-1);f=3000-14\*log(t\^27);c="play -qn synth pl " f "
    fade 0.1s 1 &";print $0;system(c)}'</code> : Joue des sons en
    fonction du temps nécessaire pris par les paquets ping pour revenir
    à votre machine ;
- <code>$ lsof /dev/video0</code> : Liste
    les processus qui utilisent la webcam ;
- <code>$ ls -1d \~/.\* | grep -v '\~$' |
    wc -l</code> : Compte le nombre de 'dot files' dans votre Home
    Directory. Via [@bortzmeyer][]
- <code>$ last | grep -A1 -m1 "\^$(whoami)
    "</code> : Affiche la dernière personne à s'être connectée avant
    vous sur votre machine ;
- <code>$ sort -nt . -k 1,1 -k 2,2 -k 3,3 -k
    4,4 IPAddresses.txt</code> : Trie une liste d'adresses IPv4 ;
- <code>$ exif \*.JPG | grep "F-Number" |
    cut -d| -f2 | sort | uniq --count | sort -n</code> : Affiche la
    liste des focales les plus utilisées à partir des données EXIF de
    vos photos. Via [@b\_doin][] pour [@gchampeau][] ;

</p>
Et voilà, je pense avoir fait le tour de la plupart des commandes que
j'avais en stock, si j'en trouve, je mettrais à jour l'article et
diffusant la MAJ sur Twitter ;-)

<div align=center text-align=center><a href="static/upload/montage_combined.jpg"><img src="static/upload/montage_combined.jpg" width="450" align="center" /></a><br /> $ montage -geometry ...</div> 
<div align=center text-align=center><a href="static/upload/jp2a.png"><img src="static/upload/jp2a.png" width="450" align="center" /></a><br /> $ jp2a </div> 

  [Twitter]: http://twitter.com/_Quack1 "@_Quack1"
  [@climagic]: https://twitter.com/climagic "@climagic"
  [@gordontesos]: http://twitter.com/gordontesos "@gordontesos"
  [@warzauwynn]: http://twitter.com/warzauwynn "@warzauwynn"
  [@Albahtaar]: http://twitter.com/albahtaar "@Albahtaar"
  [@mariosangiorgio]: http://twitter.com/mariosangiorgio "@mariosangiorgio"
  [@fern4lvarez]: http://twitter.com/fern4lvarez "@fern4lvarez"
  [@bortzmeyer]: http://twitter.com/bortzmeyer "@bortzmeyer"
  [@b\_doin]: http://twitter.com/b_doin "@b_doin"
  [@gchampeau]: http://twitter.com/gchampeau "@gchampeau"
