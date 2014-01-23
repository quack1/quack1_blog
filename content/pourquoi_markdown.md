Title: Pourquoi écrire en Markdown ?
Date: 2014-01-23 10:19
Author: Quack1
Category: Writing
Tags: Écriture, Markdown, planet-libre, planet-ubuntu
Slug: pourquoi_markdown
Summary: Depuis quelques temps, je parle beaucoup de [Markdown](/tag/markdown.html), de l'utilisation que j'en ai et des outils que j'utilise, mais jamais des raisons de cette utilisation. C'est désormais chose faite ! :)
Lang: fr

Depuis quelques temps, je parle beaucoup de [Markdown](/tag/markdown.html), de l'utilisation que j'en ai et des outils que j'utilise, mais jamais des raisons de cette utilisation. Je vais essayer de lister ici les quelques raisons qui me font utiliser Markdown au quotidien, et quelques pistes si vous voulez vous y mettre ! :)

<div align="center" style="color:#ccc;">☠</div>

J'ai d'abord choisi d'écrire en Markdown, un peu par _obligation_. Quand j'ai [migré le blog sur Pelican]({filename}/blog_v3.md) il y a presque un an, je me suis retrouvé à écrire tous mes billets en Markdown[^1]. Et c'est petit à petit que je me suis mis à ne trouver que — ou presque — des avantages au Markdown.

D'abord, il est super léger, et ne nécessite qu'un simple éditeur de texte. Les fichiers sont écrits en simple texte, en donc ne nécessite pas d'installer un quelconque logiciel supplémentaire sur son ordinateur (pas besoin de Microsoft Office, de LibreOffice, ou iWorks). À ma connaissance, tous les OS d'aujourd'hui disposent, en natif après l'installation, d'un éditeur de texte. Donc on peut écrite en Markdown sur tous les OS, sans rien installer. Même Windows a le _Bloc-Notes_ !

<!-- Image bloc note MD -->

L'avantage d'utiliser Markdown, c'est de posséder une syntaxe claire et légère pour définir la mise en forme. Par exemple, pour écrire une portion de texte en gras, il suffit de l'entourer de deux symboles `*` ou de deux `_`. Exemple : `J'aime **beaucoup** les Kinder` devient « J'aime **beaucoup** les Kinder ». Pour mettre du texte en italique, il suffit d'un seul de ces symboles (`_bonjour_` devient « _bonjour_ »).

On peut aussi écrire des listes en commençant les lignes par des tirets, faire des citations, des liens hypertextes, etc...

L'avantage d'une syntaxe aussi légère est — à mon avis — double : 

- Le fichier Markdown est lisible tel quel. En quelques minutes, vous êtes déjà habitué à comprendre que du texte entouré de deux étoiles est important, car en gras, que les lignes débutant par des tirets forment une liste, etc... Si vous ne me croyez pas, reprenez la capture d'écran du bloc-notes Windows un peu plus haut. Le texte est parfaitement lisible, même sans mise en forme[^2].
- Ensuite, on peut écrire du Markdown, avec de la mise en forme, n'importe où. Vous êtes devant un ordi, ouvrez un éditeur de texte. En voiture, dans le bus, le métro, sans PC, pas de souci ! Envoyez vous un sms, un mail, créez une note dans Evernote ou autre, et vous n'aurez à faire qu'un copier-coller une fois rentré chez vous pour retrouver votre texte, parfaitement mis en forme[^3].

<div align="center" style="color:#ccc;">☠</div>

Je trouve qu'un des principaux avantages du Markdown est justement ici : ne pas avoir à se soucier de la forme. Combien de fois est ce que vous avez fini des rapports ou des présentations parce que vous avez passé 80% du temps à mettre en forme trois phrases, pour vous rendre compte, après coup, que vous devez tout refaire parce que le contenu est trop grand/large/différent ? Avec Markdown, vous pouvez vous contrefoutre de la forme. Le plus important c'est ce que vous dites, c'est le contenu. Le reste, c'est du pipeau pour se donner un genre parce qu'on sort un document tout beau tout propre. Alors qu'au final, la forme, on s'en branle un peu, le plus important c'est ce qu'on met dedans.

