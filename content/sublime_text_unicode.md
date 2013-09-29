Title: Taper de l'Unicode dans Sublime-Text
Date: 2013-09-29 22:09
Author: Quack1
Category: Geek
Tags: Sublime-Text, Unicode, planet-libre
Slug: sublime_text_unicode
Summary: Dans Sublime-Text, on ne peut pas de base taper des caractères Unicode. Voici la marche à suivre pour activer cette fonction.

J'ai déjà sûrement le dire sur ce blog ou sur [Twitter](https://twitter.com/_Quack1), j'utilise l'éditeur de texte [Sublime Text](http://www.sublimetext.com/) qui est, pour moi, l'éditeur de texte le plus avancé du moment (_boouh, il utilise même pas <s>vim</s>Emacs_).

Le seul problème que j'ai, est que l'on ne peut pas y taper de l'[Unicode](https://fr.wikipedia.org/wiki/Unicode) avec le raccourci clavier traditionnel `Ctrl+Shift+U`. La raison ? Cette combinaison de touches est déjà _mappée_ à une autre action dans Sublime-Text, le _soft-undo_.

Je n'ai pas réussi à trouver à quoi ça servait, donc je l'ai désactivée dans Sublime-Text, pour que le raccourci natif d'Ubuntu soit pris en compte pour l'Unicode!

Pour cela, allez dans _Préférences_ puis _Key Bindings - Default_. Faites une recherche sur `ctrl+shift+u`, et commentez la ligne.

Redémarrez Sublime-Text, et vous pourrez taper des caractères Unicode sans problème! :)

[Via SuperUser.com](http://superuser.com/questions/510907/unicode-composition-in-sublime-text)