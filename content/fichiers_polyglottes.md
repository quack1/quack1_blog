Title: Fichiers Polyglottes : Ou comment avoir 4 fichiers en un
Date: 2013-07-03 10:12
Author: Quack1
Category: Securité
Slug: fichiers_polyglottes
Tags: SSTIC 2013, Fichiers Polyglottes, Corkami, planet-libre, SSTIC
Summary: Présentation et démonstration de création des fichiers polyglottes. Les fichiers polyglottes sont des fichiers qui seront interprétés différement selon la façon dont ils seront lancés. Exemple : exécuter le programme lancera un programme binaire, l'ouvrir dans un navigateur affichera un code HTML, bien que le fichier d'origine soit reconnu comme un fichier PDF par le système.
Lang: fr
Status: draft

<div align=center><a href="static/upload/pass.png"><img src="static/upload/pass.png" width="300" align=center /></a></div>

Au [SSTIC](/tag/SSTIC.html) de cette année, une des conférences qui m'a le plus interessé était celle présentée par Ange Albertini et intitulée "Polyglottes Binaires et Implications". J'y ai en particulier découvert les fichiers polyglottes. J'ai rapidement résumé la conférence dans [ce billet](/sstic_2013_1.html).

Les fichiers polyglottes sont des fichiers qui apparaissent comme étant d'un certain type (exemple : un fichier PDF), mais qui pourtant seront interprétés différement si on les ouvre dans un autre programme. 

Par exemple, nous allons voir dans cet article comment créer un binaire ELF (exécutable Linux) qui contiendra également un PDF, une archive Jar (exécutable Java) et du code Html. Par contre, pour éviter que vous regardiez seulement comment qu'on fait sans lire les explications que j'aurais écrit avec patience juste pour vous, et ben je mettrais les lignes de commandes tout en bas de l'article! (Rassurez-vous, pour les plus pressés, vous pouvez toujours scroller ;-) ).

&nbsp;

Voici l'architecture du fichier polyglotte que l'on va créer : 

- Binaire ELF
- PDF
- Archive Jar
	- HTML

Et vous verrez que même si on n'a qu'un seul gros fichier, il est tout à fait possible d'ouvrir chacun des fichiers qu'il contient! Pour comprendre comment ça marche, il faut regarder un peu mieux l'organisation des formats de fichiers utilisés.

Les binaires ELF (si je ne me plante pas) doivent impérativement débuter par l'en-tête ELF, puis doit contenir toutes les instructions à exécuter. Les instructions s'exécutant "séquentiellement" suivant les appels à celles-ci, le programme va finalement s'arrêter à une instruction de type "EXIT" (c'est du pseudo-code, pas de l'ASM :P). Du coup, on peut bien mettre ce qu'on veut après, tant que le programme n'essaye pas d'exécuter ça comme des fonctions, ça devrait passer.

Le PDF est organisé comme l'ELF. Il doit (théoriquement) débuter par une signature PDF (sous la forme `%PDF-X.Y`). En pratique, tant que cette signature est localisée dans les 1024 premiers octects du fichier PDF, la plupart des visionneuses PDF ouvrent les fichiers sans problème. Donc, tant que notre binaire ELF ne fait pas plus d'1ko, en mettant un PDF après ça marche pas mal. Si vous vous demandez comment on détecte la fin d'un PDF (et vous avez raison de le faire), on peut remarquer que les fichiers se terminent par `%%EOF`.

Du coup, il nous reste à mettre après notre ELF et notre PDF une archive Jar qui contient elle-même du HTML.

Une page Html, c'est quoi ? Et bien je vais vous dire ce que c'est. C'est du texte qui commence par `<html>` et qui fini par `</html>`. Donc tout ce qui se trouve entre ces deux balises sera interprété par les navigateurs. Même si ces balises sont situés après 28Mo de pur binaire, ça fonctionnera.

Une archive Jar, ce n'est rien de plus qu'une archive Zip qui contient tous les fichiers `.class` Java ainsi qu'un fichier `MANIFEST`. Ce Jar doit impérativement se terminer à la fin du fichier. On peut quand même noter deux choses supplémentaires sur l'archive Jar : 

Les fichiers Class Java contiennent toutes les chaînes de caractères en clair. C'est à dire qu'en parcourant le fichier binaire, on pourra quand même lire les chaînes de type `String` de notre code Java. C'est cette particularité que nous allons utiliser pour intégrer notre code Html au code Java. Le navigateur tombera à un moment sur ces balises html et affichera le code interprété.

