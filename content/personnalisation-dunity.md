Title: Personnalisation d'Unity 
Date: 2011-12-12 06:33
Author: Quack1
Category: Ubuntu
Tags: myunity, personnalisation, ubuntu, unity, planet-libre
Summary: Personnalisation d'Unity avec l'outil myUnity.

J'ai fait une découverte intéressante ce matin en lisant ma timeline. Un tweet d'[@UbuntuFeed](https://twitter.com/#!/UbuntuFeed).

Un petit utilitaire permettant de personnaliser Unity, la nouvelle interface d'Ubuntu (nouvelle, pas tellement, puisqu'Unity est là depuis 2 versions déjà :-/ ). L'appli s'appelle *myunity*, et avait l'air sympa.

Donc j'ai voulu installer ça vite fait, mais en fait elle n'est pas encore présente dans les repositories officiels d'Ubuntu, donc il faut rajouter le ppa.

Somme toute, ça a pas été super long.

<pre>
    $ sudo add-apt-repository ppa:myunity/ppa &amp;&amp; sudo apt-get update &amp;&amp; sudo apt-get install myunity
</pre>

Quand on rajoute le repository, j'ai eu un message me disant que l'application était déjà présente dans les sources officielles d'Ubuntu, en fait pas du tout. Il faut bien rajouter le ppa et mettre à jour l'index apt-get. Ensuite vous pouvez l'utiliser en lançant directement l'appli dans le terminal

<pre>
    $ myunity
</pre>

<div align=center><a href="static/upload/myunity.png"><img src="static/upload/myunity.png" width="450" align="center" /></a></div> 

Au final, après utilisation, je m'attendais quand même à mieux. MyUnity
permet de régler la taille des icônes du dock, la transparence des
icônes, la brillance de celles-ci.... J'espère que ce n'est qu'un début
et qu'on pourra personnaliser Unity plus que ça dans les prochaines
versions.

Normalement, myUnity sera officiellement présente dans les dépôts
d'Ubuntu à partir de la 12.04. Espérons que le lancement d'une version
LTS chez Ubuntu nous offrira un nouvel Unity :)

Si quelqu'un lit ce blog, et qu'en plus il a des solutions pour
personnaliser Unity, je suis preneur ;)

