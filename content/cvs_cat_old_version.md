Title: Lire un fichier versionné dans une de ses anciennes versions #git #hg
Date: 2014-01-06 20:28
Author: Quack1
Category: Geek
Tags: CSV, Git, Mercurial, planet-libre, Dev
Slug: cvs_cat_old_version
Summary: 
Lang: fr

Je l'ai déjà mentionné ici, j'[écris ce blog en Markdown](/tag/markdown.html), et je [versionne le tout avec Git]({filename}/git_hooks_pelican.md). Il m'arrive aussi d'utiliser Mercurial (`hg`), histoire de diversifier un peu les outils que j'utilise.

J'avais besoin tout à l'heure de récupérer le contenu d'un fichier, mais dans une ancienne version. Comme je ne suis pas non plus un pro des gestionnaires de versions, faire des `rebase`, naviguer dans les _commits_ et autres n'étaient pas vraiment au programme. J'ai donc cherché un autre moyen de le faire et je suis tombé sur une petite option sympa de Mercurial. 

	$ hg cat -r 42 post.md

Cette commande va lire le contenu du fichier `post.md` tel qu'il était à la révision **42**.

L'équivalent pour [Git](/tag/git.html) c'est ça (en remplaçant `<rev>` par l'identifiant du commit) :

	$ git show <rev>:path/fo/file.ext

[^1]: De même, Mercurial possède `hg addremove` pour ajouter au prochain commit tous les nouveaux fichiers et ceux modifiés et supprimer les fichiers qui n'existent plus. Je n'ai pas trouvé de façon simple de le faire en une commande avec git.

[Trouvé ici](http://blog.pilotsystems.net/2009/05/tutorial-francais-mercurial-hg "Un tutorial en français sur l'utilisation de Mercurial"), tout en bas de la page, et [ici](http://stackoverflow.com/questions/2071288/equivalent-in-git-of-hg-cat-or-svn-cat).