Le problème c'est que nos classes Java sont regroupées dans une archive Zip. Le Zip, je ne sais pas si vous le savez, mais il peut être compressé, ou non. S'il est compressé, on ne pourra pas accéder à la chaîne Html en clair, mais si on désactive la compression, notre code Html sera pleinement accessible.

&nbsp;

Pour résumer : 

- Le ELF doit être au début du fichier
- Le PDF doit commencer dans les 1024 premiers octets du fichier
- Le code Html doit être inclut comme variable `String` d'une des classes Java.
- L'archive Jar ne doit pas être compressée et doit terminer le fichier.

On remarque que toutes ces manipulations sont possibles pour deux raisons : 

1. Les formats de fichiers sont plutôt permissifs
2. Les lecteurs de fichiers sont assez laxistes avec les formats et tolèrent que le code actif ne commence et ne termine pas le fichier effectivement lu.

On peut ensuite imaginer plein d'applications à ce type de fichiers. La plupart des anti-virus doivent détecter rapidement si un fichier est infecté ou non. Du coup, bien souvent, si le fichier semble être un PDF, il n'est analysé que comme un PDF. S'il possède également du code binaire ou du Javascript malicieux, il ne sera pas analysé comme tel.

Je sais que vous en avez envie, donc passons à la pratique!

On a deux façons de créer notre fichier polyglotte : écrire chacun des 3 fichiers à la main en assembleur/binaire, tel [que le fait Ange Albertini](http://code.google.com/p/corkami/wiki/mix), ou bien à [l'arrache](http://www.byatoo.com/la-rache/) comme je l'ai fait moi, de la manière suivante :

&nbsp;

Commençons par créer un petit binaire tout simple à partir d'un code écrit en C, qui va simplement afficher un texte à l'écran.

	:::C
	#include <stdio.h>
	int main(void){
		printf("quackiNuX [elf]\n");
		return 0;
	}

On compile : 

	:::zsh
	gcc -Wall quackiNuX.c -o quackiNuX.elf

&nbsp;

Le fichier PDF est réalisé simplement depuis Libre Office. Une ligne de texte, et on exporte en PDF.

<div align=center>
	<a href="/static/upload/quackinux_pdf.png"><img src="/static/upload/quackinux_pdf.png" align="center" width="250"/></a>
</div>

&nbsp;

Le code source Java est identique au code C, on y rajoute simplement une variable globale contenant le code Html : 

	:::java
	public class QuackiNuX{
		private static final String h = "<html><body><style>body { visibility: hidden; } .n { visibility: visible; position: absolute; padding: 0 1ex 0 1ex; margin: 0; top: 0; left: 0; }</style><div class=n><h1>quackiNuX [Html inside Java]</h1><script>alert('quackiNuX [Javascript inside Html inside Java]');</script></div><!--";
		public static void main(String[] args){
			System.out.println("quackiNuX [Jar]");
		}
	}

&nbsp;

Enfin, pour créer notre fichier polyglotte, on concatène tous les fichiers à la suite les uns des autres : 

	:::zsh
	$ cat quackiNuX.elf quackiNuX.pdf quackiNuX.jar > mix/quackiNuX.mix
	$ cd mix/
	$ ls
	quackiNuX.mix
	$ cp quackiNuX.mix{,.jar}
	$ cp quackiNuX.mix{,.pdf}
	$ cp quackiNuX.mix{,.html}
	$ ll
	total 128
	-rwxrw-r-- 1 quack quack 22328 juin  27 22:06 quackiNuX.mix
	-rwxrw-r-- 1 quack quack 22328 juin  27 22:06 quackiNuX.mix.html
	-rwxrw-r-- 1 quack quack 22328 juin  27 22:06 quackiNuX.mix.jar
	-rwxrw-r-- 1 quack quack 22328 juin  27 22:07 quackiNuX.mix.pdf
	$ md5sum *
	402fa683789e4b06dc42943d929cb24f  quackiNuX.mix
	402fa683789e4b06dc42943d929cb24f  quackiNuX.mix.html
	402fa683789e4b06dc42943d929cb24f  quackiNuX.mix.jar
	402fa683789e4b06dc42943d929cb24f  quackiNuX.mix.pdf

Les 4 fichiers sont identiques, et pourtant si on les ouvre tous à la fois, on obtient ceci : 

<div align=center>
	<a href="/static/upload/quackinux_all.png"><img src="/static/upload/quackinux_all.png" align="center" width="550"/></a>
</div>

#WIN

Special thanks to [Ange Albertini](https://twitter.com/angealbertini) and [his presentation at SSTIC 2013](https://www.sstic.org/2013/presentation/polyglottes_binaires_et_implications/)