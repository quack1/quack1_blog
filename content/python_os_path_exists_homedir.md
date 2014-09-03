Title: Python — os.path.exists("~/something") retourne toujours False
Date: 2014-09-03 13:02
Author: Quack1
Category: Geek
Tags: Python, Linux, planet-libre
Slug: python_os_path_exists_homedir
Summary: 
Lang: fr

_Strange fact_ que je viens de découvrir dans Python[^1].

La méthode [`os.path.exists()`](https://docs.python.org/2/library/os.path.html#os.path.exists "Python v2.7.8 Documentation - os.path.exists(path)") retourne toujours `False` quand l'argument commence par un `~`.

    :::Python
    >>> import os.path
    >>> os.path.exists("~/.my.cnf")
    False

Il faut utiliser la méthode [`os.path.expanduser()`](https://docs.python.org/2/library/os.path.html#os.path.expanduser "Python v2.7.8 Documentation - os.path.expanduser(path)") pour remplacer le `~` par le contenu de la variable `$HOME` — et ainsi obtenir un chemin absolu — pour que le résultat de la méthode soit correct.

    :::Python
    >>> os.path.expanduser("~/.my.cnf")
    '/home/quack/.my.cnf'
    >>> os.path.exists(os.path.expanduser("~/.my.cnf"))
    True

Selon la documentation, le problème pourrait provenir d'un appel à la méthode `os.stat`, même si celle si ne génère pas d'autre erreur que « `OSError: [Errno 2] No such file or directory: '~/.my.cnf'` » dans mon shell.

Bizarre. À l'avenir, je saurais que le problème peut venir de là !

[^1]: Ici en version 2.7.6 sur une xUbuntu. Le bug est le même sur Python 3.4.0