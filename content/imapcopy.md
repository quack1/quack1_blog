Title: Migration de comptes mails IMAP
Date: 2014-06-30 19:36
Author: Quack1
Category: Linux
Tags: Linux, Mail, IMAP
Summary: Changer de provider de mails, notamment pour avoir une meilleure vie privée, c'est bien. Garder l'histoirique de ses anciens mails, c'est mieux. **imapcopy** est là pour ça.

Depuis l'affaire Snowden, tout le monde nous rebat les oreilles à coup de « GMail c'est nul », « bouh, Microsoft vole votre vie privée » et autres joyeusetés. Méticuleux comme vous êtes, vous avez donc changé de _provider_ de mails pour un service plus respectueux de la vie privée ou — mieux — pour votre propre serveur de mails.

Sauf qu'en changeant de service, vous perdez également tout vos anciens mails présents sur le précédent serveur. Mais il existe un outil, **imapcopy** qui permet de récupérér vos mails ! 

Il va se connecter à votre ancien serveur, récupérer tous les mails, puis les resynchroniser sur le nouveau serveur.

&nbsp;

Sur toutes les bonnes distribs, ça s'installe simplement.

    :::bash
    sudo apt-get install imapcopy

On crée ensuite un fichier de configuration comme celui donné ci-dessous.

    :::bash
    $ cat imapcopy.cfg
    SourceServer source.tld
    SourcePort 143

    DestServer dest.tld
    DestPort 143 
    # SourceUser SourcePassword DestinationUser DestinationPassword 
    Copy "user@source.tld" "password" "user@dest.tld" "password2"
    Copy "user2@source.tld" "PASSWORD" "user2@dest.tld" "PASSWORD2"

Il est donc possible de migrer, d'un seul coup, les mails de plusieurs comptes sur le même serveur. Pour lancer la migration, on lance `imapcopy` qui va récupérer le fichier de conf. dans le répertoire courant.

    :::bash
    imapcopy

&nbsp;

Attention, tous les échanges se font ici en clair (et pas de façon chiffrée). Pour cela, vous pouvez utiliser un tunnel ssh (si vous avez la main sur la machine distante) ou bien l'utilitaire `stunnel`.

    :::bash
    sudo apt-get install stunnel

On lance ensuite la création des tunnels :

    :::bash
    stunnel -c -f -d 1143 -r source.tld:993 -P ''
    stunnel -c -f -d 1144 -r dest.tld:993 -P ''

Et on n'oublie pas de modifier le fichier de configuration pour utiliser ces nouveaux ports :

    :::bash
    $ cat imapcopy.cfg
    SourceServer 127.0.0.1
    SourcePort 1143
    
    DestServer 127.0.0.1
    DestPort 1144

&nbsp;

Vous pouvez également tester votre configuration avec un `imapcopy -t`.

&nbsp;

_Cet article est une traduction libre et adaptée de l'article d'[Emmanuel Revah](http://manurevah.com). L'[article source](http://manurevah.com/blah/en/p/Migrate-emails-with-imapcopy) est distribué sous licence CC-BY-NC-SA.