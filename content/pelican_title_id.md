Title: Pelican : Ajouter automatiquement des attributs HTML 'id' aux titres
Date: 2014-05-22 19:43
Author: Quack1
Category: Blog
Tags: Blog, Pelican, Markdown, HTML, planet-libre
Slug: pelican_title_id
Summary: 
Lang: fr

Par défaut, avec [le moteur de blog Pelican](/tag/pelican.html), dans le code HTML, les titres (`<h1>`, `<h2>`, `<h3>`, etc) sont générés basiquement sans attribut `id`.

Par exemple, si dans ma source [Markdown](/tag/markdown.html) j'ai : 

	:::markdown
	Du texte

	# Un titre

	Re du texte

le code HTML suivant sera généré : 

	:::html
	<p>Du texte</p>
	<h1>Un titre</h1>
	<p>Re du texte</p>

L'inconvénient, c'est que sans attribut `id` dans les titres, on ne peut pas faire de lien direct à une partie. Par exemple, le lien `/article.html#un-titre` ne sera pas valide.

Il est possible avec Pelican et Markdown d'automatiser cela, en activant dans Pelican une extension Markdown nommée `headerid`. Elle est intégrée par défaut dans Markdown (en tout cas, elle l'est sur mon Ubuntu) donc elle ne nécessite aucune installation supplémentaire.

Pour l'activer, on ajoute simplement l'extension dans son `pelicanconf.py` :

	:::python
	MD_EXTENSIONS = ['headerid']

Et voilà. À chaque génération du blog, les titres disposeront d'un attribut `id` qui sera généré à partir du texte du titre. Si deux titres sont identiques, ils seront suffixés d'un numéro.

	:::html
	<p>Du texte</p>
	<h1 id="un-titre">Un titre</h1>
	<p>Re du texte</p>

Je peux donc désormais faire des liens sur [une partie bien précise d'un article](/homemade_guitar_rex.html#et-alors-on-fait-quoi-avec-tout-ca).

&nbsp;

Pour plus d'infos : 

- [La doc Pelican [en]](http://pelican.readthedocs.org/en/latest/settings.html) ;
- [L'extension headerid dans la doc Markdown [en]](http://pythonhosted.org/Markdown/extensions/header_id.html)