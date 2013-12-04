Title: Utiliser des notes de bas de page avec Pelican en Markdown
Date: 2013-12-04 09:45
Author: Quack1
Category: Blog
Tags: Pelican, Blog, Markdown, Footnote, planet-libre
Slug: footnote_pelican
Summary: Pelican est magique. Il utilise toute la puissance de Markdown lors de la génération des articles, ce qui signifie qu'on peut même utiliser des notes de bas de page !

Pelican est magique. 

Plus ça va, et moins j'ai envie de repasser sur un moteur de blog comme Wordpress ou Tumblr.

On peut facilement lui [rajouter des thèmes]({filename}/pelican_notebook.md "Thème « Notebook » pour Pelican"), on peut y ajouter un [formulaire de recherche]({filename}/search_form.md "Un formulaire de recherche avec DuckDuckGo!"), ou encore utiliser la puissance de Git pour [publier automatiquement les nouveaux articles]({filename}/git_hooks_pelican.md "Publier automatiquement ses nouveaux articles sur le moteur de blog Pelican avec Git"). Et surtout, on peut écrire les articles avec [Markdown](https://quack1.me/tag/markdown.html "Tag #Markdown")

J'ai découvert hier qu'il était possible d'utiliser des notes de bas de page directement depuis Markdown, cette fonctionnalité étant prise en charge dans la bibliothèque Python-Markdown !

La syntaxe est très simple, et on peut définir des notes de plusieurs façons. Exemple de fichier source Markdown :

	:::Markdown
	Une footnote[^1] numérotée.

	Du texte

	Une définition[^!Def] d'un mot donnée en bas de page, ou encore[^footnote] un label pour la note, nommé « footnote ».

	[^1]: Le texte de la footnote numérotée.

	[^footnote]: Le texte de la footnote qui avait un label.

	[^!Def]: La définition du mot donné plus haut dans le texte.

		Cette définition fait plusieurs lignes,

		et chaque ligne est indentée.

Le texte des notes peut être placé partout dans la source de l'article (pas forcément en bas de l'article), et celui-ci peut également être multi-lignes, il suffit d'indenter chaque nouvelle ligne avec au moins 4 espaces.

Et le rendu est le suivant : 

---

_Une footnote[^1] numérotée._

_Du texte_

_Une définition[^!Def] donnée en bas de page, ou encore[^footnote] un label pour la note, nommé « footnote »._

[^1]: Le texte de la footnote numérotée.

[^footnote]: Le texte de la footnote qui avait un label.

[^!Def]: La définition du mot donné plus haut dans le texte.

	Cette définition fait plusieurs lignes,

	et chaque ligne est indentée.

---

Et comme vous le voyez, aux notes sont automatiquement associés des liens pour naviguer dans l'article plus facilement. Détail, vous n'êtes pas obligés de mettre le texte des _footnotes_ tout en bas de votre fichier source, Pelican se chargera de les placer en bas de l'article généré.

C'est quand même méga classe qu'un petit truc comme Pelican soit aussi puissant qu'un gros moteur de blog !

[Source](http://b.xd.cm/pelican-footnotes.html "Footnotes in Pelican with Markdown") via [@GetPelican](https://twitter.com/GetPelican "GetPelican sur Twitter")