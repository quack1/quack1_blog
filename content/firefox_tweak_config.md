Title: Améliorer Firefox en quelques coups de about:config
Date: 2013-10-08 18:20
Author: Quack1
Category: Geek
Tags: planet-libre, Firefox, Mozilla
Slug: firefox_tweak_config
Summary: Firefox, le navigateur web de Mozilla est entièrement customisable, notamment grâce à ses nombreux add-ons. Mais il est encore possible de l'améliorer en modifiant sa configuration interne.

Le site [LifeHacker](http://lifehacker.com/the-best-about-config-tweaks-that-make-firefox-better-1442137111) propose aujourd'hui une série d'une dizaine d'options permettant de customiser Firefox pour améliorer son fonctionnement, en utilisant les options `about:config` du navigateur.

Je vous laisse parcourir le lien si vous voulez tous les avoir, perso j'en ai retenu 3 :

### Désactiver la vérification de compatibilité des plugins

Certains plugins ne sont pas _officielement_ supportés par Firefox, mais ils sont quand même utilisables avec la version que vous avez du navigateur. Pour supprimer la vérification au démarrage, passez la valeur `extensions.checkCompatibility` à `False`.

### Visualiser les onglets ouverts dans Ctrl+Tab

À la manière de `Alt+Tab` sur votre système, Firefox dispose du raccourci clavier `Ctrl+Tab` qui vous permet de naviguer entre les onglets ouverts. Il est possible de visualiser les onglets ouverts avant qu'ils s'affichent en passant la valeur `browser.ctrlTab.previews` à True.

### Modifier le nombre de lignes et colonnes de la page « Nouvel Onglet »

Enfin, quand vous ouvrez un nouvel onglet dans Firefox, il affiche une page qui contient les 9 pages que vous visitez le plus. Il est possible de modifier le nombre de lignes et colonnes en modifiant les options `browser.newtabpage.rows` et `browser.newtabpage.columns`

&nbsp;

Et voilà, ce n'est pas grand chose, mais c'est tout ces petits riens qui font des grands tout! ;-)