Title: Améliorer le fonctionnement de Thunderbird avec des comptes IMAP Gmail
Date: 2013-09-16 13:10
Author: Quack1
Category: Geek
Tags: Thunderbird, Mozilla, Gmail, Google, IMAP, planet-libre
Slug: thunderbird_gmail_ameliorer
Summary: Quand je synchronise mes comptes Gmail dans Thunderbird, j'ai remarqué qu'il était super lent, et qu'il arrivait même à ralentir complètement mon système. Ceci est causé par une nouvelle fonctionnalité présente sur Gmail, que l'on peut désactiver dans Thunderbird pour lui donner un coup de boost!

Si comme moi vous accédez à votre compte Gmail depuis [Mozilla Thunderbird](/tag/thunderbird.html), vous avez peut-être déjà observé des ralentissements de ce dernier.

Chez moi, ça lui arrivait de complêtement se figer, de récupérer mes mails en retard, de ne plus répondre ou de réagir en retard, ou de carrément utiliser 100% d'un CPU et de tout ralentir, alors que mon système disposait de pas mal de ressources pour le faire tourner. 

Pour vous donner une idée de ma config, j'utilise Thunderbird 24 (bêta) sur Ubuntu 13.04, avec 3 comptes Gmail et 3 comptes postfix [auto-hebergés](/pages/contact.html), plus 1 calendrier Thunderbird qui se synchronise avec le plugin [Lightning](http://www.mozilla.org/projects/calendar/). Et tous mes mails sont triés dans des dossiers et _LABEL_.

Et bien rassurez-vous, ça ne vient pas de votre machine ou de votre système, mais bien de Thunderbird.

Et plus particulièrement de la fonctionnalité _CONDSTORE_ activée depuis peu sur tous les comptes Gmail par Google. Cette fonction permet de mieux détecter et gérer les conflits entre plusieurs clients mails qui synchroniseraient les mêmes comptes.

La solution, pour empêcher que cette fonctionnalité ralentisse Mozilla THunderbird est plutôt brutale puisqu'elle consiste à complètement la désactiver dans le client mail. 

Pour cela, les étapes sont les suivantes :

1. Ouvrez le menu _Outils_ (sur Thunderbird 24, allez dans _Préférences_), puis _Options_ ;
1. Choisissez _Avancé_, puis dans l'onglet _Général_, cliquez sur _Éditeur de configuration_ ;
1. Cliquez sur _Je ferai attention, promis!_ ;
1. Tapez _condstore_ dans la barre de recherche ;
1. Le seul résultat devrait être _mail.server.default.use_condstore_ ;
1. La valeur est normalement à _True_ ;
1. Pour désactiver CONDSTORE, double-cliquez sur la ligne. La valeur devrait passer à _false_.


Pour moi ça a plutôt bien marché puisque mon Thunderbird est beaucoup plus réactif qu'avant, et comme je n'utilise qu'un seul client mail, pas de problème de conflits à régler!

J'espère que ça marchera aussi pour vous si vous avez les même problèmes.

&nbsp;

[Via ghacks.net](http://www.ghacks.net/2013/09/07/fix-gmail-imap-slows-thunderbird-mails-arriving-timely-fashion/)