Pour la petite histoire, j'ai des collègues qui pensent que, si vous leur passez un Word ou un PowerPoint « de travail » avec du texte noir sur fond blanc, c'est un travail baclé que vous avez fait à l'arrache. Juste parce qu'il n'y a pas de mise en forme.

Le meilleur contre-exemple, c'est quand même les scénarios. Les mecs écrivent des histoires de malades, dépensent des millions de dollars pour tourner des supers films avec des caméras 4K (TK), et au final le script est juste [écrit en `Courier New` et sans mise en forme de malade](http://www.backstory.fr/courier-12-majuscules-et-formats-de-scenarios/)[^4].

Pour ma part, quand je veux générer des PDF ou des ODT un peu classes, j'utilise [pandoc](http://johnmacfarlane.net/pandoc/) et des feuilles de style, propres au format de destination. Je ne vais pas faire de tuto (enfin, pas tout de suite), mais [ce site est pas trop mal pour débuter](http://enacit1.epfl.ch/markdown-pandoc/).

<div align="center" style="color:#ccc;">☠</div>

Enfin, je ne peux pas finir ce — long — post sans parler des inconvénients de Markdown. Perso, je n'en ai pas vu des masses. Si tant est qu'on ait un éditeur de texte qui le supporte, la lecture d'un source `.md` est super simple, l'écriture aussi.

Générer des PDF ou autres, c'est un peu plus tendu pour les non connaisseurs, mais je des outils intègrent déjà ce genre de fonctionnalités (comme [Uberwriter]({filename}/uberwirter_markdown.md) par exemple).

Enfin, Markdown ne gère pas encore tout ce qu'on peut avoir envie de faire dans un document texte. Pour taper du texte « simple » (j'entends par là, du texte avec mise en avant (gras, italique, souligné), listes à puces ou numérotées, titres, liens, images, ...), c'est royal, mais quand on arrive sur des bibliographies ou des trucs un peu plus exotiques, c'est — à ma connaissance — pas géré nativement par Markdown[^5].

<div align="center" style="color:#ccc;">☠</div>

En conclusion : utilisez Markdown, c'est bon, ça mord pas, et ça fait de la place sur les disques !

Quelques liens que j'ai vu passer récemment chez [urbanbike](http://www.urbanbike.com) : 

- [Markdown, à quoi ça sert ?](http://www.urbanbike.com/index.php/site/perdu-avec-markdown-a-quoi-cela-sert-quelques-explications)
- [Apprendre Markdown simplement en 8 jours (**sans déconner, testez Markdown !**)](http://www.urbanbike.com/index.php/site/apprendre-markdown-en-8-jours)
- [Si vous voulez tester Markdown directement dans votre navigateur[^6]](https://stackedit.io/)
- [Utiliser Markdown en entreprise](http://www.urbanbike.com/index.php/site/communication-dentreprise-et-markdown) et [utiliser Markdown en entreprise (2)](http://www.urbanbike.com/index.php/site/communication-dentreprise-et-markdown-2)


[^1]: En même temps, j'avais un peu choisi Pelican pour ça aussi :p

[^2]: Et aujourd'hui, de nombreux éditeurs de texte (comme [Sublime-Text](/tag/sublime-text.html)) supportent le Markdown et mettent automatiquement le texte en forme. Voir [ici]({filename}/sublime_text_markdown_conf.md) par exemple.

[^3]: Chose parfaitement impossible avec Microsoft Office ou Libre Office, pour lesquels il faut refaire la mise en forme par la suite.

[^4]: Et, ici aussi, comme pour le Markdown, on regarde juste la mise en forme brute du texte : majuscules, minuscules, indentation du texte, et pas s'il est écrit en jaune, corps 16, souligné en rouge ;)

[^5]: Mais on peut, dans du Markdown, intégrer du code Html, ou du LaTeX aussi je crois. Je n'ai jamais essayé ça, si vous l'avez fait, je veux bien un retour d'xp :p

[^6]: L'appli est écrite en Html5, et reste stockée en cache dans votre navigateur, donc vous pourrez même l'utiliser hors-ligne.