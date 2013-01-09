Title: Visualiser graphiquement vos expressions régulières en ligne
Date: 2013-01-09 22:03
Author: Quack1
Category: Geek
Tags: visualisation, regex, graphique

<div align=center><img src="static/upload/i_know_regex.png" width="600" align=center /></div>

Qui n'a jamais eu du mal à comprendre une grosse expression régulière plutôt tordue, avec des symboles et des conditions dans tous les sens ? On peut tomber dans certains cas sur des regex illisibles, même pour des développeurs spécialistes!

Pour faciliter le développement de ses expressions, voici un petit outil online, [Regexper](http://www.regexper.com/) qui permet de visualiser de façon graphique ce que votre motif va "matcher". 

Puisqu'un dessin vaut mieux qu'un long discours, voici une screenshot du site en question, avec la visualisation d'une expression régulière de matching d'adresse email : 
<pre>
[a-z0-9_\\+-]+(?:\\.[a-z0-9_\\+-]+)\*@[a-z0-9-]+(?:\\.[a-z0-9-]+)\*\\.(?:[a-z]{2,4})
</pre>

<div align=center><a href="static/upload/regexper.png"><img src="static/upload/regexper.png" width="700" align="center" /></a></div> 

Et puisqu'une bonne chose n'arrive jamais seule, le projet est sous Licence CC-BY-NC-SA-3.0, donc librement modifiable, et dispo sur [GitHub](https://github.com/javallone/regexper) :-)

[Source](https://twitter.com/matti_sg/status/288758421136764928 "Source sur twitter") : via [@fo0_](https://twitter.com/fo0_) & [@matti_sg](https://twitter.com/matti_sg/status/288758421136764928)

