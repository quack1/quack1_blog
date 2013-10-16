Title: Retour sur l'utilisation de ZSH au quotidien sur Ubuntu
Date: 2013-10-16 09:58
Author: Quack1
Category: Linux
Tags: Bash, Zsh, Ubuntu, planet-libre, planet-ubuntu, Avis
Slug: zsh_avis
Summary: Depuis quelques mois, j'utilise zsh comme shell par défaut sur Ubuntu en lieu et place de bash qui est utilisé par défaut. Retour sur l'utilisation de ce shell au quotidien.

Dans [un billet du 16 Mai]({filename}/zsh_intro.md), je vous avais présenté le shell zsh, et certains des avantages qui me donnaient envie de l'utiliser. Depuis cette date, je l'utilise au quotidient sur mon poste perso en remplacement de bash qui est installé par défaut.

Et je peux vous dire qu'il vaut vraiment le détour. On trouve plein de petites améliorations qui font qu'au final il est beaucoup plus agréable de l'utiliser plutôt que bash 😉

Le premier avantage de zsh est, incontestablement, le dépôt [oh-my-zsh](https://github.com/robbyrussell/oh-my-zsh), qui rajoute énormément de thèmes et d'exemples de configurations à zsh, ce qui le rend utilisable dès le début, sans configuration, avec énormément de fonctionnalités.

Ensuite, plein de petits trucs — qui paraîssent inutiles au premier abord — deviennent clairement indispensables au fil du temps. Certains d'entre eux proviennent des plugins zsh. Il en existe un très grand nombre, notamment pour ssh, git, python, mercurial, screen, ...

Liste non exhaustive de ce que j'aime dans zsh :

- La suppression de **mots** avec ˄W. Dans bash, un ˄W supprime _tout_ avant le curseur jusqu'au prochain espace. Avec zsh, la suppression s'arrête au prochain _word separator_, comme « / » par exemple. C'est très utile quand on fait des _cp_ à répétition, et qu'on souhaite juste changer le dernier sous-répertoire!
- Si on souhaite naviguer dans sa ligne de commande avec des `Ctrl+<ARROW KEY>`, le curseur se déplacera également de mot en mot, et non jusqu'au prochain espace ou simplement de caractères en caractères.
- Il ne faut qu'un seul appui sur `<TAB>` pour afficher la liste des fichiers accessibles avec la complétion automatique, contre deux dans bash. Ça peut paraître rien, un seul appui sur une touche, mais à la fin de la journée vous aurez gagné un bon paquet de temps 😉 ;
- La complétion automatique, tant que j'en parle, continuons. zsh peut auto-compléter même si les noms des répertoires ne sont pas complets. Exemple : si je tape dans mon shell `cd ~/I/S/` et que je fait `<TAB>`, zsh auto-complètera automatiquement la ligne en `cd ~/Images/Screenshots` ;
- Notez aussi que l'auto-complétion n'est pas sensible à la casse. Donc si vous vous trompez entre majuscules et minuscules, l'auto-complétion marchera aussi 😎 ;
- L'auto-complétion fonctionne aussi avec des commandes systèmes. Par exemple, avec la suite `ip`. Un `$ ip route<TAB><TAB>` affichera toutes les options qu'il est possible d'utiliser, avec une ligne d'aide à côté. Il est aussi possible d'avoir de l'auto-complétion sur les _hosts_ ssh (mais je crois que c'est natif dans bash aussi), et surtout, de l'auto-complétion à distance lors des _scp_!
- ...

J'ai sûrement trouvé d'autres choses sympas dans zsh, mais je n'ai pas tout noté et bien évidemment, je n'ai pas tout retenu. Si je pense à d'autres choses, je mettrais mon billet à jour pour maintenir la base que j'ai ici!

Dans tous les cas, n'hésitez pas à migrer vos machines sur zsh, à peu près tout ce qui se fait sur bash est compatible, et vous aurez en plus plein d'améliorations qui vous faciliteront la vie!

&nbsp;

_Au passage, je viens de découvrir tous les smileys de la table Unicode, donc oui, j'en ai truffé tout mon article 😁_