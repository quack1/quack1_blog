Title: Pelican 3.4 is out !
Date: 2014-07-04 09:37
Author: Quack1
Category: Blog
Tags: Blog, Pelican, planet-libre
Slug: pelican_3-4
Summary: 
Lang: fr

Une nouvelle mouture du moteur de blog [Pelican](http://getpelican.com), la 3.4, vient tout juste de sortir !

La principale nouveauté est la meilleure gestion de la regénération du blog. Auparavant, à chaque mise à jour (ajout/suppression d'un article, ajout/suppression d'une catégorie, ajout d'une ligne à un article), tout le blog était regénéré de zéro.

Désormais ce n'est plus le cas, puisqu'uniquement le contenu modifié est regénéré.

&nbsp;

Plusieurs autres modifications ont également été apportées, voir le CHANGELOG pour plus de détails : 

	:::rst
	 Release history
	 ###############

	 3.4.0 (2014-07-01)
	 ==================

	 - Speed up content generation via new caching mechanism
	 - Add selective post generation (instead of always building entire site)
	 - Many documentation improvements, including switching to prettier RtD theme
	 - Add support for multiple content and plugin paths
	 - Add ``:modified:`` metadata field to complement ``:date:``.
	    Used to specify the last date and time an article was updated independently from the date and time it was published.
	 - Add support for multiple authors via new ``:authors:`` metadata field
	 - Watch for changes in static directories when in auto-regeneration mode
	 - Add filters to limit log output when desired
	 - Add language support to drafts
	 - Add ``SLUGIFY_SOURCE`` setting to control how post slugs are generated
	 - Fix many issues relating to locale and encoding
	 - Apply Typogrify filter to post summary
	 - Preserve file metadata (e.g. time stamps) when copying static files to output
	 - Move AsciiDoc support from Pelican core into separate plugin
	 - Produce inline links instead of reference-style links when importing content
	 - Improve handling of ``IGNORE_FILES`` setting behavior
	 - Properly escape symbol characters in tag names (e.g., ``C++``)
	 - Minor tweaks for Python 3.4 compatibility
	 - Add several new signals
