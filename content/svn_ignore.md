Title: [NOTE] Ignorer des fichiers dans un dépôt SVN
Date: 2014-09-29 20:01
Author: Quack1
Category: Geek
Tags: SVN, Linux, planet-libre, planet-ubuntu
Slug: svn_ignore
Summary: svn étant quand même moins _user-friendly_ que git, petite note en passant pour lui demander d'ignorer certains fichiers du répertoire de travail.
Lang: fr

[svn](/tag/svn.html) étant quand même moins _user-friendly_ que [git](/tag/git.html)[^1], petite note en passant pour lui demander d'ignorer certains fichiers du répertoire de travail.

	:::bash
	$ svn propset svn:ignore "*.pyc" .

_Attention au point à la fin de la commande._

[Via](http://www.math-linux.com/linux-2/commande-du-jour/article/svn-comment-ignorer-des-fichiers-ou-des-repertoires-avec-subversion)

[^1]: Où ça un troll ?