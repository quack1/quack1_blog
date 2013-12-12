Title: HIDS OSSEC - De la difficulté de monitorer un système Windows 64 bits
Date: 2013-12-11 18:32 
Author: Quack1
Category: Securité
Tags: Securité, IDS, HIDS, OSSEC, Job, Windows
Slug: ossec_32_64
Summary: 

[OSSEC](https://quack1.me/tag/ossec.html "Tag « OSSEC » sur Quack1.me") est un système de détection d'intrusions qui se base sur des évènements système pour générer ses alertes de sécurité. Il est open-source, mais surtout il est [multiplateformes](http://www.ossec.net/ "OSSEC Homepage"). Dans le cas présent, à $DAY_JOB, nous avons un problème avec son déploiement sur des systèmes Microsoft Windows 64 bits.

Cet HIDS intègre la possibilité de faire des « _File Integrity checking_ », ou _syscheck_. Dans les faits, on donne à l'agent OSSEC une liste de répertoires ou fichiers et/ou clés de registre à surveiller et, toutes les _x_ secondes, il vérifie – récursivement – si le [hash](http://fr.wikipedia.org/wiki/Hash "Fonction de Hachage sur Wikipédia") [MD5](http://fr.wikipedia.org/wiki/MD5 "MD5 sur Wikipédia") d'un de ses fichiers ou clés a changé. Si oui, une alerte est levée.

Dans les faits, cette _feature_ marche très bien sur Linux et Windows.

Sauf que.

L'agent OSSEC n'est disponible sur [la page de téléchargement d'OSSEC](http://www.ossec.net/?page_id=19) qu'en version 32bits. Soit. Au final, il tourne très bien sur des serveurs Windows Server 64bits. On reçoit des logs, des alertes,... Bref, ça tourne.

Et j'ai commencé à mettre en place des _syscheck_. Plus particulièrement, des _syscheck_ sur des clés de registre. Dans l'exemple ci-dessous, je cherche à vérifier si, et quand, la clé `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run` est modifiée. La configuration pour OSSEC est donc :

<a href="/upload/ossec_32_64_conf_ossec.png"><img src="/upload/ossec_32_64_conf_ossec.png" width="600" align="center" /></a>

Et là, c'est le drame. J'ai tenté de modifier cette clé en particulier, de modifier une de ses valeurs pré-existantes, d'en créer ou d'en supprimer, mais impossible d'obtenir une alerte avec OSSEC.

J'ai passé un bon moment à essayer de toutes les manières possibles, de redémarrer l'agent OSSEC, le serveur OSSEC, de modifier les clés avant, ou après avoir touché à l'agent OSSEC. Bref, ça commençait un doucement me saouler, et dans une dernière tentative je décide de retourner fouiller le fond de <s>l'Internet</s> Google.

Et je tombe [là-dessus](http://akbarov.blogspot.fr/2013/08/the-case-of-ossec-registry-monitoring_23.html). Et là, hallelujah ! J'ai trouvé une – presque – solution !

Sur un système 64 bits, les applications compilées en 32 bits n'accèdent pas directement à toutes les clés de registre. Pour assurer une « compatibilité », quand une application 32 bits tente d'accéder à certaines clés (la liste de celles-ci est (heureusement) [donnée par Microsoft](http://msdn.microsoft.com/en-us/library/windows/desktop/aa384253%28v=vs.85%29.aspx "Registry Keys Affected by WOW64")), elle est redirigée vers une autre clé.

Dans mon exemple, en utilisant les outils de la [suite SysInternals](http://technet.microsoft.com/en-gb/sysinternals/bb842062 "") de Microsoft, on peut observer que mon agent OSSEC 32 bits, configuré pour lire la valeur de `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Run`, accède en réalité à `HKEY_LOCAL_MACHINE\Software`**`\WOW6432Node\`**`Microsoft\Windows\CurrentVersion\Run`.

<a href="/upload/ossec_32_64_sysinternal.png"><img src="/upload/ossec_32_64_sysinternal.png" width="600" align="center" /></a>

C'est donc pour cette raison que, quand je modifiait une clé de registre que je pensais être motinorée par OSSEC, en réalité ce n'était pas la bonne qui était surveillée.

Au final, si je modifie la bonne clé de registre, j'obtiens des alertes OSSEC.

<a href="/upload/ossec_32_64_regedit.png"><img src="/upload/ossec_32_64_regedit.png" width="600" align="center" /></a>

<a href="/upload/ossec_32_64_alert.png"><img src="/upload/ossec_32_64_alert.png" width="600" align="center" /></a>

<div align="center" style="color:#ccc;">☠</div>

Ce mode de compatibilité ne s'applique pas qu'aux clés de registre. Nous avons exactement le même problème avec les fichiers et répertoires. Les applications 32bits n'accèdent pas directement à `C:\Windows\System32`, mais plutôt à `C:\Windows\SysWOW64`[^1]. 

Dans ce cas précis, il existe un contournement, donné par [Microsoft](http://msdn.microsoft.com/en-us/library/windows/desktop/aa384187%28v=vs.85%29.aspx "File System Redirector"). Pour accéder au « vrai » répertoire `C:\Windows\System32` depuis une application 32 bits, il faut utiliser le répertoire `C:\Windows\Sysnative`[^2].

<div align="center" style="color:#ccc;">☠</div>

Finalement, la solution a été un peu tendue à trouver, mais au moins j'ai trouvé pourquoi ça ne marchait pas.

Il n'existe pas de solution pour le problème des clés de registre, je n'ai pu en trouver que pour les _syscheck_ sur les répertoires.

<div align="center" style="color:#ccc;">☠</div>

Finalement, les _syscheck_ sous Windows 64 bits, c'est bien ou pas ?

- Oui. Ça permet de monitorer des répertoires, des fichiers ou des clés de registres proprement et simplement ;
- Par contre, le mode de compatibilité de Windows fout la merde partout. L'agent OSSEC n'est disponible officiellement qu'en 32 bits, et pas les ressources aujourd'hui pour se pencher sur une adaptation pour recompilation en 64 bits. 

On peut quand même se débrouiller pour superviser complètement le système, mais ça implique de maintenir des règles _syscheck_ en double (pour le mode 32 et le mode 64 bits), et cette variation ne marchera qu'avec les répertoires, et pas les clés de registre.


[^1]: Plus précisément, les chemins d'accès sont `%windir%\System32` et `%windir%\SysWOW64`.
[^2]: Ici aussi, le chemin exact est `%windir%\Sysnative`.