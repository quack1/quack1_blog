Title: Recon-ng : _Next Generation Web Reconnaissance_
Date: 2013-02-07 08:54
Author: Quack1
Category: Pentest
Slug: recon-ng
Tags: reconnaissance, passive, publique, pentest, osint, recon-ng, web
Summary: Recon-ng, ou le nouvel outil de reconnaissance Web publique.

<div align=center><img src="static/upload/recon-ng.png" width="600" height="169" align=center /></div>

Je suis depuis la toute fin de l'année dernière en train de vous écrire la deuxième partie de ma série d'article sur le [pentest](./tag/serie_pentest.html "Tag : serie_pentest"), dédiée à la reconnaissance publique de la cible, en se servant de toutes les données disponibles un peu partout dans les tuyaux.

Et bien, [@LaNMaSteR53](https://twitter.com/lanmaster53), auditeur en sécurité américain, a publié au milieu du mois de janvier dernier un framework permettant de réaliser efficacement et rapidement une reconnaissance publique de votre cible.

L'outil a été présenté par son créateur à la Hack3rcon et au DerbyCon très récemment, et 1 vidéo pour chacun de ces talks est [disponible sur son site](http://lanmaster53.com/talks/).

Cependant, je vais vous présenter ce très bon outil ici (en français ;-) ).

Le programme est un Free Software (diffusé sous GPL), codé en Python, et disponible sur le [dépôt Git du créateur sur Bitbucket](https://bitbucket.org/LaNMaSteR53/recon-ng).

Pour le récupérer sur votre machine, vous devrez cloner le projet en local. Notez que les mises à jour seront à effectuer également via Git.

	:::bash
	# Pour le clonage : 
	$ git clone https://bitbucket.org/LaNMaSteR53/recon-ng
	# Pour les mises à jour : 
	$ cd recon-ng/
	$ git pull

Pour les gens qui ne connaissent pas Metasploit, l'utilisation de **recon-ng** sera quelque peu spéciale à prendre en main. Pour les autres, vous ne serez pas dépaysés.

Le programme, une fois lancé, vous offre un invite-de-commandes permettant d'utiliser chacun de ses modules. Si vous tapez une commande inconnue pour le framework, elle sera exécutée dans votre shell.

Les commandes disponibles sont (liste non exhaustive) : 

- `help` : affiche une aide
- `modules` : liste les modules disponibles
- `exit` : quitte le module dans lequel vous vous trouvez, sinon quitte le programme
- `options` : affiche les options du programme
- `use` : charge un module pour l'utiliser
- `info` : affiche les informations sur le module, et en particulier ses arguments
- `set` : donne une valeur à un argument du module chargé
- `search` : effectue une recherche dans la liste des modules
- `run` : exécute le module chargé, avec les arguments donnés

&nbsp;

Je vais rapidement vous présenter les informations que vous pouvez obtenir avec cet outil, puis je vous ferais une démo "textuelle" du fonctionnement d'un module, afin que vous ayez une vision plus réelle de son utilisation.

- `auxiliary::googli` : Utilise le site [http://goog.li](http://goog.li) pour retrouver la valeur en clair d'un hash donné
- `auxiliary::noisette` : Effectue la même opération que `googli` mais avec le site [http://noisette.ch](http://noisette.ch)
- `auxiliary::pwnedlist` : Verifie sur le site [http://PownedList.com](http://PownedList.com) si une adresse mail a été compromise
- `auxiliary::resolve` : Retrouve les noms d'hôte associés à une adresse IP
- `auxiliary::server_enum` : Permet de retrouver des informations concernant le serveur qui fait tourner un site Web
- `contacts::linkedin` : Récupère des informations sur des salariés d'un société via Linkedin (nécéssite une clé d'API). Il existe un module de contact pour le site [Jigsaw](http://www.jigsaw.com/). Cependant, le site n'a pas l'air très utilisé en France
- `hosts::*` : Permet d'effectuer un "brute-force" (raisonnable : 1 requête toutes les 15 secondes pour éviter le blacklistage de votre IP) sur différents moteurs de recherche pour retrouver des noms de domaines ou des adresses mail. Le module `hosts::brute-force` effectue un brute-force sur les données contenues dans les DNS en testant une liste prédéfinie de sous-domaines
- `output::*` : Permet d'exporter certaines des données au format CVS ou HTML
- `pwnedlist::*` : Toues ces modules permettent d'exploiter les données disponibles sur le site [http://PownedList.com](http://PownedList.com)

Enfin, notez que toutes les données sont stockées au fur et à mesure des lancements des modules dans une base de données interne, que vous pourrez par la suite exploiter dans des scripts au moyen de requêtes SQL.

&nbsp;

Et maintenant, le temps de la "démo" est arrivé!

Je vais vous donner la trace d'exécution de l'utilisation du programme afin d'exécuter un brute-force sur Google pour recupérer les sous-domaines de `google.com` (quoi ? Vous avez dit Inception ?), puis pour chercher sur Jigsaw les noms des employés de Mozilla.

	:::bash
	quack@spiderman:$ ./recon-ng.py 

	    _/_/_/    _/_/_/_/    _/_/_/    _/_/_/    _/      _/            _/      _/    _/_/_/
	   _/    _/  _/        _/        _/      _/  _/_/    _/            _/_/    _/  _/       
	  _/_/_/    _/_/_/    _/        _/      _/  _/  _/  _/  _/_/_/_/  _/  _/  _/  _/  _/_/_/
	 _/    _/  _/        _/        _/      _/  _/    _/_/            _/    _/_/  _/      _/ 
	_/    _/  _/_/_/_/    _/_/_/    _/_/_/    _/      _/            _/      _/    _/_/_/    

	             [recon-ng v1.00 Copyright (C) 2013, Tim Tomes (@LaNMaSteR53)]              

	[12] auxiliary modules
	[2] output modules
	[7] hosts modules
	[5] pwnedlist modules
	[2] contacts modules

	recon-ng > use hosts::google
	recon-ng [hosts::google] > info

	  Name:
	    Google Hostname Enumerator

	  Author:
	    Tim Tomes (@LaNMaSteR53)

	  Description:
	    Harvests hosts from Google.com by using the 'site' search operator. This module updates the 'hosts'
	    table of the database with the results.

	  Options:

	    Name     Current Value  Req  Description
	    -------  -------------  ---  -----------
	    domain                  yes  target domain
	    verbose  True           yes  verbose output

	recon-ng [hosts::google] > set domain google.com
	domain => google.com
	recon-ng [hosts::google] > set verbose false
	verbose => false
	recon-ng [hosts::google] > run
	[*] news.google.com
	[*] play.google.com
	[*] translate.google.com
	[*] www.google.com
	[*] images.google.com
	[*] encrypted.google.com
	[*] blogsearch.google.com
	[*] books.google.com
	[*] plus.google.com
	[*] picasaweb.google.com
	[*] developers.google.com
	[*] cloud.google.com
	[*] code.google.com
	[*] knol.google.com
	[*] scholar.google.com
	[*] www.sites.google.com
	[*] sites.google.com
	[*] mail.google.com
	[*] support.google.com
	[*] sketchup.google.com
	[*] accounts.google.com
	[*] adwords.google.com
	[*] chrome.google.com
	[*] groups.google.com
	[*] finance.google.com
	[*] profiles.google.com
	[*] maps.google.com
	[*] investor.google.com
	[*] research.google.com
	[*] productforums.google.com
	[*] docs.google.com
	[*] spreadsheets.google.com
	^C
	[*] 32 total hosts found.
	[*] 11 NEW hosts found!
	recon-ng [hosts::google] > 

_J'ai ici désactivé le mode verbeux, donc le programme ne vous indiquera pas quand il ne trouve plus de résultat, et "tournera dans le vide". Pour pourrez arrêter l'exécution du module par un Ctrl-C._

Au moment où on exécute le module _jigsaw_, il y aura 2 interactions avec l'utilisateur : il demandera de préciser quel est le nom de la companie à analyser. Ensuite, durant les étapes `Query: http://.......`, vous devrez presser Ctrl-C pour arrêter les requêtes et analyser les résultats.

	:::bash
	recon-ng > use contacts::jigsaw
	recon-ng [contacts::jigsaw] > info

	  Name:
	    Jigsaw Contact Enumerator

	  Author:
	    Tim Tomes (@LaNMaSteR53)

	  Description:
	    Harvests contacts from Jigsaw.com. This module updates the 'contacts' table of the database with the
	    results.

	  Options:

	    Name      Current Value  Req  Description
	    --------  -------------  ---  -----------
	    company                  yes  target company name
	    keywords                 no   additional keywords to identify company
	    verbose   True           yes  verbose output

	recon-ng [contacts::jigsaw] > set company Mozilla
	company => Mozilla
	recon-ng [contacts::jigsaw] > run
	[*] Gathering Company IDs...
	[*] Query: http://www.jigsaw.com/FreeTextSearchCompany.xhtml?opCode=search&freeText=Mozilla+
	[*] Query: http://www.jigsaw.com/FreeTextSearchCompany.xhtml?rpage=2&opCode=search&freeText=Mozilla+
	[*] 228351 Mozilla Corporation (64 contacts)
	[*] 5133052 Mozilla Corporation (1 contacts)
	Enter Company ID from list [228351]: 
	[*] Gathering Contact IDs for Company '228351'...
	[*] Query: http://www.jigsaw.com/SearchContact.xhtml?rpage=1&opCode=showCompDir&companyId=228351
	[*] Query: http://www.jigsaw.com/SearchContact.xhtml?rpage=2&opCode=showCompDir&companyId=228351
	^C
	[*] Gathering Contacts...
	[*] Dave Hyatt - Co-Founder
	[*] Dietrich Ayala - Senior Software Engineer
	[*] Carsten Book - Quality Assurance Software Engineer
	[*] David Boswell - Community Manager
	[*] Harvey Anderson - Vice President Business Affairs and General Counse
	[*] Bob Moss - Senior Director of Engineering
	[*] Justin Scott - FireFox Add-Ons Product Manager
	[*] Laura Thomson - Webtools Engineering Manager
	[*] Shyam Mani - Systems Administrator
	[*] Lynn Mock - Board MEMBERS
	[*] Jay Sullivan - Vice President Products
	[*] Anthony Chung - Quality Assurance Manager
	[*] Diane Bisgeier - Program Manager, WebFWD
	[*] Patrick Finch - European Marketing Manager
	[*] Janet Swisher - Developer Documentation Developer at
	[*] Johnny Stenback - Engineering Manager
	[*] Zhenshuo Fang - User Experience Designer
	[*] Natasha Ma - Senior Marketing Manager, Taiwan/Hong Kong Markets
	[*] Olivier Yiptong - Software Engineer
	[*] Barry Munsterteiger - Creative Instigator/Director
	[*] Rebecca Berto - Benefits Specialist
	[*] Jeremy Orem - Systems Engineer
	[*] Justin Dow - Systems Administrator
	[*] Chris Hofmann - Director Special Projects
	[*] Mark Finkle - Developer
	[*] Dave Townsend - Firefox Engineer
	[*] Alexander Limi - Firefox User Experience
	[*] Johnathan Nightingale - Director of Firefox Engineering
	[*] Kai-Chih Hu - Global Engineering Project Manager
	[*] Clint Talbert - Test Development and Automation Team Lead
	[*] William Quiviger - Marketing Executive France
	[*] Leslie Orchard - Senior Web Developer
	[*] Derek Moore - Systems/Network Engineer
	[*] Aleksandr Milewski - Information Technology/Operations Ambassador
	[*] Geo George Mealer - Software Engineer in Test
	[*] Krupa Raj - Senior test Engineer
	[*] Rebecca Billings - Senior Quality Engineer
	[*] Jennifer Morrow - User Experience Designer
	[*] Pascal Finette - Director of the Open Innovation Group and WebFWD
	[*] Dan Mills - Product Manager
	[*] Gervase Markham - Marketing Specialist
	[*] Michael Coates - Senior Manager of Infrastructure Security
	[*] Damon Sicore - Senior Vice President of Engineering
	[*] Curtis Koenig - Senior Security Program Manager
	[*] Deborah Cohen - Vice President Chief of People at Mozilla
	[*] Gary Kovacs - Chief Executive Officer at Mozilla Corporation
	[*] Ed Lim - Systems Administrator
	[*] Kym Lee - Staffing Associate
	[*] Daniel Veditz - Security Lead
	[*] Tanvi Vyas - Security Engineer
	[*] 50 total contacts found.
	[*] 50 NEW contacts found!
	recon-ng [contacts::jigsaw] > 

&nbsp;

Et voilà le travail! N'hésitez pas à écrire et publier vos propres plugins, et dans le cas où vous auriez d'autres questions, vous pouvez me les poser dans les commentaires ou sur [Twitter](http://twitter.com/_Quack1) ou par [mail](quack1blog@gmail.com).